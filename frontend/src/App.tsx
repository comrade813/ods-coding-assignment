import React, { useEffect, useState } from 'react';
import './App.css';
import SearchBar from './searchbar';
import { Flights, Airports } from './types';
import { request } from './request';
import { AxiosError, AxiosResponse } from 'axios';
import Table from './table';

function App() {
  const [airports, setAirports] = useState<Airports>([]);
  const [flights, setFlights] = useState<Flights | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    request("airports", (response) => {
      console.log(response)
      setAirports(response.data);
    }, () => {})
  }, []);

  const onResultsLoaded = (response: AxiosResponse<any,any>) => {
    setError(null);
    setFlights(response.data);
  }

  const onRequestFailed = (error: AxiosError) => {
    console.log(error.response?.data)
    if(error.response?.data) {
      setError(String(error.response?.data))
    } else {
      setError("Something went wrong")
    }
  }

  const onClear = () => {
    setFlights(null);
  }

  return (
    <div className="App">
      <div className={flights == null ? "header" : "header-small"}>
        <div className="title">Flight Search</div>
        <SearchBar airports={airports} 
                   onResultsLoaded={onResultsLoaded}
                   onRequestFailed={onRequestFailed} />
        {error != null && <div className="error"> {error} </div>}
      </div>
      { flights != null &&
        <div className="results">
          <button className="clear" onClick={onClear}> Clear Results </button>
          {flights.length > 0 && <Table data={flights} />}
          {flights.length === 0 && <div> No flights to show. </div>}
        </div>
      }
    </div>
  );
}

export default App;
