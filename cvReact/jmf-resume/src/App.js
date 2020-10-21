import React, { Component } from 'react';
import './App.css'
import profilePic from './assets/profile_pic.PNG'

function App() {
  return (
    <body>
      <div className="bordeTestDelete" id="header">
        <container id="contenedorCabe">
          <img src={ profilePic } alt="Profile Pic" id="profilePic" />
          <h1 className="name">José Manuel Francisco Aliaga</h1>
        </container>
      </div>
    </body>
  );
}

export default App;
