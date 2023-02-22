import sqlite3
import uuid
from datetime import datetime
import Constants
from Constants import CREATE_PROJECT, status_list, user_company
from database.CreateDatabase import get_cursor, connect_to_db


# This function is responsible for getting the list of projects assigned to the user's company.
def get_projects_by_user_company(logged_in_username):
    print("In get_projects ")
    projects = []
    try:
        cur = get_cursor()
        query_filter = {'company': user_company[logged_in_username]}
        cur.execute(get_query(query_filter))
        rows = cur.fetchall()

        for i in rows:
            project = {}
            project["id"] = i["id"]
            project["name"] = i["name"]
            project["description"] = i["description"]
            project["created"] = i["created"]
            project["updated"] = i["updated"]
            project["status"] = i["status"]
            project["creator"] = i["creator"]
            project["company"] = i["company"]
            projects.append(project)

    except Exception as e:
        print("Error occurred while getting ProjectModule details.", str(e))
        projects = []
    return projects


# This function is responsible for getting the list of projects given the specific project details.
def get_projects_by_filter(request_filter):
    print("In get_projects_by_filter ")
    projects = []
    try:
        if 'company' in request_filter.keys():
            get_projects_by_user_company(request_filter.get('company'))
        else:
            query = get_query(request_filter)
            cur = get_cursor()
            cur.execute(query)
            rows = cur.fetchall()
            for i in rows:
                project = {}
                project["id"] = i["id"]
                project["name"] = i["name"]
                project["description"] = i["description"]
                project["created"] = i["created"]
                project["updated"] = i["updated"]
                project["status"] = i["status"]
                project["creator"] = i["creator"]
                project["company"] = i["company"]
                projects.append(project)

    except Exception as e:
        print("Exception occurred while getting ProjectModule given ID. ", str(e))
        return projects
    return projects


# This function is responsible for building the query from the provided filters.
def get_query(filters):
    print("In get_query")
    query = Constants.GET_ALL_PROJECTS + " where "
    conditions = ""
    for eachFilterKey in filters.keys():
        if conditions == "":
            conditions += eachFilterKey + "=" + "'" + filters.get(eachFilterKey) + "'"
        else:
            conditions += " and " + eachFilterKey + "=" + "'" + filters.get(eachFilterKey) + "'"
    return query + "" + conditions


# This function is responsible for validation of the request payload while creating Project.
def validate_project_details(project_details):
    print("In validate_project_details")
    if len(project_details) != 3:
        raise Exception("Project details are missing.")
    for each_data in project_details:
        if each_data not in Constants.create_project_attributes:
            raise Exception("Incorrect data. Please provide Project Name, Project Description and Project Status")
    for each_data in project_details:
        if each_data.lower() == 'name':
            if len(project_details.get('name')) > 15:
                raise Exception("Project details validation failed. Too long Project Name.")

        if each_data.lower() == 'description':
            if len(project_details.get('description')) > 150:
                raise Exception("Project details validation failed. Too long description.")

        if each_data.lower() == 'status':
            if project_details.get('status').lower() not in status_list:
                raise Exception("Project details validation failed. Invalid Status")
    return True

# This function is responsible for creating the Project.
def create_project(project_details, login_username):
    print("In create_project ")
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        if not validate_project_details(project_details):
            raise Exception("Project Validation failed.")

        project_details['id'] = str(uuid.uuid4())
        project_details['created'] = datetime.now()
        project_details['updated'] = datetime.now()
        project_details['creator'] = login_username
        project_details['company'] = user_company[login_username]
        cur.execute(CREATE_PROJECT, (
            project_details['id'], project_details['name'], project_details['description'], project_details['created'],
            project_details['updated'], project_details['status'], project_details['creator'],
            project_details['company']))
        conn.commit()

    except Exception as e:
        print("Exception while creating ProjectModule." + str(e))
        conn().rollback()

    finally:
        conn.close()
    return project_details
