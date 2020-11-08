import React from "react";
import ReactDom from "react-dom";
import './index.css';

// capitalize the first letter of a function to indicate React that it's a component!

function BookList() {
	// to render a component, it must be capitalized
	return (
	  <>
	    <section className='booklist'>
	      <Book />
	    </section>
	  </>
	);
} // Greeting would be our root component

//const Person = () => {
//	return <h2>Jogn Doe</h2>;
//};
//const Message = () => <p>This is a message</p>;

const Book = () => {
  const title = 'Seveneves'
  const author = 'Neal Stephenson'
  return (
    <article className='book'>
      <Image />
      <h1>{title}</h1>
      <h4 style={{color:'·617d98', fontSize:'0.75rem', marginTop:'0.25rem'}}>{author.toUpperCase()}</h4>
    <p>{6+6}</p>
    </article>
  )
}

const Image = () => (
  <img src='https://images-na.ssl-images-amazon.com/images/I/31vRcR-gi3L._SX248_BO1,204,203,200_.jpg' alt='' />
)

//const Title = () => <h1>Seveneves</h1>
//  const Author = () => <h4 style={{color:'·617d98', fontSize:'0.75rem', marginTop:'0.25rem'}}>Neal Stephenson</h4>
  // to access JSscript world from JSX, use {} - it has to be set up as an object - that's why we use double courly brackets.
  // values have to be marked between ''/"".
  // Values added in line step over values added on the CSS file

// looking for what we are going to render, Greeting, and where to render it, the html

ReactDom.render(<BookList />, document.getElementById("root"));


// function Greeting() --> stateless functional component or dumb components.
// Always needs to return JSX.
// JSX rules: we always have to return a SINGLE element
// div / section / article or fragment
// FRAGMENT: use <> ... </> = React.Fragment
// use camelCase for html attribute
// className instead of class
// close every element
// formatting
// #####################
// NESTED COMPONENTS
// 2:10:21 --> starting with props
//
//
//
//
//
//
//
