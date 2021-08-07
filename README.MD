# pAWS | Dependency Checker - Pre-Commit Hook

<br/>

<p align="center">
  <img width="200" src="./static/logo.png">
</p>


<br/>
<br/>

An automated pre-commit hook which prompts and prevents developers from including vulnerable third-party dependencies in their application.

# Note

- The current script query from http://paws-backend.ap-southeast-2.elasticbeanstalk.com/threat/search. This maybe taken down hence please change line 18 in ```pre-commit.py``` from ```async with session.post('http://paws-backend.ap-southeast-2.elasticbeanstalk.com/threat/search',json={"package_manager_type" : "npm","package_list" : [package],"level": 0, "severity": ["CRITICAL"], "date": "None"}) as r:``` to 
```
async with session.post('http://127.0.0.1:5000/threat/search',json={"package_manager_type" : "npm","package_list" : [package],"level": 0, "severity": ["CRITICAL"], "date": "None"}) as r:
```
and ensure the backend located at https://github.com/UNSW-pAWS/webapp-backend is up and running before proceeding.
- If the api have not been changed please proceed to the section ```Original proceedures```.
- If the api have been changed please proceeed to the section ```Change proceedures```.
# Original proceedures.
## How to set up your environment or project repo (as a project manager)

1. head to root of your folder type 
```
npm init
``` 
and fill in the information

2. type 
```
git init
``` 
to initialise a git repo

3. head to package.json and enter the following into scripts (assuming all the developers are using linux)
```
"preinstall": "git clone https://github.com/UNSW-pAWS/pre-commit-hook.git && chmod +x ./pre-commit-hook/setup.sh && bash ./pre-commit-hook/setup.sh"
```

# For developer use on a local environment

1. git clone your project repo

2. run 
```
npm i
``` 
(preinstall script will run and setup your pre-commit hook on developer's local enviroment)

# Change proceedures