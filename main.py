from flask import Flask, jsonify, request, make_response
import logging as logger
from security import auth, identity
from flask_jwt import JWT, jwt_required
from celery import Celery



appInstance = Flask(__name__)

appInstance.secret_key = '#0#'
jwt = JWT(appInstance,auth,identity)







if __name__ == '__main__':
    from api import *
    from apis import *
    appInstance.run(debug=True)
    