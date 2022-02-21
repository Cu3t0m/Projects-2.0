import logo from './logo.svg';
import './App.css';

function App() {
  return (
    <>
    <div className="App">
      <div className='App-body'>
        <h1>Welcome to my website!</h1>
        <p>This website is written in React, which was made to be a testament to what I've learnt</p>
      </div>
      <div className='App-footer'>
        <img src={logo} className="App-logo" alt="logo" />
      </div>
    </div>
    </>
  );
}

export default App;