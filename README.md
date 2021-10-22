# probe-acis-weather-data
Probes the ACIS weather archive

![acis](https://user-images.githubusercontent.com/39776793/138525358-4a464343-93bf-46f7-8728-c474ed270fc8.png)

The Applied Climate Information System (ACIS) stores weather data for a variety of weather stations. To access the raw data, you must communicate with the database via web API.  
This code handles the web API communication and can download raw data from any weather station with an associated stationID of any type listed in the below table.

<img src="https://user-images.githubusercontent.com/39776793/138525373-6b6faa83-68cd-41c4-b502-09de0a99e1ac.PNG" width="400">

For example, Boulder Municipal Airport in Boulder, CO has a FAA type station ID of BDU.
To extract the temperatures from BDU from 12 to 18 of October 2021, you would run
```python
import probe-acis-weather-data as pawd
temp_lo, temp_hi, temp_avg, metadata = pawd.getTemps(stationID="BDU 3", startdate="2021-10-12", enddate="2021-10-18")
```
