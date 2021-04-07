import os
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc
import json
from flask_cors import CORS
import json

from database.models import db_drop_and_create_all, setup_db, Drink
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

'''
@TODO uncomment the following line to initialize the datbase
!! NOTE THIS WILL DROP ALL RECORDS AND START YOUR DB FROM SCRATCH
!! NOTE THIS MUST BE UNCOMMENTED ON FIRST RUN
'''
db_drop_and_create_all()

## ROUTES
'''
@TODO implement endpoint
    GET /drinks
        it should be a public endpoint
        it should contain only the drink.short() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks')
def get_drinks():
    drinks = Drink.query.all()
    short_drinks = []
    for drink in drinks:
        short_drinks.append(drink.short())
    
    #print(short_drinks)

    return jsonify({
        'success' : True,
        'drinks' : short_drinks
    })

'''
@TODO implement endpoint
    GET /drinks-detail
        it should require the 'get:drinks-detail' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drinks} where drinks is the list of drinks
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks-detail')
@requires_auth('get:drinks-detail')
def get_drink_details(test):
    drinks = Drink.query.all()
    long_drinks = []
    for drink in drinks:
        long_drinks.append(drink.long())
    
    #print(long_drinks)

    return jsonify({
        'success' : True,
        'drinks' : long_drinks
    })

'''
@TODO implement endpoint
    POST /drinks
        it should create a new row in the drinks table
        it should require the 'post:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the newly created drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks', methods=['POST'])
@requires_auth('post:drinks')
def add_drink(test):
    #print(test)
    newtitle = request.get_json()['title']
    newrecipe = request.get_json()['recipe']
    newrecipe = str(newrecipe).replace("'", '"')
    #print(newtitle, newrecipe)

    new_drink = Drink(title=newtitle, recipe=newrecipe)
    try:
        new_drink.insert()
        #print('done')
        #print(new_drink.id)
    except Exception as e:
        print(e)
        abort(422)
    
    return jsonify({
        'success' : True,
        'drinks' : new_drink.id
    })

'''
@TODO implement endpoint
    PATCH /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should update the corresponding row for <id>
        it should require the 'patch:drinks' permission
        it should contain the drink.long() data representation
    returns status code 200 and json {"success": True, "drinks": drink} where drink an array containing only the updated drink
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['PATCH'])
@requires_auth('patch:drinks')
def update_drink(perms, id):
    if id is None:
        abort(404)
    
    try:
        newtitle = request.get_json()['title']
        title = True
    except:
        title = False
    
    try:
        newrecipe = request.get_json()['recipe']
        newrecipe = str(newrecipe).replace("'", '"')
        recipe = True
    except:
        recipe = False
    #print(newtitle, newrecipe)
    
    drink = Drink.query.filter(Drink.id == id).first()

    if title:
        drink.title = newtitle
    if recipe:
        drink.recipe = newrecipe

    drink.update()

    drink_list = []
    drink_list.append(drink.long())

    return jsonify({
        'success' : True,
        'drinks' : drink_list
    })

'''
@TODO implement endpoint
    DELETE /drinks/<id>
        where <id> is the existing model id
        it should respond with a 404 error if <id> is not found
        it should delete the corresponding row for <id>
        it should require the 'delete:drinks' permission
    returns status code 200 and json {"success": True, "delete": id} where id is the id of the deleted record
        or appropriate status code indicating reason for failure
'''
@app.route('/drinks/<int:id>', methods=['DELETE'])
@requires_auth('delete:drinks')
def delete_drink(perms, id):
    #print(perms)
    if id is None:
        abort(404)

    drink = Drink.query.filter(Drink.id == id).first()
    try:
        drink.delete()
    except Exception as e:
        print(e)
        abort(422)

    return jsonify({
        'success' : True,
        'delete' : id
    })

## Error Handling
'''
Example error handling for unprocessable entity
'''
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

'''
@TODO implement error handlers using the @app.errorhandler(error) decorator
    each error handler should return (with approprate messages):
             jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''

'''
@TODO implement error handler for 404
    error handler should conform to general task above 
'''
@app.errorhandler(404)
def not_found(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404

'''
@TODO implement error handler for AuthError
    error handler should conform to general task above 
'''
@app.errorhandler(AuthError)
def authorization_error(error):
    return jsonify({
                    "success": False, 
                    "error": 401,
                    "message": "unauthorized"
                    }), 401
