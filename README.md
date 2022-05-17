# update-gitops-task


## Util Functions

### git_clone

This function clone your git repository. it takes following parameters 

- repo: repo to clone (Required)
- user: username of git user for authentication
- password: password of git user for authentication

**Return:** Repo object

#### Example 
 ```
 repo = GitClone("https://github.com/hanzala1234/py-script-test-temp","/tmp/file-123","my_user","dummy_password")
```
### update_chart_file

This function update dependency and chart version of Chart.yaml. it takes following parameters

- path: path of ```Chart.yaml``` file (Required)
- version: Version of updated chart (Required)

**Return:** nil

#### Example
``` 
 UpdateChartFile(repo.working_dir+"/Chart.yaml","2.2.7")
```

#### Example
``` 
 SetGitConfig(repo,"user1","user1@gmail.com")
```

### update_yaml_file

This function update yaml file. it takes following parameters

- path: path of yaml file to read data from
- location: path to update
- value: value to be updated

#### Example
``` 
 UpdateYamlFile("01-gabbar/stakater-nordmart-review/01-dev/values.yaml",["deployment","image","tag"],"1.1.0")
```

**Return:**  nil 


### get_tenant_by_namespace

This function get tenant name by namespace if namespace is following <tenant>-<environment> convention. it takes following parameters

- namespace: Name of namespace


#### Example
``` 
 GetTenantByNamespace("gabbar-build")
```

**Return:**  tenant 