from flask_restful import Resource
import logging as logger
from models import EmployeeModel
from flask import Flask, jsonify, request, make_response
from flask_mongoengine import MongoEngine
#from main import appInstance
from flask_jwt import JWT, jwt_required



###########
class Employee(Resource):
    def get(self):
        employees = EmployeeModel.objects.all()
        return jsonify({'data': employees})
        
    @jwt_required()
    def post(self):
        content = request.get_json()
        employee = EmployeeModel(employee_id=content['employee_id'], employee_name=content['employee_name'])
        employee.save()
        #return make_response("", 201)
        return {"you sent":content}

    def put(self):
        pass

    def delete(self):
        pass

class EmployeeByName(Resource):
    def get(self,employee_name):
        employee_obj = EmployeeModel.objects(employee_name=employee_name).first()
        if employee_obj:
            return jsonify(employee_obj.to_json())
        else:
            return make_response("", 404)
        #logger.debug("Inside GET")
        #return {"message": "Inside GET Method:{}".format(emply_id) }, 200

    def post(self):
        pass

    @jwt_required()
    def put(self,employee_name):
        content = request.get_json()
        employee_obj = EmployeeModel.objects(employee_name=employee_name).first()
        if employee_obj:
            employee_obj.update(employee_name=content['employee_name'])
            return make_response("Updated", 201)
        else:
            return make_response("not found", 404)

    @jwt_required()
    def delete(self, employee_name):
        employee_obj = EmployeeModel.objects(employee_name=employee_name).first()
        if employee_obj:
            employee_obj.delete()
            return make_response("Deleted", 201)
        else:
            return make_response("not found", 404)