from flask_restful import Resource
import logging as logger
from models import ClientModel, ProjectModel, EmployeeModel
from flask import Flask, jsonify, request, make_response
from flask_mongoengine import MongoEngine
from flask_jwt import JWT, jwt_required



###########
class Client(Resource):
    def get(self):
        clnts = []
        for clnt in ClientModel.objects:
            clnts.append(clnt)
        return jsonify({'data': clnts})
        
    @jwt_required()
    def post(self):
        content = request.get_json()
        clnt = ClientModel(clnt_id=content['clnt_id'], clnt_name=content['clnt_name'])
        clnt.save()
        #return make_response("", 201)
        return {"you sent":content}

    def put(self):
        pass

    def delete(self):
        pass

class ClientByName(Resource):
    def get(self,clnt_name):
        the_client = ClientModel.objects(clnt_name=clnt_name).first()
        if the_client:
            #return jsonify(clnt_obj.to_json())
            clnt_projs = ProjectModel.objects(client_id=the_client['id']).all()
            proj_lst = ''
            emply_lst = ''
            for i in clnt_projs:
                proj_lst += i['proj_name'] + '........'

                proj_emplys = EmployeeModel.objects(project_id=i['id']).all()
                emply_lst += 'Project Name: {}  Employees Names: '.format(i['proj_name'])
                for i in proj_emplys:
                    emply_lst += i['emply_name'] + '...... '
                    #return jsonify({"project":the_project['proj_name'], "employees":emply_lst})

            return jsonify({"client":the_client['clnt_name'], "projects":proj_lst, "employees":emply_lst})


        #clnt_obj = ClientModel.objects(clnt_id=clnt_id).first()
        #if clnt_obj:
        #    return jsonify(clnt_obj.to_json())
        #else:
            return make_response("", 404)
        

    def post(self):
        pass
    
    @jwt_required()
    def put(self,clnt_name):
        content = request.get_json()
        clnt_obj = ClientModel.objects(clnt_name=clnt_name).first()
        clnt_obj.update(clnt_name=content['clnt_name'])

    @jwt_required()
    def delete(self,clnt_name):
        clnt_obj = ClientModel.objects(clnt_name=clnt_name).first()
        if clnt_obj:
            clnt_obj.delete()
            return make_response("Deleted", 201)
        else:
            return make_response("not found", 404)