-- Enable pgvector extension
CREATE EXTENSION IF NOT EXISTS vector;

-- Create tables for code artifacts
CREATE TABLE IF NOT EXISTS symbols (
    id SERIAL PRIMARY KEY,
    file_path TEXT NOT NULL,
    symbol_name TEXT NOT NULL,
    symbol_type TEXT NOT NULL,
    definition_location TEXT,
    module_name TEXT,
    embedding VECTOR(1536),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS imports (
    id SERIAL PRIMARY KEY,
    file_path TEXT NOT NULL,
    import_statement TEXT NOT NULL,
    imported_module TEXT,
    import_type TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS call_graphs (
    id SERIAL PRIMARY KEY,
    caller_file TEXT NOT NULL,
    caller_function TEXT NOT NULL,
    callee_file TEXT NOT NULL,
    callee_function TEXT NOT NULL,
    call_location TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS api_routes (
    id SERIAL PRIMARY KEY,
    file_path TEXT NOT NULL,
    route_path TEXT NOT NULL,
    http_method TEXT NOT NULL,
    handler_function TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS code_embeddings (
    id SERIAL PRIMARY KEY,
    file_path TEXT NOT NULL,
    code_snippet TEXT NOT NULL,
    embedding VECTOR(1536),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes for better performance
CREATE INDEX IF NOT EXISTS idx_symbols_name ON symbols(symbol_name);
CREATE INDEX IF NOT EXISTS idx_symbols_module ON symbols(module_name);
CREATE INDEX IF NOT EXISTS idx_imports_module ON imports(imported_module);
CREATE INDEX IF NOT EXISTS idx_call_graph_caller ON call_graphs(caller_function);
CREATE INDEX IF NOT EXISTS idx_api_routes_path ON api_routes(route_path);
CREATE INDEX IF NOT EXISTS idx_embeddings_similarity ON code_embeddings USING hnsw (embedding vector_ip_ops);