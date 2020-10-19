import React, { Component} from 'react';
import './App.css';

// importar datos

import tasks from './sample/tasks.json'

import Tasks from './components/Tasks'

// componente inicial

class App extends Component {

    state = {
        tasks: tasks
    }

    render() {
        return <div>
            {/* { this.state.tasks.map(e => <h1> { e.title } </h1>) } */}
            { /*this.state.tasks.map(e => <p key={ e.id }>
                { e.title } - { e.description } - { e.done } - { e.id }
                { <Tasks/> }
            </p>) */}
            <Tasks tasks={this.state.tasks}/>
        </div>
    }
}

export default App;