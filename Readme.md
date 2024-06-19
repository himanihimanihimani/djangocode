venv 
__pycache__
.idea
.env


pip install django   #for installing the django only in this file.

django-admin startproject project . #it helps to create projectfolder
python manage.py startapp base #base is just app,this command helps to python manage.py runserver # this is for the checking the error in django project in seprate terminal


python manage.py migrate  #this command helps to create dtabasetable which is already in django file


pip freeze > requirements.txt # it creates a new file which shows what you downloaded packages

 pip install psycopg2-binary # it also helps to connect django file with postgrs


 pip install -r .\requirements.txt   # to install all package at once in requirements

