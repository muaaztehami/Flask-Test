from flask import Flask, jsonify, request, make_response
import logging as logger
from models import ProjectModel, EmployeeModel, ClientModel, appInstance
from flask_jwt import JWT, jwt_required
#from main import celery

from celery import Celery
BROKER_URL = 'redis://localhost:6379/'
celery = Celery('apis', broker=BROKER_URL)



@appInstance.route('/funnelbeam/check_employees',methods=['GET'])
def process():
    check_employees.delay()
    return 'celery worked'

@celery.task(name='apis.check_employees')
def check_employees():
    emplys = EmployeeModel.objects.all()
    not_working = ''
    for e in emplys:
        if e['project_id'] == None:
            not_working +=e['emply_name']
    return not_working
#check_employees.delay()

@jwt_required()
@appInstance.route('/add_employee/<proj_name>/<emply_name>', methods=['PUT'])
def add_employee_to_project(proj_name, emply_name):
    the_project = ProjectModel.objects(proj_name=proj_name).first()
    emply_obj = EmployeeModel.objects(emply_name=emply_name).first()
    emply_obj.update(project_id=the_project['id'])
    return make_response({"employees":emply_obj}, 201)
    
@jwt_required()
@appInstance.route('/remove_employee/<proj_name>/<emply_name>', methods=['PUT'])
def remove_employee_to_project(proj_name, emply_name):
    the_project = ProjectModel.objects(proj_name=proj_name).first()
    emply_obj = EmployeeModel.objects(emply_name=emply_name).first()
    emply_obj.update(project_id=None)
    return make_response({"employees":emply_obj}, 201)


##################################
@jwt_required()
@appInstance.route('/add_project/<clnt_name>/<proj_name>', methods=['PUT'])
def add_project_to_client(clnt_name, proj_name):
    the_client = ClientModel.objects(clnt_name=clnt_name).first()
    proj_obj = ProjectModel.objects(proj_name=proj_name).first()
    proj_obj.update(client_id=the_client['id'])
    return make_response({"projects":proj_obj}, 201)

@jwt_required()
@appInstance.route('/remove_project/<clnt_name>/<proj_name>', methods=['PUT'])
def remove_project_to_client(clnt_name, proj_name):
    the_client = ClientModel.objects(clnt_name=clnt_name).first()
    proj_obj = ProjectModel.objects(proj_name=proj_name).first()
    proj_obj.update(client_id=None)
    return make_response({"projects":proj_obj}, 201)
