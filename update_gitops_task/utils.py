
from git import Repo
import yaml
import re

def GitClone(repo,dest,user="",password=""):
   if(user!="" and password != ""):
         index = repo.find("github")
         repo=repo[:index]+user+":"+password+"@"+repo[index:]
   cloned_repo=Repo.clone_from(repo,dest)
   return cloned_repo
   
def UpdateChartFile(path,version):
     
     data = getYamlData(path)
     data["version"] = version 
     data["dependencies"][0]["version"] = version

     WriteYaml(path,data)

def GitCommit(repo,message,push=False):
   try: 
    repo.git.add(update=True)
    repo.index.commit(message)
    if(push):
         origin = repo.remote(name='origin')
         origin.push()
   except:
      print('Some error occured while pushing the code')

def SetGitConfig(repo,user,email):
    repo.config_writer().set_value("user","name",user).release()
    repo.config_writer().set_value("user","email", email).release()

def WriteYaml(path,data):
      with open(path, 'w') as yaml_file:
        yaml_file.write( yaml.dump(data, default_flow_style=False))

def GetYamlData(path):
     stream = open(path, 'r')
     data = yaml.load(stream,Loader=yaml.FullLoader)
     return data
