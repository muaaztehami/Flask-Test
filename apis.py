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
def check_employees(task_id=None):
    not_working = EmployeeModel.objects(projects_id=None).all()
    employee_names = ''
    for e in not_working:
        employee_names +=e['employee_name']
    return employee_names
#check_employees.delay()

@jwt_required()
@appInstance.route('/add_employee/<project_name>/<employee_name>', methods=['PUT'])
def add_employee_to_project(project_name, employee_name):
    the_project = ProjectModel.objects(project_name=project_name).first()
    employee_obj = EmployeeModel.objects(employee_name=employee_name).first()
    employee_obj.update(projects_id=the_project['id'])
    return make_response({"employees":employee_obj}, 201)
    
@jwt_required()
@appInstance.route('/remove_employee/<project_name>/<employee_name>', methods=['PUT'])
def remove_employee_to_project(project_name, employee_name):
    the_project = ProjectModel.objects(project_name=project_name).first()
    employee_obj = EmployeeModel.objects(employee_name=employee_name).first()
    employee_obj.update(projects_id=None)
    return make_response({"employees":employee_obj}, 201)


##################################
@jwt_required()
@appInstance.route('/add_project/<client_name>/<project_name>', methods=['PUT'])
def add_project_to_client(client_name, project_name):
    the_client = ClientModel.objects(client_name=client_name).first()
    project_obj = ProjectModel.objects(project_name=project_name).first()
    project_obj.update(clients_id=the_client['id'])
    return make_response({"projects":project_obj}, 201)

@jwt_required()
@appInstance.route('/remove_project/<client_name>/<project_name>', methods=['PUT'])
def remove_project_to_client(client_name, project_name):
    the_client = ClientModel.objects(client_name=client_name).first()
    project_obj = ProjectModel.objects(project_name=project_name).first()
    project_obj.update(clients_id=None)
    return make_response({"projects":project_obj}, 201)
