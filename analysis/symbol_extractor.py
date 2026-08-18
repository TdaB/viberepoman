"""
Symbol Extractor Service
Extracts symbols (functions, classes, variables) from ASTs
"""

import ast
from typing import List, Dict, Any

class SymbolExtractorService:
    def __init__(self):
        pass
    
    def extract_symbols(self, asts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Extract symbols from a list of ASTs
        """
        symbols = []
        
        for ast_data in asts:
            file_path = ast_data.get('file_path', '')
            tree = ast_data.get('ast')
            
            if not tree:
                continue
                
            # Extract all symbols from the AST
            for node in ast.walk(tree):
                symbol_info = self._extract_symbol_from_node(node, file_path)
                if symbol_info:
                    symbols.append(symbol_info)
        
        return symbols
    
    def _extract_symbol_from_node(self, node: ast.AST, file_path: str) -> Dict[str, Any]:
        """
        Extract symbol information from a single AST node
        """
        symbol_info = {
            'file_path': file_path,
            'symbol_name': '',
            'symbol_type': '',
            'definition_location': '',
            'module_name': ''
        }
        
        if isinstance(node, ast.FunctionDef):
            symbol_info.update({
                'symbol_name': node.name,
                'symbol_type': 'function',
                'definition_location': f"{file_path}:{node.lineno}",
                'module_name': self._get_module_name(file_path)
            })
            return symbol_info
            
        elif isinstance(node, ast.ClassDef):
            symbol_info.update({
                'symbol_name': node.name,
                'symbol_type': 'class',
                'definition_location': f"{file_path}:{node.lineno}",
                'module_name': self._get_module_name(file_path)
            })
            return symbol_info
            
        elif isinstance(node, ast.Assign):
            # Handle variable assignments
            if len(node.targets) > 0:
                target = node.targets[0]
                if isinstance(target, ast.Name):
                    symbol_info.update({
                        'symbol_name': target.id,
                        'symbol_type': 'variable',
                        'definition_location': f"{file_path}:{node.lineno}",
                        'module_name': self._get_module_name(file_path)
                    })
                    return symbol_info
                    
        elif isinstance(node, ast.AnnAssign):
            # Handle annotated assignments
            if isinstance(node.target, ast.Name):
                symbol_info.update({
                    'symbol_name': node.target.id,
                    'symbol_type': 'variable',
                    'definition_location': f"{file_path}:{node.lineno}",
                    'module_name': self._get_module_name(file_path)
                })
                return symbol_info
                
        return None
    
    def _get_module_name(self, file_path: str) -> str:
        """
        Extract module name from file path
        """
        import os
        base_name = os.path.basename(file_path)
        if base_name.endswith('.py'):
            return base_name[:-3]
        return base_name