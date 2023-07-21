SELECT_ALL_DESTINATION_AIRPORTS = """
    SELECT destination AS dest, destination_full_name as full
    FROM flight_data.flights 
"""

SELECT_ALL_ORIGIN_AIRPORTS = """
    SELECT origin AS origin, origin_full_name as full
    FROM flight_data.flights 
"""

INSERT_ALL_AIRPORTS = """
    INSERT INTO flight_data.airports (code, full_name)
    VALUES (%s, %s)
    ON CONFLICT (code)
    DO NOTHING
"""

SELECT_ALL_AIRPORTS = """
    SELECT *
    FROM flight_data.airports
"""
    
SELECT_FLIGHTS_TO_DESTINATION = """
    SELECT flight_identifier, flt_num, scheduled_origin_gate,
        scheduled_destination_gate, out_gmt, in_gmt, 
        off_gmt, on_gmt, destination, origin,
        destination_full_name, origin_full_name
    FROM flight_data.flights
    WHERE destination = %s
"""

SELECT_FLIGHTS_FROM_ORIGIN = """
    SELECT flight_identifier, flt_num, scheduled_origin_gate,
        scheduled_destination_gate, out_gmt, in_gmt, 
        off_gmt, on_gmt, destination, origin,
        destination_full_name, origin_full_name
    FROM flight_data.flights
    WHERE origin = %s
"""

SELECT_FLIGHTS_FROM_ORIGIN_TO_DESTINATION = """
    SELECT flight_identifier, flt_num, scheduled_origin_gate,
        scheduled_destination_gate, out_gmt, in_gmt, 
        off_gmt, on_gmt, destination, origin,
        destination_full_name, origin_full_name
    FROM flight_data.flights
    WHERE origin = %s
    AND destination = %s
"""