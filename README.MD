# pAWS | Dependency Checker - Pre-Commit Hook

<br/>

<p align="center">
  <img width="200" src="./static/logo.png">
</p>


<br/>
<br/>

An automated pre-commit hook which prompts and prevents developers from including vulnerable third-party dependencies in their application.

## How to set up your environment

1. head to root of your folder type ```npm init``` and fill in the information
2. type ```git init``` to initialise a git repo
3. head to package.json and enter the following into scripts ```"preinstall": "git clone https://github.com/UNSW-pAWS/pre-commit-hook.git && chmod +x ./pre-commit-hook/setup.sh && bash ./pre-commit-hook/setup.sh"```

# For developer use on a local environment

1. git clone your project repo
2. run ```npm i``` (preinstall script will run and setup your pre-commit hook on developer's local enviroment)