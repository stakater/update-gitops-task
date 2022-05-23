
from git import Repo

import update_gitops_task.helpers as helpers

# Clone git repo
def git_clone(repo,dest,email,user,password=""):
   if(user!="" and password != ""):
        if repo.find("github") != -1: 
         index = repo.find("github")
        elif repo.find("gitlab") != -1:
          index = repo.find("gitlab")
        repo=repo[:index]+user+":"+password+"@"+repo[index:]
   print("Cloning Git repo....")
   cloned_repo=Repo.clone_from(repo,dest)
   cloned_repo.config_writer().set_value("user","name",user).release()
   cloned_repo.config_writer().set_value("user","email", email).release()
   print("done")
   return cloned_repo

#Update Chart file
def update_chart_file(path,version):     
     print("Updating chart version to "+ version +"....")
     update_yaml_file(path,["version"],version,False)
     update_yaml_file(path,["dependencies",0,"version"],version,False)
     print("done")

# Add index, commit and optional push
def git_commit(repo,message,push=False):
   try: 
    repo.git.add(repo.working_dir)
    repo.index.commit(message)
    if(push):
         print("Pushing repository...")
         origin = repo.remote(name='origin')
         origin.push()
         print("done")
   except Exception as e:
      print('Some error occured while pushing the code'+ e)

# Update key in yaml file at key located in location parameter
def update_yaml_file(path,location,value,log=True):
   data = helpers.get_yaml_data(path)
   helpers.set_in_dict(data,location,value)
   print("setting value of "+ ".".join(str(l) for l in location ) + " to "+ value + "..." ) if log else 0
   helpers.write_yaml(path,data)
   print("done") if log else 0

def get_tenant_by_namespace(namespace):
  index = namespace.find("-") 
  tenant = namespace[:index]
  return tenant

def key_exist(path, location): 
    data = helpers.get_yaml_data(path)
    for k in location:
       try:
          data = data[k]
       except:
           return False
    return True



