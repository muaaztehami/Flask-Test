from flask_restful import Resource
import logging as logger
from models import ProjectModel, EmployeeModel
from flask import Flask, jsonify, request, make_response
from flask_mongoengine import MongoEngine
from flask_jwt import JWT, jwt_required




###########
class Project(Resource):
    def get(self):
       # emplys = EmployeeModel.objects.all()
        projs = []
        for proj in ProjectModel.objects:
            projs.append(proj)
        return jsonify({'data': projs})
        
    @jwt_required()
    def post(self):
        content = request.get_json()
        proj = ProjectModel(proj_id=content['proj_id'], proj_name=content['proj_name'])
        proj.save()
        #return make_response("", 201)
        return {"you sent":content}


class ProjectByName(Resource):
    def get(self,proj_name):
        the_project = ProjectModel.objects(proj_name=proj_name).first()
        if the_project:
            
            proj_emplys = EmployeeModel.objects(project_id=the_project['id']).all()
            
            lst = ''
            for i in proj_emplys:
                lst += i['emply_name'] + '........'
            return jsonify({"project":the_project['proj_name'], "employees":lst})


        #proj_obj = ProjectModel.objects(proj_id=proj_id).first()
        #if proj_obj:
        #    return jsonify(proj_obj.to_json())
        #else:
        return make_response("Not found", 404)
        

    def post(self):
        pass

    @jwt_required()
    def put(self,proj_name):
        content = request.get_json()
        proj_obj = ProjectModel.objects(proj_name=proj_name).first()
        proj_obj.update(proj_name=content['proj_name'])

    @jwt_required()
    def delete(self,proj_name):
        proj_obj = ProjectModel.objects(proj_name=proj_name).first()
        if proj_obj:
            proj_emplys = EmployeeModel.objects(project_id=proj_obj['id']).all()
            for e in proj_emplys:
                e['project_id']=None
            
            proj_obj.delete()
            return make_response("Deleted", 201)
        else:
            return make_response("not found", 404)