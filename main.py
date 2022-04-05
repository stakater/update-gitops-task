
from git import Repo
import yaml
import re



def GitClone(repo,dest,user="",password=""):
   if(user!="" and password != ""):
         index = repo.find("github")
         repo=repo[:index]+user+":"+password+"@"+repo[index:]
   cloned_repo=Repo.clone_from(repo,dest)
   return cloned_repo
   


def UpdateChartFile(source,imageVersion):
     
     stream = open(source, 'r')
     data = yaml.load(stream,Loader=yaml.FullLoader)

     data["version"] = imageVersion 
     data["dependencies"][0]["version"] = imageVersion

     with open(source, 'w') as yaml_file:
        yaml_file.write( yaml.dump(data, default_flow_style=False))


def GitCommit(repo,message,push=False):
   try: 
    repo.git.add(update=True)
    repo.index.commit(message)
    if(push):
         origin = repo.remote(name='origin')
         origin.push()
   except:
      print('Some error occured while pushing the code') 



# repo = GitClone("https://github.com/hanzala1234/py-script-test-temp","/tmp/file-123","dummy_user","ghp_FlX0tsdfsfsdRLN1KfH6sO8ujuS0T961nt13Fg6pH")
# UpdateChartFile(repo.working_dir+"/Chart.yaml","2.2.5")
# GitCommit(repo,"Update chart file",True)

