import React from 'react'

const Book = (props) => {
  // attribute, eventHandler
  // onClick, onMouseOver
  // https://es.reactjs.org/docs/events.html
  const {img, title, author} = props.book;

  const clickHandler = () => {
    alert('heelo world');
  }
  const complexExample = (author) => {
    console.log(author);
  }

  return (
    <article className='book' onMouseOver={()=> {
      console.log(title)
    } }>
      <img src={img} alt='' />
      <h1 onClick={()=>console.log(title)}>{title}</h1>
      <h4>{author}</h4>
      {props.children}
      <button type="button" onClick={clickHandler}>Reference Example</button>
      <button type="button" onClick={() => complexExample(author)}>More complex example </button>
    </article>
  )
}

export default Book

// only can be one default
