# HOW TO SETUP YOUR ENVIROMENT

1. head to root of your folder type ```npm init``` and fill in the information
2. type ```git init``` to initialise a git repo
3. head to package.json and enter the following into scripts ```"preinstall": "git clone https://github.com/UNSW-pAWS/pre-commit-hook.git && chmod +x ./pre-commit-hook/setup.sh && bash ./pre-commit-hook/setup.sh"```

# FOR DEVELOPER USE ON LOCAL ENVIROMENT

1. git clone your project repo
2. run ```npm i``` (preinstall script will run and setup your pre-commit hook on developer's local enviroment)