import googlemaps
import responses
import random

class LifeLink:
    def __init__(self, distance, service):
        assert service == "urgent care" or service =="vet"
        assert type(distance)== float or type(distance) == int

        self.client = googlemaps.Client(key= 'AIzaSyDZP67HsK_6GmGq3WaL4IIZOeHIbHgg-hk')
        self.location = self.client.geolocate()['location']
        self.distance = distance * 1.60934 *1000

        if(service == 'vet'):
            self.service = 'veterinary services'
        else:
            self.service = service

    def get_current_location(self):
        return self.location
    
    def get_distance(self):
        return self.distance

    def get_service(self):
        return self.service
    
    def get_nearby_places(self):
        nearby_places = self.client.places_nearby(keyword= self.service, location =self.location, radius = self.distance)
        if(nearby_places['results'] is None):
            return None #none found
        else:
            results = []
            for i in nearby_places['results']:
                wait_time = random.randint(1, 180)
                destination = i['geometry']['location']
                distance = self.client.distance_matrix(origins = self.location, destinations = destination)['rows'][0]['elements'][0]['distance']['text']
                results.append({'name':i['name'], 'address': i['vicinity'], 'distance': {distance}, 'wait_time': wait_time, 'open': i['opening_hours']['open_now']})
            return results

<<<<<<< HEAD
<<<<<<< HEAD

with open('instance.txt', 'r') as f:
    distance = float(f.readline(1))
    service = f.readline(2)


instace = LifeLink(distance, service)
=======
=======
>>>>>>> 92d2a9554c532f5fb1afc772d69ffd14b09deac3
f = open('initialize.txt', 'r')
instance = LifeLink(f.readline().rstrip()[0:2], 'vet')
places = instance.get_nearby_places()
marker = instance.get_current_location()
with open('location.txt', 'w') as f:
    f.write(str(list(places)) + "\n")
    f.write(str(list(marker)))
    f.close()
<<<<<<< HEAD
>>>>>>> ed8d18a788eeb88aecadf39d297d95a32616cd92
=======
=======

with open('instance.txt', 'r') as f:
    distance = float(f.readline(1))
    service = f.readline(2)


instace = LifeLink(distance, service)
>>>>>>> 3512f91 (hsjdflksjdf)
>>>>>>> 92d2a9554c532f5fb1afc772d69ffd14b09deac3
