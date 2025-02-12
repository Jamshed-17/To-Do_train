import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import Title from './Title';
import Input from './Input'
import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Title />
    <Input />
  </React.StrictMode>
);

reportWebVitals();
