#!/usr/bin/env python3
"""
Main entry point for the Python Analysis Services
This file orchestrates all the analysis services
"""

import os
import sys
from typing import Dict, Any

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from ast_parser import ASTParserService
from symbol_extractor import SymbolExtractorService
from import_resolver import ImportResolverService
from call_graph_generator import CallGraphGeneratorService
from api_route_detector import APIRouteDetectorService
from embedding_generator import EmbeddingGeneratorService

class AnalysisOrchestrator:
    def __init__(self):
        self.ast_parser = ASTParserService()
        self.symbol_extractor = SymbolExtractorService()
        self.import_resolver = ImportResolverService()
        self.call_graph_generator = CallGraphGeneratorService()
        self.api_route_detector = APIRouteDetectorService()
        self.embedding_generator = EmbeddingGeneratorService()
        
    def analyze_codebase(self, code_directory: str) -> Dict[str, Any]:
        """
        Analyze a complete codebase and extract all knowledge artifacts
        """
        print(f"Starting analysis of codebase at {code_directory}")
        
        # Step 1: Parse ASTs
        asts = self.ast_parser.parse_directory(code_directory)
        
        # Step 2: Extract symbols
        symbols = self.symbol_extractor.extract_symbols(asts)
        
        # Step 3: Resolve imports
        imports = self.import_resolver.resolve_imports(asts)
        
        # Step 4: Generate call graphs
        call_graphs = self.call_graph_generator.generate_call_graphs(asts)
        
        # Step 5: Detect API routes
        api_routes = self.api_route_detector.detect_routes(asts)
        
        # Step 6: Generate embeddings
        embeddings = self.embedding_generator.generate_embeddings(asts)
        
        return {
            'symbols': symbols,
            'imports': imports,
            'call_graphs': call_graphs,
            'api_routes': api_routes,
            'embeddings': embeddings
        }

def main():
    """Main function to run analysis services"""
    print("Repo Explainer - Analysis Services")
    print("=" * 40)
    
    # For demonstration, we'll create a simple test case
    # In production, this would be triggered by the orchestrator service
    
    orchestrator = AnalysisOrchestrator()
    
    # This is where you'd pass in actual code directory to analyze
    # For now, let's just show the services are ready
    print("Analysis services initialized successfully")
    print("Ready to process code artifacts...")

if __name__ == "__main__":
    main()