
class Pharmacy:

    def __init__(self, name=None, latitude=None, longitude=None, dict=None):
        if dict is None:
            self.name      = name
            self.latitude  = float( latitude )
            self.longitude = float( longitude )
        else:
            self.name      = dict['name']
            self.latitude  = float( dict['latitude'] )
            self.longitude = float( dict['longitude'] )


    def toJSON(self):
        return {'name':self.name,'latitude':self.latitude,'longitude':self.longitude}


    def toXML(self):
        xml_msg = '<pharmacy>'
        xml_msg += '<name>{}</name>'.format( self.name )
        xml_msg += '<latitude>{}</latitude>'.format( self.latitude )
        xml_msg += '<longitude>{}</longitude>'.format( self.longitude )
        xml_msg += '</pharmacy>'

        return xml_msg
