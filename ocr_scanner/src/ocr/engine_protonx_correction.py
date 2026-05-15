"""
ProtonX Legal Text Correction Engine for OCR Post-Processing

This module provides Vietnamese text correction using the ProtonX Legal Text Correction model,
specifically optimized for OCR post-processing (especially PaddleOCR outputs).

Model: protonx-models/protonx-legal-tc
- Trained on 800,000 correction pairs
- 30,000 manually annotated by Vietnamese experts
- Specialized for legal/administrative documents
- No hallucination, confidence-based correction

Performance: ~95%+ accuracy on Vietnamese legal/admin documents
"""

from typing import List, Dict, Optional
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import os
import sys
import re

# Add parent directory to path for config access
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

# Global instance (lazy loaded)
_protonx_corrector = None


class ProtonXCorrector:
    """
    ProtonX-based text correction for Vietnamese OCR post-processing.
    
    Features:
    - Singleton pattern for efficient model loading
    - Text chunking for long documents (max 160 tokens)
    - CPU/GPU support
    - Batch processing
    """
    
    def __init__(self, model_path: str = None, max_tokens: int = 160):
        """
        Initialize ProtonX corrector.
        
        Args:
            model_path: Local model path or HuggingFace model path (default: local models directory)
            max_tokens: Maximum tokens per chunk (default: 160)
        """
        print("🔧 Initializing ProtonX Text Correction...")
        
        # Use local model path by default for portable deployment
        if model_path is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            local_model_path = os.path.join(base_dir, "..", "..", "models", "protonx-legal-tc", "snapshots", "04d5b4062ef2ac8846c27ed1b07765a8b3c049c7")
            local_model_path = os.path.normpath(local_model_path)
            
            if os.path.exists(local_model_path):
                model_path = local_model_path
                print(f"📁 Using local model: {local_model_path}")
            else:
                # Fallback to HuggingFace download
                model_path = "protonx-models/protonx-legal-tc"
                print(f"🌐 Local model not found, will download from HuggingFace")
        
        self.model_path = model_path
        self.max_tokens = max_tokens
        
        # Load tokenizer and model
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_path)
            self.model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
            
            # Setup device
            self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            self.model.to(self.device)
            self.model.eval()
            
            device_name = "GPU" if torch.cuda.is_available() else "CPU"
            print(f"✅ ProtonX ready on {device_name}")
            
        except Exception as e:
            print(f"❌ Error loading ProtonX model: {e}")
            print("💡 Tip: Run 'pip install transformers>=4.46.3 tokenizers>=0.20.3'")
            raise
    
    def _split_into_sentences(self, text: str) -> List[str]:
        """
        Split text into sentences for chunking.
        
        Args:
            text: Input text
            
        Returns:
            List of sentences
        """
        # Split by common Vietnamese sentence endings
        sentences = re.split(r'([.!?;]\s+)', text)
        
        # Recombine sentences with their punctuation
        result = []
        for i in range(0, len(sentences) - 1, 2):
            sentence = sentences[i]
            if i + 1 < len(sentences):
                sentence += sentences[i + 1]
            result.append(sentence.strip())
        
        # Add last sentence if exists
        if len(sentences) % 2 == 1:
            result.append(sentences[-1].strip())
        
        return [s for s in result if s]
    
    def _chunk_text(self, text: str) -> List[str]:
        """
        Split text into chunks that fit within max_tokens limit.
        
        Args:
            text: Input text
            
        Returns:
            List of text chunks
        """
        sentences = self._split_into_sentences(text)
        chunks = []
        current_chunk = []
        current_length = 0
        
        for sentence in sentences:
            # Tokenize to check length
            tokens = self.tokenizer.encode(sentence, add_special_tokens=False)
            sentence_length = len(tokens)
            
            # If single sentence is too long, split it
            if sentence_length > self.max_tokens:
                # Save current chunk if exists
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                    current_chunk = []
                    current_length = 0
                
                # Split long sentence by words
                words = sentence.split()
                temp_chunk = []
                temp_length = 0
                
                for word in words:
                    word_tokens = self.tokenizer.encode(word, add_special_tokens=False)
                    word_length = len(word_tokens)
                    
                    if temp_length + word_length <= self.max_tokens:
                        temp_chunk.append(word)
                        temp_length += word_length
                    else:
                        if temp_chunk:
                            chunks.append(' '.join(temp_chunk))
                        temp_chunk = [word]
                        temp_length = word_length
                
                if temp_chunk:
                    chunks.append(' '.join(temp_chunk))
            
            # If adding sentence exceeds limit, save current chunk
            elif current_length + sentence_length > self.max_tokens:
                if current_chunk:
                    chunks.append(' '.join(current_chunk))
                current_chunk = [sentence]
                current_length = sentence_length
            
            # Add sentence to current chunk
            else:
                current_chunk.append(sentence)
                current_length += sentence_length
        
        # Add remaining chunk
        if current_chunk:
            chunks.append(' '.join(current_chunk))
        
        return chunks
    
    def correct_text(self, text: str, num_beams: int = 10) -> str:
        """
        Correct a single text chunk (must be <= max_tokens).
        
        Args:
            text: Input text (should be within token limit)
            num_beams: Number of beams for beam search (default: 10)
            
        Returns:
            Corrected text
        """
        if not text or not text.strip():
            return text
        
        try:
            inputs = self.tokenizer(
                text,
                return_tensors="pt",
                truncation=True,
                max_length=self.max_tokens
            ).to(self.device)
            
            with torch.no_grad():
                outputs = self.model.generate(
                    **inputs,
                    num_beams=num_beams,
                    num_return_sequences=1,
                    max_new_tokens=self.max_tokens,
                    early_stopping=True
                )
            
            corrected = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
            return corrected
            
        except Exception as e:
            print(f"⚠️ Error correcting text: {e}")
            return text  # Return original on error
    
    def correct_text_chunked(self, text: str, num_beams: int = 10, preserve_formatting: bool = True) -> str:
        """
        Correct long text by automatically chunking.
        
        Args:
            text: Input text (any length)
            num_beams: Number of beams for beam search
            preserve_formatting: Whether to preserve original line breaks
            
        Returns:
            Corrected text
        """
        if not text or not text.strip():
            return text
        
        # Preserve original line breaks
        original_lines = text.split('\n') if preserve_formatting else [text]
        corrected_lines = []
        
        for line in original_lines:
            if not line.strip():
                corrected_lines.append(line)
                continue
            
            # Chunk the line if needed
            chunks = self._chunk_text(line)
            corrected_chunks = [self.correct_text(chunk, num_beams) for chunk in chunks]
            corrected_line = ' '.join(corrected_chunks)
            corrected_lines.append(corrected_line)
        
        return '\n'.join(corrected_lines) if preserve_formatting else ' '.join(corrected_lines)
    
    def correct_batch(self, texts: List[str], num_beams: int = 10) -> List[str]:
        """
        Correct multiple texts.
        
        Args:
            texts: List of input texts
            num_beams: Number of beams for beam search
            
        Returns:
            List of corrected texts
        """
        return [self.correct_text_chunked(text, num_beams) for text in texts]


