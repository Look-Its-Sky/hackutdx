import React, { useEffect, useState } from 'react';
import logo from './logo.svg';
import './App.css';

const HOST = 'localhost'
const PORT = 8000;

function App() {
  const [data, setData] = useState(null);    

  useEffect(() => {
    fetch(`http://${HOST}:${PORT}`)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Network response was not ok\nresponse : ${response}`);
        }
        return response.json();
      })
      .then(data => setData(data))
      .catch(error => console.error('Error:', error));
    }, []);
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        {data && (
          <div>
            <h2>
              API Test:{"\n"} 
              <pre>{JSON.stringify(data)}</pre>
            </h2>
          </div>
        )}
      </header>
    </div>
  );
}

export default App;
