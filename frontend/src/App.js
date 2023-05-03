import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react'

import Camera from './Camera/Camera';
import Light from './Light/Light';
import Graph from './Graph/Graph';
import Param from './Param/Param';
import Temperature from './Temperature/Temperature';

import Backend from './Backend.js';

const NAME = 'victorsplant';

function App() {

  const [samples, setSamples] = useState([]);

  const setDateAndTime = () => {
    let now = new Date().toISOString().split('T');
    let date = now[0];
    let time = now[1].split(':')[0] + ':' + now[1].split(':')[1];
    setTime(time);
    setDate(date);
  };

  const updateSamples = () => {
    Backend.fetch_samples(res => {
      if (res.result == 'ok') {
        setSamples([...samples, res.data]);
        console.log(samples);
      }
    });
  }

  useEffect(() => {
    updateSamples();
    setDateAndTime();
    setInterval(setDateAndTime, 1000)
  }, []);

  const [time, setTime] = useState('');
  const [date, setDate] = useState('');

  return (
    <div className="App">

      <nav className="navbar mb-5">
        <a className="navbar-brand ms-5 mt-2" href="/">{ NAME }</a>
      </nav>

      <div className="container-fluid">

        <div className="row">

          <div className="col-6">
            <div className="row mb-3">
              <h4>{date} {time}</h4>
            </div>

            <div className="row">
              <div className="col-6">
                <Param name="Temperature" value={23.4} unit={"C"} />
                <Param name="Moisture" value={23.4} unit={"%"} />
              </div>
              <div className="col-6">
                <img className='rounded w-50' src="/plant.jpg"></img>
              </div>
            </div>

            <div className="row mt-5">
              <div className="graph-container w-100">
                <Graph />
              </div>
            </div>

            <div className="row mt-5">
              <div className="graph-container w-100">
                <Graph samples={ samples }/>
              </div>
            </div>

          </div>

          <div className="col-6">
            <div className="img-fluid">
              <img src="/plant.jpg"></img>
            </div>
          </div>

        </div>

      </div>


    </div>

  );
}

export default App;
