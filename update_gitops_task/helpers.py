import yaml

# Take dict data object and write it to yaml file
def write_yaml(path,data):
  with open(path, 'w') as yaml_file:
     yaml_file.write( yaml.dump(data, default_flow_style=False))

# Get yaml data from yaml file specified in path parameter
def get_yaml_data(path):
     stream = open(path, 'r')
     data = yaml.load(stream,Loader=yaml.FullLoader)
     return data


def set_in_dict(dataDict, mapList, value): 
    for k in mapList[:-1]: dataDict = dataDict[k]
    dataDict[mapList[-1]] = value