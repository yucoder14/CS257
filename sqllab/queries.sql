
--find all the earthquakes that occurred in the Japan region 
SELECT * FROM earthquakes WHERE latitude BETWEEN 20 AND 45 AND longitude BETWEEN 122 AND 153 ORDER BY mag DESC;

--find top 10 strongest earthquakes that occurred in the Western Hemisphere
SELECT * FROM earthquakes WHERE mag > 5 AND longitude BETWEEN 0 AND 180 ORDER BY mag DESC LIMIT 10;

--find earthquakes that occurred in New Year's EVE 
SELECT * FROM earthquakes WHERE EXTRACT(YEAR FROM quakedate) = 2022 AND EXTRACT(MONTH FROM quakedate) = 12 AND EXTRACT(DAY FROM quakedate) = 31 ORDER BY mag DESC;
