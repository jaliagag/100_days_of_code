# ReactJS

## Fatz Tech

<https://www.youtube.com/watch?v=zIY87vU33aA&t=2s>

Js library - diseñar interfaces de usuario, elementos en pantalla - y poder reutilizarlos

Usa el Virtual Dom -- hace que sea más rápida la interfaz.

- Vista declarativas - declarative views
- virtual DOWM
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

1:16:18

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
