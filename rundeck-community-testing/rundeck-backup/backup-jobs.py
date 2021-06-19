#!/usr/bin/env python3

import json, requests, os

def main():
  # Load config:
  conf_file = open('backup-jobs-conf.json')
  conf_data = json.load(conf_file)
  conf_file.close()
  rundeck_url = conf_data["rd_url"]  
  
  # Get api token:
  api_token_file = open("rundeck-token")
  api_token = api_token_file.read().replace("\n", "")
  api_token_file.close()

  # Get list of projects:
  proj_list_url = f'{rundeck_url}/api/38/projects'
  proj_list_headers = {
    'X-Rundeck-Auth-Token': '',
    'Accept':'application/json',
  }
  proj_list_headers['X-Rundeck-Auth-Token'] = api_token
  projR = requests.get(proj_list_url, headers=proj_list_headers)
  proj_list_json = projR.json()

  # Extract list of project names:
  project_names = []
  for i in proj_list_json:    
    project_names.append(i.get("name"))

  # Ensure backup dir for each Project
  backup_dir_base = conf_data["bu_base_path"]
  for i in project_names:
    if not os.path.exists(os.path.join(backup_dir_base, i)):
      os.makedirs(os.path.join(backup_dir_base, i))

  # Export all jobs for a given project into a file called jobs.xml
  # e.g.: backup-base-dir/project-name/jobs.xml
  export_headers = {
      'X-Rundeck-Auth-Token': '',
      'Accept': 'application/xml'     
  }
  export_headers['X-Rundeck-Auth-Token'] = api_token  
  for proj_name in project_names:
    export_url = f'{rundeck_url}/api/38/project/{proj_name}/jobs/export'
    export_req = requests.get(export_url, headers=export_headers)     
    backup_file = open(os.path.join(backup_dir_base, proj_name, "jobs.xml"), 'wb')
    backup_file.write(export_req.content)
    backup_file.close()
    
if __name__ == "__main__":
    main()