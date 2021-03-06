# ReactJS

## Fatz Tech

<https://www.youtube.com/watch?v=zIY87vU33aA&t=2s>

Js library - diseñar interfaces de usuario, elementos en pantalla - y poder reutilizarlos

Usa el Virtual Dom -- hace que sea más rápida la interfaz.

- Vista declarativas - declarative views
- virtual DOM
- components: pequeñas etiquetas html que se pueden reutilizar
- server side rendering: enviar la interfaz a medida que se vaya pidiendo

### COMPONENTES

dividir una aplicación grande en pequeñas parets - componenetes; encapsulan código. Los componentes se ven como etiquetas html

Encapsula el código HTML, CSS y JS.

- React Native: hacer que funcione en android/iOs
- next.js: framework de server-side rendering;
- graphQL: lenguaje para solicitar datos y especificar qué necesitas y qué necesitas enviar; para mantener el código y las consultas que se hacen desde el servidor
- redux: manejador de estados de la app; mejora el mantenimiento del código de react
- MERN: stack, define muchas tecnologías (mongo express react node) -- app entera con js
- ionic4: relacionado con angular (y vue) - app movil

<https://reactjs.org>

```js
npx create-react-app my-app
cd my-app
npm start // inicia y crea el servidor en desarrollo
npm run build // convertir el código de desarrollo en código de producción - convierte código en JS
npm test // ejecutar archivos de intermedio
npm run eject
npm run eject
```

No escribimos HTML - SOLO js

El código dentro de App.js que parece HTML es JSX, no HTML. En JSX usamos `className` en vez de `class`. Es JavaScript > babel repl

React usa babel que convierte código de react en código js puro.

| HTML | JS |
| ---- |---- |
| `<h1>hello world</h1>` | `React.createElement("h1", null, "hello world!");` |

Como esto es difícil de manetener, tenemos en react este código que parece HTML, que es JS, JSX.

```js
function Helloworld(props) {
  return (
    <div id="hello">
      <p>Hellow World</p>
    </div>
  )
}
// formas de crear un componente
// variable
const App = () => <div>This is my component: <Helloworld/> </div>

// clase
class App extends React.Component {
  render() {
    return <div>This is my component: <Helloworld/> </div>
  }
}
// función
function App() {
  return (
    <div>
      This is my component: <Helloworld />
    </div>
  );
}
```

### Props

Datos que le pasamos de afuera hacia dentro del componente.

```js
function Helloworld(props) {
  return (
    <div id="hello">
      <h3>{props.subtitle}</h3>
      {props.mytext}
    </div>
  )
}

function App() {
  return (
    <div>
      This is my component: 
      <Helloworld mytext="wharup men" subtitle="lorem ipsum"/> 
      <Helloworld mytext="holis" subtitle="otro subtítulo"/> 
      <Helloworld mytext="holisss"/>
    </div>
  );
}
```

### State

Datos internos de un componente. Cada vez que llamemos a Helloworld, cada componente tiene su propio estado y funciona de manera independiente.

```js
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
```

En React, cuando ponemos algo en de JSX dentro de `{}` esto le indica que es código JS.

```jsx
render() {
  return <div>
    { 5 + 5 }
  </div>
}
```

### Task App

Un componente solo puede retornar un elemento a la vez

#### Método MAP

`a.map((e) => e + 3)`. El método map _NO_ modifica el array.

### Styles

Objetos de JS para estilizar. Importar un css y listo; no usamos _class_, sino **CLASSNAME**. 

Para hacer un estilo inline, `style=({background: 'red'})` <-- objeto de JS para estilizar. Se pueden guardar en **variables**.

Cambiar estilos de manera dinámica; la idea de usar una función es para aplicar condicionales!

```js
,color: this.props.task.done ? 'gray': 'black'
// operador ternario - condicional en una sola línea
// si this.props.task.done es true (?) el color del texto es 'gray'. En caso contrario ':', que esté en negro 'black'
```

### PropTypes

Tipos de datos de las propiedades, de los props. Advertencias para cuando estoy codeando para facilitar el debug.

