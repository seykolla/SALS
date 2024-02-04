import googlemaps
import responses
import random

class LifeLink:

    def __init__(self, distance, service):
        with open('initialize.txt', 'r') as f:
            self.distance = float(f.readline()[0:2]) * 1.60934 *1000
            service = f.readline()

        self.client = googlemaps.Client(key= 'AIzaSyDZP67HsK_6GmGq3WaL4IIZOeHIbHgg-hk')
        self.location = self.client.geolocate()['location']
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









