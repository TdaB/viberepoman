"""
Import Resolver Service
Analyzes import statements and resolves dependencies
"""

import ast
from typing import List, Dict, Any
from pathlib import Path

class ImportResolverService:
    def __init__(self):
        pass
    
    def resolve_imports(self, asts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Resolve imports from a list of ASTs
        """
        imports = []
        
        for ast_data in asts:
            file_path = ast_data.get('file_path', '')
            tree = ast_data.get('ast')
            
            if not tree:
                continue
                
            # Extract all import statements from the AST
            for node in ast.walk(tree):
                import_info = self._extract_import_from_node(node, file_path)
                if import_info:
                    imports.append(import_info)
        
        return imports
    
    def _extract_import_from_node(self, node: ast.AST, file_path: str) -> Dict[str, Any]:
        """
        Extract import information from a single AST node
        """
        if isinstance(node, ast.Import):
            # Handle 'import module' statements
            for alias in node.names:
                return {
                    'file_path': file_path,
                    'import_statement': f"import {alias.name}",
                    'imported_module': alias.name,
                    'import_type': 'module',
                    'alias': alias.asname if alias.asname else None
                }
                
        elif isinstance(node, ast.ImportFrom):
            # Handle 'from module import x' statements
            module_name = node.module or ''
            return {
                'file_path': file_path,
                'import_statement': f"from {module_name} import {', '.join([alias.name for alias in node.names])}",
                'imported_module': module_name,
                'import_type': 'from_module',
                'level': node.level
            }
            
        return None