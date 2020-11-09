import React from "react";
import ReactDom from "react-dom";
import './index.css';

// capitalize the first letter of a function to indicate React that it's a component!
//

const firstBook = {
  img: 'https://images-na.ssl-images-amazon.com/images/I/31vRcR-gi3L._SX248_BO1,204,203,200_.jpg'
  ,title:'Seveneves'
  ,author: 'Neal Stephenson'
}

const secondBook = {
  img: 'https://images-na.ssl-images-amazon.com/images/I/41ti7jItpeL._SX329_BO1,204,203,200_.jpg'
  ,title:'Dune'
  ,author: 'Frank Herbert'
}

function BookList() {
	// to render a component, it must be capitalized
	return (
	  <>
	    <section className='booklist'>
	      <Book img={firstBook.img} title={firstBook.title} author={firstBook.author}/>
	      <Book img={secondBook.img} title={secondBook.title} author={secondBook.author} />
	    </section>
	  </>
	);
} // Greeting would be our root component

//const Person = () => {
//	return <h2>Jogn Doe</h2>;
//};
//const Message = () => <p>This is a message</p>;

const Book = (props) => {
  const {img, title, author} = props
  return (
    <article className='book'>
      <img src={img} alt='' />
      <h1>{title}</h1>
      <h4>{props.author}</h4>
    </article>
  )
}

// different ways of accessing props
// 
// 1) props.img
// 2) define the values that will be included in the props in a constant and call it
// 	const {img} = props
// 	return <img src={img} alt=''/>
// 3) 


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
// #####################
// convention: use props; and it is an object; 
// 2:27:34
//
//
//
//
