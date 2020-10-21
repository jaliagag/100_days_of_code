import React, { Component } from 'react';


// crear nuestro componente, nuestro formulario
export default class TaskForm extends Component {

    state = {
        title: ''
        ,description: ''
    }

    onSubmit = e => {
        //console.log('enviando')
        this.props.addTask(this.state.title, this.state.description);
        //console.log(this.state)
        e.preventDefault();
    }

    onChange = e => {
        //console.log(e.target.name, e.target.value)
        //console.log(e.target.value)
        this.setState({
            [e.target.name]: e.target.value
        })
    }

  render() {
      return (
          <form onSubmit={ this.onSubmit }>
              <input 
              type="text"
              name="title" 
              placeholder="Escribe una tarea" 
              onChange={ this.onChange } 
              value={this.state.title} />
                <br />
                <br />
              <textarea 
              placeholder="escribe una descripcion" 
              name="description"
              onChange={ this.onChange } 
              value={ this.state.description } />
                <br /> 
              <input type="submit" />
          </form>
      )
  }
}

// el método render tiene que retornar algo

// export default TaskForm;
// same as above