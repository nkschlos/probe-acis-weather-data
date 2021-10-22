"""
Queries the ACIS database for weather information.

For example, to get the temperature at Boulder Municipal Airport (FAA code BDU) from 12 to 18 October 2021, you would run

temp_lo, temp_hi, temp_avg, metadata = getTemps(stationID="BDU 3", startdate="2021-10-12", enddate="2021-10-18")

"""
import urllib
import requests
import json

def getTemps(stationID, startdate, enddate):
    """Query the daily low, high, and average temperature from a single station over a range of dates

    Keyword arguments:
    stationID: (string) the sid of the station you wish to get data from. Formatted as:
                <stationID> <stationID type code>
                separated by a space. The type codes are listed in Table 1. at https://www.rcc-acis.org/docs_webservices.html
    startdate: (string) the beginning of the date range over which to acquire data, Formatted as:
                YYYY-MM-DD
    enddate: (string) the end of the date range over which to acquire data, Formatted as:
                YYYY-MM-DD

    Returns:
    temp_lo: (list of float) The low temperature of each day in degrees F
    temp_hi: (list of float) The high temperature of each day in degrees F
    temp_avg: (list of float) The average temperature of each day in degrees F
    response_meta: (dict) The metadata associated with the data supplied by the server
    """
    params = {
                "sids": stationID,
                "sdate": startdate,
                "edate": enddate,
                "elems": ["mint", "maxt", "avgt"]
              }
    response = queryData(params)
    try:
        # Parse the response
        response = response['data']
        response_data = [entry['data'] for entry in response][0]
        temp_lo = [float(entry[0]) for entry in response_data]
        temp_hi = [float(entry[1]) for entry in response_data]
        temp_avg = [float(entry[2]) for entry in response_data]
        response_meta = [entry['meta'] for entry in response][0]
    except:
        raise("Error interpreting results")
    return temp_lo, temp_hi, temp_avg, response_meta

def queryData(params):
    params = urllib.parse.urlencode({'params': json.dumps(params)})
    params = params.encode('utf-8')
    req = urllib.request.Request('http://data.rcc-acis.org/MultiStnData',params,{'Accept': 'application/json'})
    response = urllib.request.urlopen(req)
    return json.loads(response.read())
