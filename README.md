Prerequisite
=====
1. python3.6
2. virtualenv(or pyenv or any python virtual environment)
3. Docker(optional)

Installation Guide(Local with SQLite)
======
1. Make a new directory for the project and change into the directory.
```
mkdir <your-project-name>
cd <your-project-name>
```
2. Set up a virtual enviroment for the projet.
```
virtualenv <your-env-name>
# use -p flag to specify python executive file
virtualenv -p python3

# activate your virtual environment

# For Mac 
source <your-env-name>/bin/activate

# For Windows 
# I am not really familiar with windows. If you come to any trouble here,
# please refer to the virtualenv's document.
<your-env-name>\Scripts\activate.bat 
```
3. Clone the repository and change into the repository.
```
git clone git@github.com:Honesty1997/nccu-grade-system.git
cd nccu-grade-system
```
4. Install dependencies.
```
pip install -r requirements.txt
```
5. Init database.
```
python manage.py migrate
```
6. Start server.
```
python manage.py runserver
```
Open your browser and enter ```localhost:8080```, you should see your web service running.

Docker Solution
=====
The part is not completed yet. Please don't use this solution. If you want to use docker solution, after you start the compose service, you need to manually attach into the container's shell and run ```python manage.py migrate``` to init database.
1. ```make dev-up``` will start a new python web service along with a PostgreSQL sever.
2. ```make dev-build``` will build a image.