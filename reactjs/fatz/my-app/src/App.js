import React from 'react';
//import logo from './logo.svg';
import './App.css';

// function Helloworld(props) {
//   return (
//     <div id="hello">
//       <h3>{props.subtitle}</h3>
//       {props.mytext}
//     </div>
//   )
// } // UN COMPONENTE

// const App = () => <div>This is my component: <Helloworld/> </div>

// class App extends React.Component {
//   render() {
//     return <div>This is my component: <Helloworld/> </div>
//   }
// }

// MISMAS FORMAS DE HACER LOS MISMO

class Helloworld extends React.Component {

  state = {
    show: true
  }

  toggleShow = () => {
    this.setState({show: !this.state.show})
  }

  render() {
    if (this.state.show) {
      return (
        <div id="hello">
          <h3>{this.props.subtitle}</h3>
          {this.props.mytext}
          {/* <button onClick={this.toggleShow.bind(this)}>Cambiar estado</button> */}
          <button onClick={this.toggleShow}>Cambiar estado</button>
          {/* onClick es un evento*/}
        </div>
      )
    } else {
      return <h1>
          No hay elementos
          <button onClick={this.toggleShow}> Cambiar de nuevo de estado</button>
        </h1>
    }
  }
}

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
    <div>
      This is my component: 
      <Helloworld mytext="wharup men" subtitle="lorem ipsum"/> 
      <Helloworld mytext="holis"/> 
      <Helloworld mytext="holisss"/>
    </div>
  );
} // UN COMPONENTE

export default App;
