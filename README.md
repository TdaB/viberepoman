# Repo Explainer System

This project implements a comprehensive repository explainer system with the following architecture:

## Architecture Overview
```
┌───────────────────────┐
│      Git Repository   │
└───────────┬───────────┘
            │
            ▼
┌─────────────────────┐
│ Knowledge Builder   │
│                     │
│ AST                 │
│ Symbols             │
│ Imports             │
│ Call Graph          │
│ API Routes          │
│ Embeddings          │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│ PostgreSQL/pgvector │
└──────────┬──────────┘
           │
           │
  ┌────────▼────────┐
  │ Explainer Agent │
  └────────┬────────┘
           │
   ┌───────┼────────┐
   ▼       ▼        ▼
Vector Search Graph Search Code Search
   │       │        │
   └───────┼────────┘
           ▼
        Evidence
           │
           ▼
          LLM
           │
           ▼
        Answer
```

## Components

### 1. Knowledge Builder (Multi-Service Python Analysis)
- AST Parser Service: Parses code into Abstract Syntax Trees
- Symbol Extractor Service: Identifies functions, classes, variables  
- Import Resolver Service: Analyzes import statements and dependencies
- Call Graph Generator Service: Builds function call relationships
- API Route Detector Service: Identifies REST/GraphQL endpoints
- Code Embedding Generator Service: Creates vector embeddings for semantic understanding

### 2. Data Storage Layer
- PostgreSQL + pgvector: Database with vector capabilities for storing code artifacts and embeddings

### 3. Explainer Agent
- Query processing and routing
- Vector search integration  
- Graph-based search capabilities
- Code search functionality

### 4. LLM Integration Layer
- FastAPI Backend: REST API service for LLM queries
- Evidence aggregation from different search methods

### 5. Frontend Interface
- React/TypeScript: Minimal web interface for querying and viewing responses

## Implementation Plan

### Phase 1: Environment Setup
1. Create project structure with Docker configuration
2. Set up PostgreSQL database with pgvector extension  
3. Configure FastAPI backend environment

### Phase 2: Static Analysis Services (Detailed)
1. AST Parser Service: Parse code files into Abstract Syntax Trees
2. Symbol Extractor Service: Identify and extract symbols from ASTs
3. Import Resolver Service: Analyze import statements and resolve dependencies
4. Call Graph Generator Service: Identify function calls and build call graphs  
5. API Route Detector Service: Identify REST API endpoints
6. Code Embedding Generator Service: Create vector embeddings for semantic understanding

### Phase 3: Data Pipeline
1. Create database schema for storing code artifacts
2. Implement data ingestion pipeline
3. Set up vector storage for embeddings

### Phase 4: Search & Query System
1. Implement vector search functionality
2. Add graph-based search capabilities
3. Integrate code search features

### Phase 5: LLM Integration
1. Configure FastAPI endpoint for LLM queries
2. Implement evidence aggregation from search methods  
3. Create response generation pipeline

### Phase 6: Frontend Development
1. Build React interface for querying
2. Implement response display and visualization