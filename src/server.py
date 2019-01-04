from flask import Flask
from flask import send_from_directory
from flask import jsonify
from flask import request
from flask import abort

from auxiliary.VariableDeclaration import *


# App definition
app = Flask(__name__)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(img_dir, 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/img/logo.jpg', methods=['GET'])
def get_logo():
    return send_from_directory(img_dir, 'logo.jpg')


@app.route('/css/main.css', methods=['GET'])
def get_css():
    return send_from_directory(css_dir, 'main.css')


@app.route('/', methods=['GET'])
def get_html_index():
    return send_from_directory(html_dir, 'index.html')


@app.route('/<string:path>', methods=['GET'])
def get_html_page(path):
    html_file =  path + '.html'
    return send_from_directory(html_dir, html_file)


@app.route('/rest/status', methods=['GET'])
def get_status():
    resp = jsonify( server_info )
    resp.status_code = 200
    return resp


@app.route('/rest/<string:resource>', methods=['POST', 'PUT'])
def POST_resource(resource):
    if resource in daos and resource in constructors:
        print('POST/PUT on ' + resource + ': ' + str(request.form.to_dict()))
        resource_obj = constructors[resource](dict=request.form.to_dict())
        daos[resource].insert(resource_obj)
        resp = jsonify({'status': '201'})
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


@app.errorhandler(404)
def not_found(error=None):
    return send_from_directory(html_dir, '404.html')


@app.errorhandler(405)
def not_allowed(error=None):
    data = {}
    data['status'] = '405'
    data['message'] = 'URL {} not allowed from {} HTTP method'.format(request.url, request.method)
    resp = jsonify(data)
    resp.status_code = 405
    return resp


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 80))
    app.run(host='0.0.0.0', port=port, debug=True)
