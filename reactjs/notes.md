# ReactJS

<https://www.youtube.com/watch?v=zIY87vU33aA&t=2s>

Js library - diseñar interfaces de usuario, elementos en pantalla - y poder reutilizarlos

Usa el Virtual Dom -- hace que sea más rápida la interfaz.

- Vista declarativas - declarative views
- virtual DOWM
- components: pequeñas etiquetas html que se pueden reutilizar
- server side rendering: enviar la interfaz a medida que se vaya pidiendo

## COMPONENTES

dividir una aplicación grande en pequeñas parets - componenetes; encapsulan código. Los componentes se ven como etiquetas html

Encapsula el código HTML, CSS y JS.

8:20

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
