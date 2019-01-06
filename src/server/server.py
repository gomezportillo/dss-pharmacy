import os, sys, inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir  = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from auxiliary.VariableDeclaration import *


"""
This method will return the favicon of the website
"""
@app.route('/favicon.ico', methods=['GET'])
def GET_favicon():

    return send_from_directory(IMG_DIR,
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


"""
This method will return the logo of the main page of the website
"""
@app.route('/img/logo.jpg', methods=['GET'])
def GET_logo():

    return send_from_directory(IMG_DIR,
                               'logo.jpg')


"""
This method will return the CSS of the site
"""
@app.route('/css/main.css', methods=['GET'])
def GET_css():

    return send_from_directory(CSS_DIR,
                               'main.css')


"""
This method will return the main page
"""
@app.route('/', methods=['GET'])
def GET_html_index():

    return send_from_directory(HTML_DIR,
                               'index.html')


"""
This method will return any asked webpage, or the 404 webpage if not found
"""
@app.route('/<string:route>', methods=['GET'])
def GET_html_page(route):

    html_file_name =  route + '.html'
    html_file_route =  os.path.join(HTML_DIR, html_file_name)

    if os.path.isfile( html_file_route ):
        return send_from_directory(HTML_DIR,
                                   html_file_name)
    else:
        return send_from_directory(HTML_DIR,
                                   '404.html')


"""
This method overrides the default handler for the HTTP error 404 (not found)
"""
@app.errorhandler(404)
def HANDLE_not_found(error=None):

    return send_from_directory(HTML_DIR,
                               '404.html')


"""
This method overrides the default handler for the HTTP error 405 (operationnot allowed)
"""
@app.errorhandler(405)
def HANDLE_not_allowed(error=None):

    message = {}
    message['status'] = '405'
    message['message'] = 'URL {} not allowed from {} HTTP method'.format(request.url, request.method)

    response = Response(json.dumps( message, indent=4 ),
                        status=405,
                        mimetype='application/json')
    return response


"""
This method will return some information about the server for the Android app
"""
@app.route('/rest/status', methods=['GET'])
def GET_status():

    response = Response(json.dumps( server_info, indent=4 ),
                        status=200,
                        mimetype='application/json')
    return response


"""
PHARMACIES
"""
"""
This method will handle POST and PUT methods over pharmacies
"""
@app.route('/rest/pharmacies', methods=['POST', 'PUT'])
def POST_pharmacy():

    pharmacy_dict = request.form.to_dict()
    print('POST/PUT on PHARMACIES: ' + str( pharmacy_dict ))
    new_pharmacy = Pharmacy(dict=pharmacy_dict)
    DAOPharmacy.instance().insert( new_pharmacy )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response


"""
This method will handle the DELETE methods over pharmacies using URIs
"""
@app.route('/rest/pharmacies/<string:name>', methods=['DELETE'])
def DELETE_pharmacy(name):

    print('DELETE on PHARMACIES: ' + name)
    DAOPharmacy.instance().delete( name )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response



"""
This method will return all pharmacies
"""
@app.route('/rest/pharmacies', methods=['GET'])
def GET_ALL_pharmacies():

    print('GET ALL on PHARMACIES')
    pharmacies = DAOPharmacy.instance().readAll()

    format = parse_request_format( request )

    if format == 'xml':
        xml_pharmacies = ''.join([ pharmacy.toXML() for pharmacy in pharmacies ])
        response = Response('<pharmacies>{}</pharmacies>'.format(xml_pharmacies),
                            status=201,
                            mimetype='text/xml')

    else:
        json_pharmacies = [ pharmacy.toJSON() for pharmacy in pharmacies ]
        response = Response(json.dumps( json_pharmacies, indent=4 ),
                            status=201,
                            mimetype='application/json')

    return response



"""
This method will handle the GET methods over pharmacies using URIs
"""
@app.route('/rest/pharmacies/<string:name>', methods=['GET'])
def GET_pharmacy(name):

    print('GET on PHARMACIES: ' + name)
    pharmacy = DAOPharmacy.instance().find( name )

    if pharmacy is not None:
        format = parse_request_format( request )

        if format == 'xml':
            response = Response(pharmacy.toXML(),
                                status=201,
                                mimetype='text/xml')

        else:
            response = Response(json.dumps( pharmacy.toJSON(), indent=4 ),
                                status=201,
                                mimetype='application/json')

    else:
        response = Response( {},
                            status=201,
                            mimetype='application/json')

    return response


"""
PRODUCTS
"""
"""
This method will handle POST and PUT methods over products
"""
@app.route('/rest/products', methods=['POST', 'PUT'])
def POST_product():

    product_dict = request.form.to_dict()
    print('POST/PUT on PRODUCTS: ' + str( product_dict ))
    new_product = Product(dict=product_dict)
    DAOProduct.instance().insert( new_product )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response


"""
This method will handle the DELETE methods over products using URIs
"""
@app.route('/rest/products/<string:name>', methods=['DELETE'])
def DELETE_product(name):

    print('DELETE on PRODUCTS: ' + name)
    DAOProduct.instance().delete( name )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response



"""
This method will return all products
"""
@app.route('/rest/products', methods=['GET'])
def GET_ALL_products():

    print('GET ALL on PRODUCTS')
    products = DAOProduct.instance().readAll()

    format = parse_request_format( request)

    if format == 'xml':
        xml_products = ''.join([ product.toXML() for product in products ])
        response = Response('<products>{}</products>'.format(xml_products),
                            status=201,
                            mimetype='text/xml')

    else:
        json_products = [ product.toJSON() for product in products ]
        response = Response(json.dumps( json_products, indent=4 ),
                            status=201,
                            mimetype='application/json')
    return response



"""
This method will handle the GET methods over products using URIs
"""
@app.route('/rest/products/<string:name>', methods=['GET'])
def GET_product(name):

    print('GET on PRODUCTS: ' + name)
    product = DAOProduct.instance().find( name )

    if product is not None:
        format = parse_request_format( request)

        if format == 'xml':
            response = Response(product.toXML(),
                                status=201,
                                mimetype='text/xml')

        else:
            response = Response(json.dumps( product.toJSON(), indent=4 ),
                                status=201,
                                mimetype='application/json')

    else:
        response = Response({},
                            status=201,
                            mimetype='application/json')

    return response


"""
USERS
"""
"""
This method will handle POST and PUT methods over users
"""
@app.route('/rest/users', methods=['POST', 'PUT'])
def POST_user():

    user_dict = request.form.to_dict()
    print('POST/PUT on USERS: ' + str( user_dict ))
    new_user = User(dict=user_dict)
    DAOUser.instance().insert( new_user )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response


"""
This method will handle the DELETE methods over users using URIs
"""
@app.route('/rest/users/<string:name>', methods=['DELETE'])
def DELETE_user(name):

    print('DELETE on USERS: ' + name)
    DAOUser.instance().delete( name )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response



"""
This method will return all users
"""
@app.route('/rest/users', methods=['GET'])
def GET_ALL_users():

    print('GET ALL on USERS')
    users = DAOUser.instance().readAll()

    format = parse_request_format( request )

    if format == 'xml':
        xml_users = ''.join([ user.toXML() for user in users ])
        response = Response('<users>{}</users>'.format(xml_users),
                            status=201,
                            mimetype='text/xml')
    else:
        json_users = [ user.toJSON() for user in users ]
        response = Response(json.dumps( json_users, indent=4 ),
                            status=201,
                            mimetype='application/json')

    return response



"""
This method will handle the GET methods over users using URIs
"""
@app.route('/rest/users/<string:email>', methods=['GET'])
def GET_user(email):

    print('GET on USERS: ' + email)
    user = DAOUser.instance().find( email )

    if user is not None:

        format = parse_request_format( request )
        if format == 'xml':
            response = Response(user.toXML(),
                                status=201,
                                mimetype='text/xml')
        else:
            response = Response(json.dumps( user.toJSON(), indent=4 ),
                                status=201,
                                mimetype='application/json')
    else:
        response = Response( {},
                            status=201,
                            mimetype='application/json')

    return response



"""
ORDERS
"""
"""
This method will handle POST and PUT methods over orders
"""
@app.route('/rest/orders', methods=['POST', 'PUT'])
def POST_order():

    email = request.form.to_dict()['email']
    type = request.form.to_dict()['type']
    cart = request.form.to_dict()['cart']
    date = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    user = DAOUser.instance().find( email )
    print('POST/PUT on ORDERS: {}{}{}'.format( email, type, cart))

    if user is None:
        message = {'status': '404', 'message': 'User with email ' + email + ' not found.'}

    elif not cart:
        message = {'status': '409', 'message': 'Cart cannot be empty.'}

    else:
        order = Order(email, type, date, cart)
        DAOOrder.instance().insert( order )
        DAOCart.instance().deleteAll()
        message = {'status': '201'}

    response = Response(json.dumps( message ),
                        status=201,
                        mimetype='application/json')
    return response


"""
This method will handle the DELETE methods over orders using URIs
"""
@app.route('/rest/orders/<string:id>', methods=['DELETE'])
def DELETE_order(id):

    print('DELETE on ORDERS: ' + id)
    DAOOrder.instance().delete( id )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response



"""
This method will return all orders
"""
@app.route('/rest/orders', methods=['GET'])
def GET_ALL_order():

    print('GET ALL on ORDERS')
    orders = DAOOrder.instance().readAll()

    format = parse_request_format( request )

    if format == 'xml':
        xml_orders = ''.join([ order.toXML() for order in orders ])
        response = Response('<orders>{}</orders>'.format(xml_orders),
                            status=201,
                            mimetype='text/xml')

    else:
        json_orders = [ order.toJSON() for order in orders ]
        response = Response(json.dumps( json_orders, indent=4),
                            status=201,
                            mimetype='application/json')

    return response



"""
This method will handle the GET methods over orders using URIs
"""
@app.route('/rest/orders/<string:id>', methods=['GET'])
def GET_order(id):

    print('GET on ORDERS: ' + id)
    order = DAOOrder.instance().find( id )
    format = parse_request_format( request )

    if order is not None:

        if format == 'xml':
            response = Response(order.toXML(),
                                status=201,
                                mimetype='text/xml')
        else:
            response = Response(json.dumps( order.toJSON(), indent=4 ),
                                status=201,
                                mimetype='application/json')
    else:
        response = Response( {},
                            status=201,
                            mimetype='application/json')

    return response




"""
CART
"""
"""
This method will handle POST and PUT methods over cart
"""
@app.route('/rest/cart', methods=['POST', 'PUT'])
def POST_cart():

    product_dict = request.form.to_dict()
    print('POST/PUT on CART: ' + str( product_dict ))
    new_product = ProductCart(dict=product_dict)
    DAOCart.instance().insert( new_product )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response


"""
This method will handle the DELETE methods over cart using URIs
"""
@app.route('/rest/cart/<string:product>', methods=['DELETE'])
def DELETE_cart(product):

    print('DELETE on CART: ' + product)
    DAOCart.instance().delete( product )

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response


"""
This method will delete the whole cart
"""
@app.route('/rest/cart', methods=['DELETE'])
def DELETE_ALL_cart():

    print('DELETE ALL on CART')
    DAOCart.instance().deleteAll()

    response = Response(json.dumps( {'status': '201'}, indent=4 ),
                        status=201,
                        mimetype='application/json')
    return response


"""
This method will return the current cart
"""
@app.route('/rest/cart', methods=['GET'])
def GET_ALL_cart():

    print('GET ALL on CART')
    cart = DAOCart.instance().readAll()

    format = parse_request_format( request )

    if format == 'xml':
        xml_cart = ''.join([ product.toXML() for product in cart ])
        response = Response('<cart>{}</cart>'.format(xml_cart),
                            status=201,
                            mimetype='text/xml')

    else:
        json_cart = [ product.toJSON() for product in cart ]
        response = Response(json.dumps( json_cart, indent=4 ),
                            status=201,
                            mimetype='application/json')

    return response



"""
This method will handle the GET methods over cart using URIs
"""
@app.route('/rest/cart/<string:product>', methods=['GET'])
def GET_cart(product):

    print('GET on CART: ' + product)
    product = DAOCart.instance().find( product )

    if product is not None:

        format = parse_request_format( request)

        if format == 'xml':
            response = Response(product.toXML(),
                                status=201,
                                mimetype='text/xml')

        else:
            response = Response(json.dumps( product.toJSON(), indent=4 ),
                                status=201,
                                mimetype='application/json')

    else:
        response = Response( {},
                            status=201,
                            mimetype='application/json')

    return response


def parse_request_format( request ):

    try:
        format = request.url.split('?format=')[1].lower()
    except IndexError:
        return 'json'

    if format in ['xml', 'json']:
        return format
    else:
        return 'json'



if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True)
