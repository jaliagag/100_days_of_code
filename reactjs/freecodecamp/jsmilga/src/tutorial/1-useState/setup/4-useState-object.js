import React, { useState } from 'react';


const UseStateObject = () => {
  const [person, setPerson] = useState({name:'joe', age:31, message: 'random message'});


  const changeMessage = () => {
    let mensajito = person.message;
    if (mensajito === 'random message') {
      setPerson({ ...person, message: 'hello world' });
    } else {
      setPerson({ ...person, message: 'random message'});
    }
  };
  return (
    <>
      <h3>{person.name}</h3>
      <h3>{person.age}</h3>
      <h3>{person.message}</h3>
      <button className='btn' onClick={changeMessage}>change message</button>
    </>);
};

export default UseStateObject;
