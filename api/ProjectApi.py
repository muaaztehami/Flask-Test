from flask_restful import Resource
import logging as logger
from models import ProjectModel, EmployeeModel
from flask import Flask, jsonify, request, make_response
from flask_mongoengine import MongoEngine
from flask_jwt import JWT, jwt_required




###########
class Project(Resource):
    def get(self):
        projects = ProjectModel.objects.all()
        return jsonify({'data': projects})
        
    @jwt_required()
    def post(self):
        content = request.get_json()
        project = ProjectModel(project_id=content['project_id'], project_name=content['project_name'])
        project.save()
        #return make_response("", 201)
        return {"you sent":content}


class ProjectByName(Resource):
    def get(self,project_name):
        the_project = ProjectModel.objects(project_name=project_name).first()
        if the_project:
            
            project_employees = EmployeeModel.objects(projects_id=the_project['id']).all()
            
            lst = ''
            for i in project_employees:
                lst += i['employee_name'] + '........'
            return jsonify({"project":the_project['project_name'], "employees":lst})


        #proj_obj = ProjectModel.objects(proj_id=proj_id).first()
        #if proj_obj:
        #    return jsonify(proj_obj.to_json())
        #else:
        return make_response("Not found", 404)
        

    def post(self):
        pass

    @jwt_required()
    def put(self,project_name):
        content = request.get_json()
        project_obj = ProjectModel.objects(project_name=project_name).first()
        if project_obj:
            project_obj.update(project_name=content['project_name'])
            return make_response("Updated", 201)
        else:
            return make_response("not found", 404)

    @jwt_required()
    def delete(self,project_name):
        project_obj = ProjectModel.objects(project_name=project_name).first()
        if project_obj:
            project_emplys = EmployeeModel.objects(projects_id=project_obj['id']).all()
            project_emplys.update(projects_id=None)
            project_obj.delete()
            return make_response("Deleted", 201)
        else:
            return make_response("not found", 404)