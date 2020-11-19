// https://es.reactjs.org/docs/forms.html
// https://es.reactjs.org/docs/uncontrolled-components.html
// https://medium.com/better-programming/the-complete-guide-to-forms-in-react-d2ba93f32825
// https://scotch.io/courses/10-react-challenges-beginner/adding-calculator <<-- THE POST
import React, { useState } from 'react';
import ReactDOM from 'react-dom'
import './App.css';

function App() {
  const [number1, setNumber1] = useState(0);
  const [number2, setNumber2] = useState(0);
  const [total, setTotal] = useState((number2*100)/number1)
//  const [total, setTotal] = useState(number1 + number2)

  const ruleOf3 = () => setTotal((number2*100)/number1)
  return (
    <>
      <div className="boxes">
        <p>Total Server Memory (in MB): 
	  <input
	    type="number"
	    id="total"
	    value={number1}
	    onChange= {e => setNumber1(+e.target.value)}
	  />
	</p>
	<p>Free Memory (in MB): 
	  <input
	    type="number"
	    id="free"
	    value={number2}
	    onChange= {e => setNumber2(+e.target.value)}
	  />
	</p>
      </div>
      <div className="outputs">
	<button onClick={ruleOf3} id="calc">Calc</button>
	<h1 id="tatales">Free memory: {total.toFixed(2)}%</h1>
      </div>
    </>
  );
}

export default App;
