#http://www.mapquestapi.com/geocoding/v1/address?key=KEY&location=Washington,DC


# Useful URLs (you need to add the appropriate parameters for your requests)
MAPQUEST_BASE_URL = "http://www.mapquestapi.com/geocoding/v1/address"
MBTA_BASE_URL = "https://api-v3.mbta.com/stops"

# Your API KEYS (you need to use your own keys - very long random characters)
MAPQUEST_API_KEY = "Rk4MrhuBVCdAfDlXg4LUJTRz5RuToDlf"
MBTA_API_KEY = "bd0e50fef16849b280f788a557e4ad31"


# A little bit of scaffolding if you want to use it
import urllib.request
import json
from pprint import pprint

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """
    f = urllib.request.urlopen(url)
    response_text = f.read().decode('utf-8')
    response_data = json.loads(response_text)
    return response_data

#print(get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'))


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.
    See https://developer.mapquest.com/documentation/geocoding-api/address/get/
    for Mapquest Geocoding  API URL formatting requirements.
    """
    datax=get_json(f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={place_name}')
    return datax["results"][0]["locations"][0]["latLng"]


#print(get_lat_long("boston"))

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, wheelchair_accessible)
    tuple for the nearest MBTA station to the given coordinates.
    See https://api-v3.mbta.com/docs/swagger/index.html#/Stop/ApiWeb_StopController_index for URL
    formatting requirements for the 'GET /stops' API.
    """
    mbta = get_json(f'{MBTA_BASE_URL}?api_key={MBTA_API_KEY}&filter[latitude]={latitude}&filter[longitude]={longitude}&sort=distance')
    return mbta["data"][0]["attributes"]["name"],mbta["data"][0]["attributes"]["wheelchair_boarding"]



#print(get_nearest_station(42.358894,-71.056742))


def find_stop_near(place_name):
    """
    Given a place name or address, return the nearest MBTA stop and whether it is wheelchair accessible.
    """
    stop_lat_long = get_lat_long(place_name)
    latitude = stop_lat_long.get("lat")
    longitude= stop_lat_long.get("lng")
    return get_nearest_station(latitude,longitude)

#print(find_stop_near("boston"))




def main():
    """
    You can test all the functions here
    """
    a = str(input('please enter place in boston:'))
    sol_1, sol_2 = find_stop_near(a)
    if sol_1:
        print(f'the closest t-station is: {sol_1} and the wheelchair accessability is: {sol_2}.')
    else:
        print('could not find solution.')


if __name__ == '__main__':
    main()