### Forms

Agregar información en un formulario que permita crear/pushear información.

```js
// importar la funcionalidad de recat y también la funcionalidad de los componentes que vienen  desde la biblioteca de react
import React, { Component } from 'react';

// crear una clase que represente un componente
// hereda los componentes la funcionalidad

export default class TaskForm extends Component {

    state = {
        title: ''
        ,description: ''
    }

    onSubmit = e => {
        //console.log('enviando')
        console.log(this.state)
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
```

### Passing Functions

Pasar una función de un archivo a otro, a través de un props. En el archivo principal de la aplicación  agrego al componente que llamo un props que después puedo usar en el componente mismo.

```js
// archivo principal de la aplicación
import React, { Component } from 'react';

export default class App extends Component {
  funcionCopada = () => {
    console.log('Esta es una función copada que va a pasar como props');
  }

  render(){
    return <div>
    <HolaMundo funcionCopada= { this.funcionCopada }/>
    </div>
  }
}

// componente - como le agregué un atributo (funcionCopada) cuando llamaba el componente
// ahora puedo usar ese atributo, que es una función, en el componente en sí

import React, { Component } from 'react';

export default class HolaMundo extends Component {
  render() {
    console.log(this.props) // debería mostrar {funcionCopada: f} por consola
    // para ejecutarla
    this.props.funcionCopada();
    // ejecuto DESDE EL COMPONENTE la función que está en el archivo principal
    return (
      <h1>Hola Mundo</h1>
    )
  }
}
```

### Eliminar y Actualizar

```js
// app.js
// agregamos 2 métodos

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

    // se los pasamos acá

    <Tasks tasks={ this.state.tasks } deleteTask= { this.deleteTask } checkDone={ this.checkDone } />

// Tasksssssssssss
// se lo agregamos a este componente para que existe en los subcomponentes
        return this.props.tasks.map(task => <Task 
            task={ task } 
            key={ task.id } 
            deleteTask={ this.props.deleteTask }
            checkDone={ this.props.checkDone } />)
// se lo pasamos a task

    render() {

        const {task} = this.props

        //const redColor = {background: 'red'}
        return   <p style={this.StyleCompleted()}>
            { task.title } - { task.description } - { task.done } - { task.id }
            <input type="checkbox" onChange={ this.props.checkDone.bind(this, task.id) } ></input>
            <button style={btnDelete} onClick={ this.props.deleteTask.bind(this, task.id) } >
                x
            </button>
        </p>          
    }

```

### Fetching Data

De servidores externos. Bucle for en JSX

```js
// desde el state/estado en sus publicaciones voy a empezar a recorrer cada uno
// con la función map
// por cada aplicación que recorre, retorno un elemento JSX
this.state.posts.map(post => {
  return <div key={post.id}>
    <h1>Título: { post.title } </h1>
    <p>{ post.body} </p>
  </div>
```

### Enrutador de React

`npm install react-router-dom`

## Acamica

Renderizar datos en el DOM.

1. es declarativo - describos qué queremos que se muestre en la UI en vez de hacerlo de manera imperativa.
2. es JS, no hay que aprender nada
3. nuestras interfaces son árboles de componentes
4. UI de manera interactiva; cuando queremos actualizar, renderizamos toda la API de nuevo;

createElement('tipo de componente a renderizar', atributos del elemento, hijos del elemento que creamos)

en React, cuando estamos creando un elemento no solemos usar "class" como atributo, sino `className`. El atributo "style" es:

```js
React.createElement('h1', {style: {color: 'red'} }, 'Hellow World!');

React.createElement('a', {
  href: 'http://google.com',
  style: { backgroundColor: 'red' }
}, 'Link a Google');

// definir hijos

var personas = ['Juan', 'Maria', 'Laura', 'German'];
var app = React.createElement('ul', null,
  personas.map(function(persona) {
    return React.createElement('li', null, persona);
  })
);
ReactDOM.render(app, document.getElementById('content'));

// otra opción

var app = React.createElement('h1', { children: 'Este es un texto' });
ReactDOM.render(app, document.getElementById('content'));
```

