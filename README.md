# pie
this is a project, where i try to create pie-chart on django-site.
## Start project
 > git clone https://github.com/jasketikus/pie.git

 > cd pie
## Instalation
1. install virtual environment 
> python -m venv venv
2. activate it
> ./venv/Scripts/activate
3. install requirements
> pip install -r requirements.txt
4. create .env file with:
> SECRET_KEY = your django key
> DEBUG = True
5. change directory to pieproject
> cd pieproject
6. migrate
> python manage.py migrate
7. now you can run server
> python manage.py runserver