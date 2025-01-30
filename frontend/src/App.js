import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [inputs, setInputs] = useState({
    "Nitrogen in kg/ha": '',
    "Phosphorus in kg/ha": '',
    "Potassium in kg/ha": '',
    "temperature in C": '',
    humidity: '',
    ph: '',
    "rainfall in mm": ''
  });

  const [crop, setCrop] = useState('');

  const handleChange = (e) => {
    setInputs({
      ...inputs,
      [e.target.name]: e.target.value
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    axios.post('http://localhost:5000/predict', inputs, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(response => {
      setCrop(response.data.crop);
    })
    .catch(error => {
      console.error('There was an error!', error);
    });
  };

  return (
    <div className="App">
      <h1>Crop Suggestion</h1>
      <form onSubmit={handleSubmit}>
        {Object.keys(inputs).map((key) => (
          <div key={key}>
            <label>{key}</label>
            <input type="text" name={key} value={inputs[key]} onChange={handleChange} />
          </div>
        ))}
        <button type="submit">Submit</button>
      </form>
      {crop && <h2>Suggested Crop: {crop}</h2>}
    </div>
  );
}

export default App;
