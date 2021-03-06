/*
Wheater Observation Station 10

Query the list of CITY names from STATION that do not end with vowels. Your result cannot contain duplicates.
The STATION table is described as follows:
           STATION
+-------------+--------------+
| Field       | Type         |
+-------------+--------------+
| ID          | NUMBER       |
| CITY        | VARCHAR2(21) |
| STATE       | VARCHAR2(2)  |
| LAT_N       | NUMBER       |
| LONG_W      | NUMBER       |
+-------------+--------------+

where LAT_N is the northern latitude and LONG_W is the western longitude.
*/
SELECT DISTINCT CITY
FROM STATION
WHERE CITY REGEXP '[^aeiouAEIOU]$'
ORDER BY CITY;
--------------------------------------------------------------------------------
SELECT DISTINCT CITY 
FROM STATION 
WHERE UPPER(SUBSTR(CITY, LENGTH(CITY), 1)) NOT IN ('A','E','I','O','U') 
AND LOWER(SUBSTR(CITY, LENGTH(CITY),1)) NOT IN ('a','e','i','o','u');