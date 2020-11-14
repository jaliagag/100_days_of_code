import React, { useState } from 'react';

const UseStateCounter = () => {
  const [value, setValue] = useState(0);
  const reset = () => {
    setValue(0)
    // we are just using this as an example - we could have simply 
    // added as an inline function, as the rest of the functions
  }
  const complexIncrease = () => {
    setTimeout(()=> {
      //setValue( value + 1 )
      // it's asyncronous; if we click 3 times, the value is still 0, the old value - to avoid that:
      setValue((prevState)=>{
	return prevState + 1;
      })
    },2000)
  }

  // example from 3-useState array using functional aproach
  // const removeItem = (id) => {
  // 	setPeople((oldPeople) => {
  // 		let newPeople = oldPeople.filter((person) => person.id !== id);
  // 		return newPeople;
  // 	});
  // };
  //
  // we can either pass in the value, say setValue(0), or we can use the 
  // functional approach were we pass in a function to the set<name> function,
  // as in setValue(()=> {}) and then make the parameter the previous state before
  // the update and we can set the functionality and the return will be the new 
  // state value

  return (
    <>
      <section style={{margin: '4rem 0'}}>
	<h2>regular counter</h2>
	<h1>{value}</h1>
	<button className='btn' onClick={()=> setValue (value -1)}>decrease</button>
	<button className='btn' onClick={reset}>reset</button>
	<button className='btn' onClick={()=> setValue (value +1)}>increase</button>
      </section>
      <section style={{margin: '4rem 0'}}>
	<h2>more complex counter</h2>
	<h1>{value}</h1>
	<button className='btn' onClick={complexIncrease}>increase later</button>
      </section>
    </>
  );
};

export default UseStateCounter;
