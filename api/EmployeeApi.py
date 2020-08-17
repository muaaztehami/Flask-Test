from flask_restful import Resource
import logging as logger
from models import EmployeeModel
from flask import Flask, jsonify, request, make_response
from flask_mongoengine import MongoEngine
#from main import appInstance
from flask_jwt import JWT, jwt_required



###########
class Employee(Resource):
    #@jwt_required()
    def get(self):
       # emplys = EmployeeModel.objects.all()
        emplys = []
        for emply in EmployeeModel.objects:
            emplys.append(emply)
        #logger(emplys)
        return jsonify({'data': emplys})
        
    @jwt_required()
    def post(self):
        content = request.get_json()
        emply = EmployeeModel(emply_id=content['emply_id'], emply_name=content['emply_name'])
        emply.save()
        #return make_response("", 201)
        return {"you sent":content}

    def put(self):
        pass

    def delete(self):
        pass

class EmployeeByName(Resource):
    def get(self,emply_name):
        emply_obj = EmployeeModel.objects(emply_name=emply_name).first()
        if emply_obj:
            return jsonify(emply_obj.to_json())
        else:
            return make_response("", 404)
        #logger.debug("Inside GET")
        #return {"message": "Inside GET Method:{}".format(emply_id) }, 200

    def post(self):
        pass

    @jwt_required()
    def put(self,emply_name):
        content = request.get_json()
        emply_obj = EmployeeModel.objects(emply_name=emply_name).first()
        emply_obj.update(emply_name=content['emply_name'])

    @jwt_required()
    def delete(self, emply_name):
        emply_obj = EmployeeModel.objects(emply_name=emply_name).first()
        if emply_obj:
            emply_obj.delete()
            return make_response("Deleted", 201)
        else:
            return make_response("not found", 404)