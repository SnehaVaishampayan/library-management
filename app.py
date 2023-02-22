#!/usr/bin/python

from flask import Flask, request, jsonify
from flask_cors import CORS
import json
from LoginModule.LoginHandler import is_user_authenticated
from database.DatabaseHandler import database_handler
from ProjectModule import ProjectHandler

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})


# 1•An API endpoint to o create a ProjectModule
@app.route('/api/project/add', methods=['POST'])
def api_add_user():
    response = []
    if is_user_authenticated(request.authorization):
        project_details = request.get_json()
        return jsonify(ProjectHandler.create_project(project_details, request.authorization['username']))
    else:
        response.append("Invalid user")
    return jsonify(response)


#  2•An API endpoint to get details about a specific ProjectModule
@app.route('/api/projects', methods=['GET'])
def api_get_projects():
    response = []
    if is_user_authenticated(request.authorization):
        if len(request.args) == 0:
            projects = ProjectHandler.get_projects_by_user_company(request.authorization['username'])
        else:
            projects = ProjectHandler.get_projects_by_filter(request.args)
        return jsonify(projects)
    else:
        response.append("Invalid user")
    return jsonify(response)


#  3•An API endpoint to list all the existing projects that belong to the user's company
@app.route('/api/projects/company', methods=['GET'])
def api_get_projects_by_company():
    response = []
    if is_user_authenticated(request.authorization):
        projects = ProjectHandler.get_projects_by_user_company(request.authorization['username'])
        return jsonify(projects)
    else:
        response.append("Invalid user")
    return jsonify(response)


# This function is responsible for starting the application
if __name__ == '__main__':
    print('In main app.py ')
    database_handler()
    app.config['JSON_SORT_KEYS'] = False
    app.run()
