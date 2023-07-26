# Credential management in python

There are various ways to use credentials in python. The one which you should **never** ever do is store the credentials in naked text visible to everyone. Here we list all the possible ways to store / use credentials during development. 


## Using env variables
The most straight-forward way to store credentials is to make use of env variables of the operating system. Just set the variable using the OS interface (GUI or command line) and access it in python via the ```os``` package's ```getenv()``` function. 

```

```

## IDE specific - vscode integrated terminal
Use a launch.json in the .vscode folder
and update envs in the terminal.integrated.env.windows variable

Disadvantage: is IDE specific - might not work in prod env and needs other configs

## dotenv package

Install the python-dotenv package
create a '.env' file 
```
MY_USER=some_user
MY_PW=some_pw
```

```
from dotenv import load_dotenv
load_dotenv(dotenv_path=".vscode/my_creds.env")
print(os.getenv("MY_PW"))
# some_pw
```
Adv: is not IDE specific- can be used by everyone

## config.py file outside of PROJECT_ROOT
Keep a common ```config.py``` file in the user's home directory - something similar to a ```.bashrc``` or a ```.condarc``` file

Advantages: since the config.py is a python script, you can already encode the password using the base64 encoding library or any other library of python

## Using pydantic along with the above
Pydantic makes it really easy in retrieving credentials. 