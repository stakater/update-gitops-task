
from git import Repo
import yaml
import re

# Clone git repo
def GitClone(repo,dest,email,user,password=""):
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
def UpdateChartFile(path,version):     
     print("Updating chart version to "+ version +"....")
     UpdateYamlFile(path,["version"],version,False)
     UpdateYamlFile(path,["dependencies",0,"version"],version,False)
     print("done")

# Add index, commit and optional push
def GitCommit(repo,message,push=False):
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

# Take dict data object and write it to yaml file
def WriteYaml(path,data):
  with open(path, 'w') as yaml_file:
     yaml_file.write( yaml.dump(data, default_flow_style=False))

# Get yaml data from yaml file specified in path parameter
def GetYamlData(path):
     stream = open(path, 'r')
     data = yaml.load(stream,Loader=yaml.FullLoader)
     return data


def setInDict(dataDict, mapList, value): 
    for k in mapList[:-1]: dataDict = dataDict[k]
    dataDict[mapList[-1]] = value


def UpdateYamlFile(path,location,value,log=True):
   data = GetYamlData(path)
   setInDict(data,location,value)
   print("setting value of "+ ".".join(str(l) for l in location ) + " to "+ value + "..." ) if log else 0
   WriteYaml(path,data)
   print("done") if log else 0

def GetTenantByNamespace(namespace):
  index = namespace.find("-") 
  tenant = namespace[:index]
  return tenant