def get_protonx_corrector(max_tokens: int = 160) -> ProtonXCorrector:
    """
    Get singleton ProtonX corrector instance.
    
    Args:
        max_tokens: Maximum tokens per chunk
        
    Returns:
        ProtonXCorrector instance
    """
    global _protonx_corrector
    
    if _protonx_corrector is None:
        _protonx_corrector = ProtonXCorrector(max_tokens=max_tokens)
    
    return _protonx_corrector


def correct_vietnamese_text_protonx(text: str, preserve_formatting: bool = True) -> str:
    """
    Easy-to-use function to correct Vietnamese text using ProtonX.
    
    Args:
        text: Input text (any length)
        preserve_formatting: Whether to preserve line breaks
        
    Returns:
        Corrected text
    """
    corrector = get_protonx_corrector()
    return corrector.correct_text_chunked(text, preserve_formatting=preserve_formatting)


if __name__ == "__main__":
    # Test the corrector
    import sys
    
    if len(sys.argv) > 1:
        test_text = sys.argv[1]
    else:
        # Sample OCR errors
        test_text = """V vic np h so hc phí
Điều 10. Điều kien bảo đm an ninh mạng đối vói thiết bi, phân cứng
Hệ thông thông tin x lý bí mt nhà nước không được kết ni vói mạng Internet."""
    
    print("=" * 80)
    print("Testing ProtonX Text Correction")
    print("=" * 80)
    print(f"\n📝 Input:\n{test_text}\n")
    
    corrected = correct_vietnamese_text_protonx(test_text)
    
    print(f"✅ Output:\n{corrected}\n")
    print("=" * 80)