Crear componentes; el segundo elemento de React.createElement se llama **props**. Los atributos que pasamos a los elementos no son solamente los atributos de HRML, sino parámetros para crear un elemento.

```js
var app = React.createElement('div', null,
  React.createElement('h1', null, 'Mi Sitio - Pagina 1'),
  React.createElement('ul', { className: 'menu' },
    React.createElement('li', null, 'Inicio'),
    React.createElement('li', null, 'Quienes Somos'),
    React.createElement('li', null, 'FAQ'),
  ),
  React.createElement('div', { className: 'contenido' },
    React.createElement('p', null, 'Mi contenido')
  )
); // << NO RECOMENDADO ???

function Encabezado(props) {
  return React.createElement(
    'h1', 
    null, 
    'Mi Sitio - ' + props.nombrePagina
  );
}

function Menu() {
  return React.createElement('ul', { className: 'menu' },
    React.createElement('li', null, 'Inicio'),
    React.createElement('li', null, 'Quienes Somos'),
    React.createElement('li', null, 'FAQ'),
  )
}

function Contenido(props) {
  return React.createElement(
    'div', 
    {className: 'contenido'}, 
    props.children
  );
}

var app = React.createElement('div', null,
  Encabezado({ nombrePagina: 'Pagina 1' }),
  Menu(),
  Contenido({ 
    children: React.createElement('p', null, 'Mi contenido') 
  })
);

var app = React.createElement('div', null,
  React.createElement(Encabezado, { nombrePagina: 'Pagina 1'}),
  React.createElement(Menu),
  React.createElement(Contenido, null,
    React.createElement('p', null, 'Mi contenido')
  )
);
```

Definir funciones que reciben props como parámetro y devuelven elementos de REAct que describen cómo se va a renderizar ese componente

## FreeCodeCamp

<https://www.youtube.com/watch?v=4UZrsTqkcW4&t=1529s>

```js
npx create-react-app my-app
cd my-app
npm start
```

- Babel compiles new JS (ES6) into old JS (ES5).
- WebPack - module bundler - bundling resources

Reacts --> functions reacts provides to complete various tasks. If it starts with **use**, that's a hook.



## ReactJS BA

Un _framework_, entorno de trabajo o marco de trabajo es un conjunto estandarizado de conceptos, prácticas y criterios para enfocar un tipo de problemática particular que sirve como referencia para enfrentar y resolver nuevos problemas de índole similar.

React es una librería open source diseñada para crear interfaces de usuario con el objetivo de facilitar el desarrollo de SPAs(single page applications). Fue creado y es mantenido (principalmente) por Facebook.

Angujar es un Framework

SPA: app de página única es una app web que cabe en una sola página con el propósito de dar una experiencia más fluida a los usuario - un único HTML pero varias rutas, como si fuera en HTML distintos, pero en realidad es el mismo HTML pero enrutado con REACT.

En REACT todo lo que sea document.getElementById or document.querySelector --> NO VA MÁS.

Componentes: en react un componente es un bloque de código reutilizable que cumpla con las siguientes propiedades

- puede recibir propiedades inmutables
- puede mutar su estado interno (en caso de tenerlo)
- tiene la capacidad de representarse a si mismo en base a propiedades y su estado interno - básicamente cada componente debe poder pintarse en el HTML

Funciones vs clases

Antes solo se usaban clases. Desde los REACT Hooks, las funciones tienen más relevancia. Recomendado aprenderlo con funciones - si bien darle bola a las clases.

React fragment - solucina el problema del wrapper sin generar un nodo extra; <> </>. A la hora de transpilar el código, no se genera nada. **USE IT** - Es más rápido tener menos nodos (milisegundos - pero más mejor no agregar nodos innecesarios).

Los props se pasa como si fueran atributos de HTML. Entre los paréntesis del componente es donde recibe los props.

Cada tag que usamos cuando llamamos al componente es llamado una _INSTANCIA_.

Todo lo que está entre paréntesis lo considera como viniendo de JS.












