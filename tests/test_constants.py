result_query = "SELECT * FROM Project where name='fake_projectName'"

fake_filters = {"name": "fake_projectName"}
fake_project_details_valid = {"name": "fake_name", "description": "fake_desc", "status": "to do"}
fake_project_details_invalid_name = {"name": "fake_very_very_long_name", "description": "fake_desc", "status": "to do"}
fake_project_details_invalid_status = {"name": "fake_name", "description": "fake_desc", "status": "incorrect_status"}

error_msg_invalid_pName = 'Project details validation failed. Too long Project Name.'
error_msg_invalid_status = 'Project details validation failed. Invalid Status'


fake_result_query_data = 'result_query_data'
fake_result_commit = 'result_commit'