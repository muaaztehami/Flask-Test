from flask_restful import Api
from main import appInstance
from .EmployeeApi import Employee, EmployeeByName
from .ProjectApi import Project, ProjectByName
from .ClientApi import Client, ClientByName


restServer = Api(appInstance)
restServer.add_resource(Employee,"/funnelbeam/employee")
restServer.add_resource(EmployeeByName,"/funnelbeam/employee/<emply_name>")

restServer.add_resource(Project,"/funnelbeam/project")
restServer.add_resource(ProjectByName,"/funnelbeam/project/<proj_name>")

restServer.add_resource(Client,"/funnelbeam/client")
restServer.add_resource(ClientByName,"/funnelbeam/client/<clnt_name>")