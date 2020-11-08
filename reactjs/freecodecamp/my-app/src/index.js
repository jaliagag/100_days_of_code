import React from "react";
import ReactDom from "react-dom";

// capitalize the first letter of a function to indicate React that it's a component!

function Greeting() {
	// to render a component, it must be capitalized
	return (
	  <>
	    <section>
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
  return <article>
    <Image />
  </article>
}

const Image = () => (
  <img src='https://images-na.ssl-images-amazon.com/images/I/31vRcR-gi3L._SX248_BO1,204,203,200_.jpg' alt='' />
)

const Author = () =>

// looking for what we are going to render, Greeting, and where to render it, the html

ReactDom.render(<Greeting />, document.getElementById("root"));


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
//
