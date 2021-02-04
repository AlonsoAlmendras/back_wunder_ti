import './App.css';
import React, { useState } from 'react';
import axios from 'axios';

const App = () => {
  const [encuestas, setEncuestas] = useState([]);

  const getDatos = () => {
    axios
      .get('http://localhost:8000/encuesta/getencuesta', {
        withCredentials: true,
      })
      .then((resp) => {
        console.log('el sistema respondio con:', resp);
        setEncuestas(resp.data.encuestas);
      })
      .catch((err) => console.log('sucedio un error, este es:', err));
  };

  return (
    <div className='App'>
      <header className='App-header'>
        <a
          className='App-link'
          href='http://localhost:8000/accounts/logout'
          rel='noopener noreferrer'
        >
          Log out
        </a>
        <button onClick={getDatos}>Ver encuestas</button>
        <p> existen {encuestas.length} encuestas</p>
        {encuestas.map((x) => (
          <p>
            nombre: {x.nombre_encuesta} texto:{x.texto_encuesta}
          </p>
        ))}
        <p></p>
      </header>
    </div>
  );
};

export default App;
