from flask_restful import Resource
import logging as logger
from models import ClientModel, ProjectModel, EmployeeModel
from flask import Flask, jsonify, request, make_response
from flask_mongoengine import MongoEngine
from flask_jwt import JWT, jwt_required



###########
class Client(Resource):
    def get(self):
        clients = ClientModel.objects.all()
        return jsonify({'data': clients})
        
    @jwt_required()
    def post(self):
        content = request.get_json()
        client = ClientModel(client_id=content['client_id'], client_name=content['client_name'])
        client.save()
        return {"your data":content}

    def put(self):
        pass

    def delete(self):
        pass

class ClientByName(Resource):
    def get(self,client_name):
        the_client = ClientModel.objects(client_name=client_name).first()
        if the_client:
            #return jsonify(clnt_obj.to_json())
            client_projects = ProjectModel.objects(clients_id=the_client['id']).all()
            project_lst = ''
            employee_lst = ''
            for i in client_projects:
                project_lst += i['project_name'] + '........'

                project_employees = EmployeeModel.objects(projects_id=i['id']).all()
                employee_lst += 'Project Name: {}  Employees Names: '.format(i['project_name'])
                for i in project_employees:
                    employee_lst += i['employee_name'] + '...... '
                    #return jsonify({"project":the_project['project_name'], "employees":employee_lst})

            return jsonify({"client":the_client['client_name'], "projects":project_lst, "employees":employee_lst})


        #clnt_obj = ClientModel.objects(clnt_id=clnt_id).first()
        #if clnt_obj:
        #    return jsonify(clnt_obj.to_json())
        #else:
            return make_response("", 404)
        

    def post(self):
        pass
    
    @jwt_required()
    def put(self,client_name):
        content = request.get_json()
        client_obj = ClientModel.objects(client_name=client_name).first()
        if client_obj:
            client_obj.update(client_name=content['client_name'])
            return make_response("Updated", 201)
        else:
            return make_response("not found", 404)

    @jwt_required()
    def delete(self,client_name):
        client_obj = ClientModel.objects(client_name=client_name).first()
        if client_obj:
            client_obj.delete()
            return make_response("Deleted", 201)
        else:
            return make_response("not found", 404)