
from git import Repo
import yaml
import re


def GitClone(repo,dest,user="",password=""):
   if(user!="" and password != ""):
         index = repo.find("github")
         repo=repo[:index]+user+":"+password+"@"+repo[index:]
   cloned_repo=Repo.clone_from(repo,dest)



def UpdateChartFile(source,imageVersion):
     
     stream = open(source, 'r')
     data = yaml.load(stream,Loader=yaml.FullLoader)

     data["version"] = imageVersion 
     data["dependencies"][0]["version"] = imageVersion

     with open(source, 'w') as yaml_file:
        yaml_file.write( yaml.dump(data, default_flow_style=False))


# UpdateChartFile("/home/hanzala/Public/stakater/stakater-nordmart-inventory/deploy/Chart.yaml","abcv-1.2.3")


# GitClone("https://github.com/stakater/update-gitops-task","/tmp/my-file","dummy-user","ghp_LajGx29I3Z9f9hAdZ7aRsdfdfUeRrUkUL1WNKIE")