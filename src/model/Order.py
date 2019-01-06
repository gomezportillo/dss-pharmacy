
class Order:

    def __init__(self, user='email@dss', type='Purchase', date='now', products={}, id=0):
        self.user = user
        self.type = type
        self.date = date
        self.cart = products
        self.id   = id


    def toJSON(self):
        json_msg             = {}
        json_msg['id']       = self.id
        json_msg['email']    = self.user
        json_msg['type']     = self.type
        json_msg['date']     = self.date
        json_msg['products'] = self.cart
        return json_msg

    def toXML(self):
        xml_msg = '<order>'
        xml_msg += '<id>{}</id>'.format( self.id )
        xml_msg += '<email>{}</email>'.format( self.user )
        xml_msg += '<type>{}</type>'.format( self.type )
        xml_msg += '<date>{}</date>'.format( self.date )

        xml_msg += '<products>'
        for product in self.cart.split(';'):
            if product:
                xml_msg += '<product>{}</product>'.format( product )
        xml_msg += '</products>'
        xml_msg += '</order>'

        return xml_msg
