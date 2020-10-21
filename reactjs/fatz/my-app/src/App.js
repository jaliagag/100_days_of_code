import React, { Component} from 'react';
import './App.css';
import { BrowserRouter as Router, Route, Link } from 'react-router-dom';

// importar datos

import tasks from './sample/tasks.json'

// componentes
import Tasks from './components/Tasks'
import TaskForm from './components/TaskForm'
import Posts from './components/Posts'

// componente inicial

class App extends Component {

    state = {
        tasks: tasks
    }

    addTask = (title, description) => {
        //console.log(title, description)
        //alert("título: " + title)
        //alert("descripción: " + description)
        const newTask = {
            title: title
            ,description: description
            ,id: this.state.tasks.length
        }
        this.setState({
            tasks: [...this.state.tasks, newTask]
        })
    }

    deleteTask = id => {
        const newTasks = this.state.tasks.filter(task => task.id !== id);
        this.setState({ tasks: newTasks })
    }

    checkDone = id => {
        const newTasks = this.state.tasks.map(task => {
            if (task.id === id) {
                task.done = !task.done
            }
            return task
        })
        this.setState({ task: newTasks })
    }

    render() {
        return <div>
            <Router>
                <Link to="/tasks">Home</Link>
                <br />
                <Link to="/posts">Posts</Link>

                <Route path="/tasks" render= {() => {
                    return <div>
                        <TaskForm addTask={ this.addTask } />
                        <Tasks 
                            tasks={ this.state.tasks } 
                            deleteTask= { this.deleteTask } 
                            checkDone={ this.checkDone } 
                        />
                    </div>
                }} >
                </Route>
                <Route path="/posts" component={Posts} />
            </Router>

            {/* { this.state.tasks.map(e => <h1> { e.title } </h1>) } */}
            { /*this.state.tasks.map(e => <p key={ e.id }>
                { e.title } - { e.description } - { e.done } - { e.id }
                { <Tasks/> }
            </p>) */}
        </div>
    }
}

export default App;