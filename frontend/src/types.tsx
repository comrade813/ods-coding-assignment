type Flights = Array<Array<string>>;

type Airport = {
    "value": string,
    "label": string
}

type Airports = Array<Airport>

export type {
    Flights,
    Airports
};