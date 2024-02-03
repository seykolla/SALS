import googlemaps
import responses
import random


responses.add(
            responses.POST,
            "https://www.googleapis.com/geolocation/v1/geolocate",
            body='{"location": {"lat": 51.0,"lng": -0.1},"accuracy": 1200.4}',
            status=200,
            content_type="application/json",
        )

client = googlemaps.Client(key= 'AIzaSyDZP67HsK_6GmGq3WaL4IIZOeHIbHgg-hk')

location = client.geolocate()['location']
print(location)
map_data = client.reverse_geocode(location)

distance_km = 2
distance_m = distance_km *1000

place = ['urgent care', 'veterinary services']

nearby_places = client.places_nearby(keyword= place[1], location =location, radius = distance_m)

if(nearby_places['results'] is None):
    print('none found in the range')

for i in nearby_places['results']:
    wait_time = random.randint(1, 180)
    destination = i['geometry']['location']
    distance = client.distance_matrix(origins = location, destinations = destination)['rows'][0]['elements'][0]['distance']['text']
    print(f"name: {i['name']}, address: {i['vicinity']}, distance: {distance}, wait time: {wait_time}, open:{i['opening_hours']['open_now']}")
    print()