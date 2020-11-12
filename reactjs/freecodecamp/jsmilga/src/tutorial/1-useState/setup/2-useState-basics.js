import React, { useState } from 'react';
// useState is a function that comes from react - it is NAMED import, it needs to be imported between curly braces.
// useState returns an array, first a VALUE, then a HANDLER; the handler is the function that controls the value that we have in our state
// RELATED TO ALL OTHER HOOKS: 
// they start with use; 
// the component name MUST be uppercase; 
// they must be in the function/component body; 
// cannot call conditionally;

const UseStateBasics = () => {
  //console.log(useState('Hello World!'));
  //const value = useState(1)[0];
  //const handler = useState(1)[1]
  //console.log(value, handler);
  const [text, setText] = useState('random title')
  // text, setText is a convention
  const handleClick = () => {
    if (text === 'random title'){
      setText('hello world!');
    } else {
      setText('random title');
    }
  }

  return(
    <React.Fragment>
      <h1>{text}</h1>
      <button className='btn' onClick={handleClick}>change title</button>
    </React.Fragment>
  )
};

export default UseStateBasics;
