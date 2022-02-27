import { useState } from 'react'
import logo from './logo.svg'
import './App.css'

function App() {
  const [count, setCount] = useState(0)

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>Hello Vite + React!</p>
        <p>
          <div className="horizontal-box">
            <button type="button" onClick={() => setCount((count) => count + 1)}>+</button>
            <p>Count is {count}</p>
            <button type="button" onClick={() => setCount((count) => count - 1)}>-</button>
          </div>
        </p>
      </header>
    </div>
  )
}

export default App
