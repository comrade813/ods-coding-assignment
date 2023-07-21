-- Table: flight_data.flights

-- DROP TABLE IF EXISTS flight_data.flights;

CREATE TABLE IF NOT EXISTS flight_data.flights
(
    id integer NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    flight_identifier character(36) COLLATE pg_catalog."default" NOT NULL,
    flt_num integer NOT NULL,
    scheduled_origin_gate text COLLATE pg_catalog."default" NOT NULL,
    scheduled_destination_gate text COLLATE pg_catalog."default" NOT NULL,
    out_gmt timestamp with time zone NOT NULL,
    in_gmt timestamp with time zone NOT NULL,
    off_gmt timestamp with time zone NOT NULL,
    on_gmt timestamp with time zone NOT NULL,
    destination character(3) COLLATE pg_catalog."default" NOT NULL,
    origin character(3) COLLATE pg_catalog."default" NOT NULL,
    destination_full_name text COLLATE pg_catalog."default",
    origin_full_name text COLLATE pg_catalog."default",
    CONSTRAINT flights_pkey PRIMARY KEY (id),
    CONSTRAINT flights_flight_identifier_key UNIQUE (flight_identifier)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS flight_data.flights
    OWNER to postgres;