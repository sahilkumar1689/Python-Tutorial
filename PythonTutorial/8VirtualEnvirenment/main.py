# Steps to create the virtual environments:
# 1. Firstly install the virtualenv using command =  "pip install virtualenv" in your command prompt globally.If you install already skip it.
# 2. Secondly open one folder in your vscode where you want to create virtual environment.After that Change powershell to command prompt.Virtual environment only works on the cmd.
# 3. After that run command "python -m venv YourfolderName". e.g. = python -m venv .venv
# 4. After that run command "cd YourFolderName/Scripts".
# 5. After that simple run "activate".After running that command you can see the (venv) like symbol.
# 6. After that you are in your virtual environment install any package.
# 7. After that simpley run "pip freeze > requirements.txt".This command create a requirements.txt file which list all your installed packages.
# 8. In further if you want you can directly install all the dependencies listed in requirements file. "pip install -r requirements.txt".
# 9. If you wanna to come out from the virtual environment simple run "deactivate" command.