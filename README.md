# Flask-Test
,,,,,,,,,,,,
DESCRIPTION:
'''''''''''
This project is connected with mongodb and restful APIs are implemented for CRUD operations
To check APIs i have used POSTMAN
Tech Stack: Python, Flask, Celery, MongoDB

,,,,,,,,,,,
HOW TO USE:
'''''''''''
-TO RUN PROJECT:
	python main.py
	
-TO RUN CELERY:
	celery -A apis.celery worker --loglevel=info -P eventlet


...........(PUT, DELETE, POST methods requires token authentication.......
................in order to get token POST request on).......
-GET TOKEN (POST)
	http://127.0.0.1:5000/auth
	{
	   "username":"admin",
	   "password":"admin123"
	} 

*******************EMPLOYEE****************************
- ADD EMPLOYEE (POST)
	http://127.0.0.1:5000/funnelbeam/employee
	{
	   "employee_id":1,
	   "employee_name":"xyz"
	}

- EDIT EMPLOYEE (PUT)
	http://127.0.0.1:5000/funnelbeam/employee/<empleyee_name>
	{
	   "employee_name":"xyz"
	}

- DELETE EMPLOYEE (DELETE)
	http://127.0.0.1:5000/funnelbeam/employee/<employee_name>

- GET EMPLOYEE BY NAME (GET)
	http://127.0.0.1:5000/funnelbeam/employee/<employee_name>

- GET EMPLOYEES (GET)
	http://127.0.0.1:5000/funnelbeam/employee
**************************************************************************
*******************CLIENT*****************************
- ADD CLIENT (POST)
	http://127.0.0.1:5000/funnelbeam/client
	{
	   "client_id":1,
	   "client_name":"xyz"
	}

- EDIT CLIENT (PUT)
	http://127.0.0.1:5000/funnelbeam/client/<client_name>
	{
	   "client_name":"xyz"
	}

- DELETE CLIENT (DELETE)
	http://127.0.0.1:5000/funnelbeam/client/<client_name>

- GET CLIENT BY NAME (GET).............(this will also return all projects of that client & employees in each project)
	http://127.0.0.1:5000/funnelbeam/client/<client_name>

- GET CLIENT (GET)
	http://127.0.0.1:5000//funnelbeam/client
**************************************************************************
*******************PROJECT*****************************
- ADD PROJECT (POST)
	http://127.0.0.1:5000/funnelbeam/project
	{
	   "project_id":1,
	   "project_name":"xyz"
	}

- EDIT PROJECT (PUT)
	http://127.0.0.1:5000/funnelbeam/project/<project_name>
	{
	   "project_name":"xyz"
	}

- DELETE PROJECT (DELETE)
	http://127.0.0.1:5000/funnelbeam/project/<project_name>

- GET PROJECT BY NAME (GET) ........(this will also return all employees of that project)
	http://127.0.0.1:5000//funnelbeam/project/<project_name>

- GET PROJECT (GET)
	http://127.0.0.1:5000/funnelbeam/project
**************************************************************************
*******************OTHER APIS*****************************
-ADD EMPLOYEE TO A PROJECT (PUT)
	http://127.0.0.1:5000/add_employee/<project_name>/<employee_name>

-REMOVE EMPLOYEE FROM A PROJECT (PUT)
	http://127.0.0.1:5000/remove_employee/<project_name>/<employee_name>

-ADD PROJECT TO A CLIENT (PUT)
	http://127.0.0.1:5000/add_project/<client_name>/<project_name>

-REMOVE PROJECT FROM A CLIENT (PUT)
	http://127.0.0.1:5000/remove_project/<client_name>/<project_name>


.......(celery runs automatically but in case to explicitly run celery).................
-CHECK UNASSIGNED EMPLOYEES (GET)
	http://127.0.0.1:5000/funnelbeam/check_employees
	





















