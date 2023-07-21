import React, { useRef } from "react";
import Dropdown from "./dropdown";
import { Airports } from "./types";
import './searchbar.css';
import { request } from "./request";
import { AxiosError, AxiosResponse } from "axios";

interface SearchBarProps {
    airports: Airports,
    onResultsLoaded: (response: AxiosResponse<any,any>) => void;
    onRequestFailed: (error: AxiosError) => void;
}

function SearchBar(props: SearchBarProps) {
    const origin = useRef<any>(null)
    const destination = useRef<any>(null);

    const onClick = () => {
        let from: string = "ANY";
        if(origin.current.getValue().length > 0) {
            from = origin.current.getValue()[0].value
        }
        let to: string = "ANY";
        if(destination.current.getValue().length > 0) {
            to = destination.current.getValue()[0].value
        }
        request(`${from}/${to}`, props.onResultsLoaded, props.onRequestFailed)
    }

    return (
        <div className="searchbar">
            <Dropdown options={props.airports} val={origin}/>
            <div className="to">to</div>
            <Dropdown options={props.airports} val={destination}/>
            <div className="break" />
            <button className="searchButton" onClick={onClick}>Search</button>
        </div>
    );
}

export default SearchBar;