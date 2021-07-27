"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from werkzeug.wrappers import response
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
import json
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = members
    if response_body:
        return jsonify(response_body), 200
    else:
        msg={"msg": "Familia no encontrada"}
        return jsonify(msg), 404

@app.route('/member', methods=['POST'])
def handle_family():
    # this is how you can use the Family datastructure by calling its methods   
    member=json.loads(request.data)
   
    if not member or member==None:
        msg={"msg":"Información ingresada de manera incorrecta"}
        return jsonify(msg),400
    else:
        family=jackson_family.add_member(member)
        return jsonify(family),200

@app.route('/member/<int:member_id>', methods=['GET'])
def member_byid(member_id):

    # this is how you can use the Family datastructure by calling its methods
    member=jackson_family.get_member(member_id)
    if member:
        response_body = member
        return jsonify(response_body), 200
    else:
        response_body={"msg": 'Miembro de familia no encontrado'}
        return response_body,404
        
@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    msg = jackson_family.delete_member(member_id)
    if msg:
        return jsonify(msg),200
    else:
        msg={"msg":"Id ingresado no coincide con ningún familiar"}
        return jsonify(msg),400

@app.route('/member/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    member=json.loads(request.data)
    msg=jackson_family.update_member(member,member_id)
    if member:
        return jsonify(msg),200
    else:
        msg={"msg":"Información ingresada de manera incorrecta"}
        return jsonify(msg),400



# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
