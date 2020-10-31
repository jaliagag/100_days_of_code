//import React from 'react'; // en las últimas versiones capaz que ya no haga falta

function Welcome(props) {
  console.log(props);
  return(
    <>
      <p>{props.texto}</p>
    </>
  )
}

export default Welcome;
