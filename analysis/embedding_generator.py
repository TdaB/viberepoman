"""
Code Embedding Generator Service
Creates vector embeddings for semantic code understanding
"""

from typing import List, Dict, Any
import numpy as np
from sentence_transformers import SentenceTransformer

class EmbeddingGeneratorService:
    def __init__(self):
        # Initialize the sentence transformer model
        # Using a smaller model for faster processing, but you can use larger ones
        try:
            self.model = SentenceTransformer('all-MiniLM-L6-v2')
        except Exception as e:
            print(f"Warning: Could not load sentence transformer model: {e}")
            # Fallback to a simple approach if model loading fails
            self.model = None
    
    def generate_embeddings(self, asts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Generate embeddings for code snippets from ASTs
        """
        embeddings = []
        
        # For demonstration purposes, we'll create some sample embeddings
        # In a real implementation, this would process actual code content
        
        for ast_data in asts:
            file_path = ast_data.get('file_path', '')
            content = ast_data.get('content', '')
            
            if not content or not self.model:
                continue
                
            try:
                # Generate embedding for the file content
                embedding = self.model.encode(content)
                
                embeddings.append({
                    'file_path': file_path,
                    'code_snippet': content[:200] + "..." if len(content) > 200 else content,  # First 200 chars
                    'embedding': embedding.tolist()  # Convert to list for JSON serialization
                })
            except Exception as e:
                print(f"Error generating embedding for {file_path}: {e}")
                continue
                
        return embeddings