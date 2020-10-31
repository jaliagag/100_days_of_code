import logo from './logo.svg';
import './App.css';
import Welcome from './components/Welcome'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Welcome texto="Soy el primer texto"/>
	<Welcome texto="Soy el segundo texto"/>
	<Welcome texto="Soy el tercer texto"/>
      </header>
    </div>
  );
}

export default App;
