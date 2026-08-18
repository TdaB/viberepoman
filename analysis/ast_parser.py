"""
AST Parser Service
Parses code files into Abstract Syntax Trees
"""

import os
import ast
from typing import Dict, List, Any
from pathlib import Path

class ASTParserService:
    def __init__(self):
        self.supported_extensions = {'.py'}
        
    def parse_file(self, file_path: str) -> Dict[str, Any]:
        """
        Parse a single Python file into an AST
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Parse the AST
            tree = ast.parse(content, filename=file_path)
            
            return {
                'file_path': file_path,
                'ast': tree,
                'content': content
            }
        except Exception as e:
            print(f"Error parsing {file_path}: {str(e)}")
            return {
                'file_path': file_path,
                'ast': None,
                'content': None,
                'error': str(e)
            }
    
    def parse_directory(self, directory_path: str) -> List[Dict[str, Any]]:
        """
        Parse all Python files in a directory
        """
        asts = []
        
        # Walk through the directory recursively
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if any(file.endswith(ext) for ext in self.supported_extensions):
                    file_path = os.path.join(root, file)
                    ast_result = self.parse_file(file_path)
                    asts.append(ast_result)
        
        return asts
    
    def get_ast_structure(self, tree) -> Dict[str, Any]:
        """
        Extract structural information from AST
        """
        if not tree:
            return {}
            
        # Simple AST structure extraction
        structure = {
            'types': [],
            'function_count': 0,
            'class_count': 0,
            'import_count': 0
        }
        
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef):
                structure['function_count'] += 1
            elif isinstance(node, ast.ClassDef):
                structure['class_count'] += 1
            elif isinstance(node, ast.Import) or isinstance(node, ast.ImportFrom):
                structure['import_count'] += 1
                
        return structure