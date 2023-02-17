import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react'

import Camera from './Camera/Camera';
import Light from './Light/Light';
import Temperature from './Temperature/Temperature';

const NAME = 'Office Plant';

function App() {

  const setDateAndTime = () => {
    let now = new Date().toISOString().split('T');
    let date = now[0];
    let time = now[1].split(':')[0] + ':' + now[1].split(':')[1];
    setTime(time);
    setDate(date);
  };

  useEffect(() => {
    setDateAndTime();
    setInterval(setDateAndTime, 1000)
  }, [])

  const [time, setTime] = useState('');
  const [date, setDate] = useState('');

  return (
    <div className="App">
      <div>
        <h1>{ NAME }</h1>
        <h4>{ time }</h4>
        <h4>{ date }</h4>
      </div>

      <div className="row m-5">
        <div className="col-6">
          <Temperature />
        </div>
        <div className="col-6">
          <Light />
        </div>
      </div>

      <div className="row">
        <div className="col-12">
          <Camera />
        </div>
      </div>

    </div>
  );
}

export default App;
