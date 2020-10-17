import React from 'react'; // Crear interfaces 
import ReactDOM from 'react-dom'; // crear interfaces específicamente para el navegador web
import './index.css'; // webpack
import App from './App';
//import * as serviceWorker from './serviceWorker'; // progressive webapp - aplicaciones que hacen que se comporten como aplicaciones móviles nativas; ejecutar la app offline (después de la ejecución/descarga de la app por primera vez)

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA

//serviceWorker.unregister();
