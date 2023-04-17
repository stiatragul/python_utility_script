### Fetch historical data from OpenWeatherMap API
https://openweathermap.org/api

What it does:
  - Fetches climate data for a particular datetime in the past (up to 1 January 1970). 
  - Returns temperature, humidity, air pressure, cloud cover and windspeed data. But other data can be returned by changing the code. 
  - Takes datetime (as UNIX time) and coordinates as csv file as input.
  - Outputs the same file with additional columns. 

Who is it for:
  - For anyone who wants to know what the climate at a particular location was like in the past.

___

#### Example

Input CSV:
```
latitude	  longitude	  date
-35.2646769	149.0628611	16/04/2023
-35.2646769	149.0628611	16/04/2023
-33.2646769	149.0628611	15/04/2023
-36.2646769	149.0628611	13/04/2023
````

output csv:
```
latitude	  longitude	  date	      timestamp	  dt	        temp	  humidity	pressure	clouds	wind_speed	date_time
-35.2646769	149.0628611	16/04/2023	1681603200	1681603200	12.36	  92	      1004	    100	    9.77	      16/04/2023 10:00
-35.2646769	149.0628611	16/04/2023	1681603200	1681603200	12.36	  92	      1004	    100	    9.77	      16/04/2023 10:00
-33.2646769	149.0628611	15/04/2023	1681516800	1681516800	17.46	  68	      1014	    37	    3.75	      15/04/2023 10:00
-36.2646769	149.0628611	13/04/2023	1681344000	1681344000	9.5	    91	      1013	    100	    3.61	      13/04/2023 10:00
```

