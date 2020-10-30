# redis-decor
redis decorator for api or ui

# poc in windows machine
Note - I am using VS Code as IDE. Reason for that, it gives a simple way to debug and configure. No extra effort needed.

# check python version
py -3 --version

# how to create virtual env in windows machine
1. py -3 -m venv .venv
2. .venv\scripts\activate

# how to install redis in windows
python -m pip install redis

# Set policy to authorize to activate virtual environment
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process

# Not required. (specific with vscode IDE)
{workspace}/.venv/Scripts/Activate.ps1

# General notes:
1. Don't need to install redis server in windows machine
2. For testing purpose redis enterprise giving a facility of 30 days trial. Which is useful to test your change.
3. BOOM !
