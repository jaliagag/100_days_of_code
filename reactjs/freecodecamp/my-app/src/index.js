import React from 'react';
import ReactDom from 'react-dom';

// capitalize the first letter of a function to indicate React that it's a component!

function Greeting(){
  return(
    <h4>Hello world!</h4>
  )
}

// looking for what we are going to render, Greeting, and where to render it, the html

ReactDom.render(<Greeting />, document.getElementById('root'));

// 1:04:11