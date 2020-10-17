import React from 'react';
//import logo from './logo.svg';
import './App.css';

function Helloworld() {
  return (
    <div id="hello">Hello World</div>
  )
} // UN COMPONENTE

// const App = () => <div>This is my component: <Helloworld/> </div>

// class App extends React.Component {
//   render() {
//     return <div>This is my component: <Helloworld/> </div>
//   }
// }

// MISMAS FORMAS DE HACER LOS MISMO

function App() {
  return (
    // <div className="App">
    //   <header className="App-header">
    //     <img src={logo} className="App-logo" alt="logo" />
    //     <p>
    //       Edit <code>src/App.js</code> and save to reload.
    //     </p>
    //     <a
    //       className="App-link"
    //       href="https://reactjs.org"
    //       target="_blank"
    //       rel="noopener noreferrer"
    //     >
    //       Learn React
    //     </a>
    //   </header>
    // </div>
    <div>This is my component: <Helloworld/></div>
  );
} // UN COMPONENTE

export default App;
