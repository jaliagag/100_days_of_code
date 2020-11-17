import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';

function Saludo(){
  return <section> 
      <App />
    </section>

}

ReactDOM.render(<Saludo />, document.getElementById('root'));

