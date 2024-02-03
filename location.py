import googlemaps
import responses
import random




client = googlemaps.Client(key= 'AIzaSyDZP67HsK_6GmGq3WaL4IIZOeHIbHgg-hk')

location = client.geolocate()['location']
map_data = client.reverse_geocode(location)

distance_mi = 1
distance_m = distance_mi * 1.60934 *1000

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