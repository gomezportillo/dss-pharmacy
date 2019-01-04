
from auxiliary.VariableDeclaration import *


"""
This method will return the favicon of the website
"""
@app.route('/favicon.ico')
def favicon():

    return send_from_directory(IMG_DIR,
                               'favicon.ico',
                               mimetype='image/vnd.microsoft.icon')


"""
This method will return the logo of the main page of the website
"""
@app.route('/img/logo.jpg', methods=['GET'])
def get_logo():

    return send_from_directory(IMG_DIR,
                               'logo.jpg')


"""
This method will return the CSS of the site
"""
@app.route('/css/main.css', methods=['GET'])
def get_css():

    return send_from_directory(CSS_DIR,
                               'main.css')


"""
This method will return the main page
"""
@app.route('/', methods=['GET'])
def get_html_index():

    return send_from_directory(HTML_DIR,
                               'index.html')


"""
This method will return any asked webpage, or the 404 webpage if not found
"""
@app.route('/<string:route>', methods=['GET'])
def get_html_page(route):

    html_file =  route + '.html'
    print(html_file)
    print(os.path.isfile(html_file))

    if os.path.isfile( os.path.join(HTML_DIR, html_file )):
        return send_from_directory(HTML_DIR,
                                   html_file)
    else:
        return send_from_directory(HTML_DIR,
                                   '404.html')


"""
This method overrides the default handler for the HTTP error 404 (not found)
"""
@app.errorhandler(404)
def not_found(error=None):

    return send_from_directory(html_dir,
                               '404.html')


"""
This method overrides the default handler for the HTTP error 405 (operationnot allowed)
"""
@app.errorhandler(405)
def not_allowed(error=None):

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
def get_status():

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

    response = Response(json.dumps( pharmacies, indent=4 ),
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
        response = Response(json.dumps( pharmacy.toJSON(), indent=4 ),
                            status=201,
                            mimetype='application/json')
    else:
        response = Response( {},
                            status=201,
                            mimetype='application/json')

    return response




"""
#############################################################################################
"""
@app.route('/rest/<string:resource>', methods=['POST', 'PUT'])
def POST_resource(resource):
    if resource in daos and resource in constructors:
        print('POST/PUT on ' + resource + ': ' + str(request.form.to_dict()))
        resource_obj = constructors[resource](dict=request.form.to_dict())
        daos[resource].insert(resource_obj)
        resp = jsonify()
        resp.status_code = 201
        return resp
    else:
        abort(404)


@app.route('/rest/<string:resource>', methods=['DELETE'])
def DELETE_product(resource):
    name = request.form.to_dict()['name']
    daos[resource].delete(name)
    resp = jsonify({'status': '201'})
    resp.status_code = 201
    return resp


# Overrides the generic template method
@app.route('/rest/orders', methods=['POST', 'PUT'])
def POST_order():
    email = request.form.to_dict()['email']
    type = request.form.to_dict()['type']
    date = datetime.datetime.now()
    cart = daos['cart'].readAll()
    user = daos['users'].find( email )

    if user is None:
        resp = jsonify({'status': '404', 'message': 'User with email ' + email + ' not found.'})

    elif not cart:
        resp = jsonify({'status': '409', 'message': 'Cart cannot be empty.'})

    else:
        order = Order(email, type, date, cart)
        daos['orders'].insert( order )
        daos['cart'].deleteAll()
        resp = jsonify({'status': '201'})

    resp.status_code = 201
    return resp


@app.route('/rest/<string:resource>/all', methods=['GET'])
def GET_ALL_resources(resource):
    if resource in daos:
        result = daos[resource].readAll()
        resp = jsonify(result)
        resp.status_code = 200
        return resp
    else:
        abort(404)


@app.route('/rest/<string:resource>/all', methods=['DELETE'])
def DELETE_all(resource):
    daos[resource].deleteAll()
    resp = jsonify({'status': '201'})
    resp.status_code = 201
    return resp





if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True)
