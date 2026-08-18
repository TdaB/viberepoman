"""
API Route Detector Service
Identifies REST API endpoints and GraphQL schemas
"""

import ast
from typing import List, Dict, Any

class APIRouteDetectorService:
    def __init__(self):
        # Common framework decorators for route detection
        self.framework_decorators = {
            'flask': ['route', 'add_url_rule'],
            'django': ['url', 'path'],
            'fastapi': ['get', 'post', 'put', 'delete', 'patch'],
            'express': ['get', 'post', 'put', 'delete']
        }
    
    def detect_routes(self, asts: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Detect API routes from a list of ASTs
        """
        routes = []
        
        for ast_data in asts:
            file_path = ast_data.get('file_path', '')
            tree = ast_data.get('ast')
            
            if not tree:
                continue
                
            # Extract all route information from the AST
            for node in ast.walk(tree):
                route_info = self._extract_route_from_node(node, file_path)
                if route_info:
                    routes.append(route_info)
        
        return routes
    
    def _extract_route_from_node(self, node: ast.AST, file_path: str) -> Dict[str, Any]:
        """
        Extract route information from a single AST node
        """
        # Handle function decorators (common in frameworks like Flask, FastAPI)
        if isinstance(node, ast.FunctionDef):
            for decorator in node.decorator_list:
                route_info = self._extract_route_from_decorator(decorator, node, file_path)
                if route_info:
                    return route_info
                    
        return None
    
    def _extract_route_from_decorator(self, decorator: ast.AST, function_node: ast.FunctionDef, file_path: str) -> Dict[str, Any]:
        """
        Extract route information from a decorator
        """
        if isinstance(decorator, ast.Name):
            # Simple decorator like @app.route('/path')
            decorator_name = decorator.id
            
            # Check if it's a framework route decorator
            for framework, decorators in self.framework_decorators.items():
                if decorator_name in decorators:
                    return {
                        'file_path': file_path,
                        'route_path': self._get_route_path(decorator),
                        'http_method': decorator_name,
                        'handler_function': function_node.name,
                        'framework': framework
                    }
                    
        elif isinstance(decorator, ast.Call):
            # Decorator with arguments like @app.route('/path', methods=['GET'])
            if isinstance(decorator.func, ast.Name):
                decorator_name = decorator.func.id
                
                # Check if it's a framework route decorator  
                for framework, decorators in self.framework_decorators.items():
                    if decorator_name in decorators:
                        return {
                            'file_path': file_path,
                            'route_path': self._get_route_path(decorator),
                            'http_method': decorator_name,
                            'handler_function': function_node.name,
                            'framework': framework
                        }
        
        return None
    
    def _get_route_path(self, decorator: ast.AST) -> str:
        """
        Extract route path from decorator arguments
        """
        if isinstance(decorator, ast.Call):
            # Look for the first argument that might be the route path
            if decorator.args:
                arg = decorator.args[0]
                if isinstance(arg, ast.Str):  # Python 3.7+
                    return arg.s
                elif isinstance(arg, ast.Constant) and isinstance(arg.value, str):  # Python 3.8+
                    return arg.value
                    
        return '/'