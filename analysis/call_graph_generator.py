"""
Call Graph Generator Service
Identifies function calls and builds call relationships
"""

import ast
from typing import List, Dict, Any

class CallGraphGeneratorService:
    def __init__(self):
        pass
    
    def generate_call_graphs(self, asts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Generate call graphs from a list of ASTs
        """
        call_graphs = []
        
        for ast_data in asts:
            file_path = ast_data.get('file_path', '')
            tree = ast_data.get('ast')
            
            if not tree:
                continue
                
            # Extract all function calls from the AST
            for node in ast.walk(tree):
                call_info = self._extract_call_from_node(node, file_path)
                if call_info:
                    call_graphs.append(call_info)
        
        return call_graphs
    
    def _extract_call_from_node(self, node: ast.AST, file_path: str) -> Dict[str, Any]:
        """
        Extract call information from a single AST node
        """
        if isinstance(node, ast.Call):
            # Get the function being called
            func = node.func
            
            # Handle different types of function calls
            if isinstance(func, ast.Name):
                return {
                    'caller_file': file_path,
                    'caller_function': '',  # We'll need to track this from context
                    'callee_file': file_path,
                    'callee_function': func.id,
                    'call_location': f"{file_path}:{node.lineno}"
                }
            elif isinstance(func, ast.Attribute):
                # Handle method calls like obj.method()
                return {
                    'caller_file': file_path,
                    'caller_function': '',  # We'll need to track this from context
                    'callee_file': file_path,
                    'callee_function': func.attr,
                    'call_location': f"{file_path}:{node.lineno}"
                }
                
        return None