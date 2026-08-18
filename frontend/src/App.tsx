import React, { useState } from 'react';
import './App.css';

function App() {
  const [query, setQuery] = useState('');
  const [response, setResponse] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleQuery = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!query.trim()) return;

    setIsLoading(true);
    
    try {
      // In a real implementation, this would call the backend API
      // For now we're simulating the response
      await new Promise(resolve => setTimeout(resolve, 1000));
      
      setResponse(`This is a simulated response to your query: "${query}"`);
    } catch (error) {
      setResponse('Error processing query. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Repo Explainer</h1>
        <p>Ask questions about any code repository and get intelligent explanations</p>
      </header>
      
      <main className="App-main">
        <form onSubmit={handleQuery} className="query-form">
          <input
            type="text"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Ask a question about the repository..."
            className="query-input"
          />
          <button type="submit" disabled={isLoading} className="query-button">
            {isLoading ? 'Processing...' : 'Explain'}
          </button>
        </form>

        {response && (
          <div className="response-container">
            <h2>Response</h2>
            <p>{response}</p>
          </div>
        )}
      </main>
    </div>
  );
}

export default App;