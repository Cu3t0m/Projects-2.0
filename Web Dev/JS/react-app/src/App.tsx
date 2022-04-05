import React from 'react';
import { useState, FC } from 'react';
import './App.css';

interface Props {
  text: string
}

const Text: FC<Props> = (props) => {
  return (  <>
    <h1>{props.text}</h1> 
  </>
  )
}

const Counter: FC = () => {
  const [count, setCount] = useState(0);
  return (
    <>
      <button type='button' onClick={() => setCount((count) => count - 1)}>-</button>
      <p>Count is {count}</p>
      <button type='button' onClick={() => setCount((count) => count + 1)}>+</button>
    </>
  )
}

const App: FC = () => {
  return (
  <>
    <header className='App-header'>
      <Text text='Hello World!' />
      <Counter />
    </header>
  </>
  )
}

export default App;
