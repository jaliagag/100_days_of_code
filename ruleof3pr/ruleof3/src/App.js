import './App.css';

const ruleOf3 = (num1, num2) => alert("Free % memory",(num2*100)/num1)

function App() {
  constructor(props){
    super(props);
    this.state = {value: ''};
    
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event){
    this.setState({value:event.target.value});
  }
  
  handleSubmit(event){
    alert(this.state.value);
    event.preventDefault();
  }

  return (
    <>
      <form onSubmit={this.handleSubmit}>
        <p>Total Memory: 
	  <input
	    type="number"
	    id="total"
	    placeholder="total MB - e.g. 4000"
	    value={this.state.value}
	  />
	</p>
	<p>Free Memory: 
	  <input
	    type="number"
	    id="free"
	    placeholder="total MB - e.g. 238"
	    value={this.state.value}
	    onChange={this.handleChange}
	  />
	</p>
	<button id="calc">Calc</button>
      </form>
    </>
  );
}

export default App;
