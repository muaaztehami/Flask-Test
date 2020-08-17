
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
    clnt_id = db.IntField()
    clnt_name = db.StringField()

    def to_json(self):
        return {
            "clnt_id": self.clnt_id,
            "clnt_name": self.clnt_name
        }

class ProjectModel(db.Document):
    proj_id = db.IntField()
    proj_name = db.StringField()
    client_id = db.ReferenceField(ClientModel)

    def to_json(self):
        return {
            "proj_id": self.proj_id,
            "proj_name": self.proj_name
        }

class EmployeeModel(db.Document):
    emply_id = db.IntField()
    emply_name = db.StringField()
    project_id = db.ReferenceField(ProjectModel)

    def to_json(self):
        return {
            "emply_id": self.emply_id,
            "emply_name": self.emply_name
        }