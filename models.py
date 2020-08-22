
from flask_mongoengine import MongoEngine
from main import appInstance
from flask_pymongo import PyMongo


database_name = "test"
mongodb_password = "foll123"
DB_URI = "mongodb+srv://muaaztehami:{}@cluster0.fye8p.mongodb.net/{}?retryWrites=true&w=majority".format(
    mongodb_password, database_name
)
appInstance.config["MONGODB_HOST"] = DB_URI
db = MongoEngine()
db.init_app(appInstance)


class ClientModel(db.Document):
    client_id = db.IntField()
    client_name = db.StringField()

    def to_json(self):
        return {
            "client_id": self.client_id,
            "client_name": self.client_name
        }

class ProjectModel(db.Document):
    project_id = db.IntField()
    project_name = db.StringField()
    clients_id = db.ReferenceField(ClientModel)

    def to_json(self):
        return {
            "project_id": self.project_id,
            "project_name": self.project_name
        }

class EmployeeModel(db.Document):
    employee_id = db.IntField()
    employee_name = db.StringField()
    projects_id = db.ReferenceField(ProjectModel)

    def to_json(self):
        return {
            "employee_id": self.employee_id,
            "employee_name": self.employee_name
        }