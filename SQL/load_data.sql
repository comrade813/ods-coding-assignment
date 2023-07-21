COPY flight_data.flights(id, 
			 created_at, 
			 updated_at, 
			 flight_identifier, 
			 flt_num, 
			 scheduled_origin_gate, 
			 scheduled_destination_gate, 
			 out_gmt, 
			 in_gmt, 
			 off_gmt, 
			 on_gmt, 
			 destination, 
			 origin, 
			 destination_full_name, 
			 origin_full_name)
FROM '/Users/kevinzheng/coding/ods/data/flights.csv'
DELIMITER ','
CSV HEADER;