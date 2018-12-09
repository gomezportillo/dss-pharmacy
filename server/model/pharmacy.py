import json

class Pharmacy:

    def __init__(self, name=None, latitude=None, longitude=None, dict=None):
        if dict is None:
            self.name      = name
            self.latitude  = float(latitude)
            self.longitude = float(longitude)
        else:
            self.name      = dict['name']
            self.latitude  = float(dict['latitude'])
            self.longitude = float(dict['longitude'])


    def toJSON(self):
        # return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)
        return {'name':self.name,'latitude':self.latitude,'longitude':self.longitude}
