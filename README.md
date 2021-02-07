For deploying the backend server:
* have python and pip installed
* activate virtual environment
  source env/bin/activate
* install packages
  pip install -r requirements.txt
* make and apply migrations
  python app/manage.py makemigrations
  python app/manage.py migrate
* create superuser if not created already or if problem occours
  python app/manage.py createsuperuser
* run server
  python app/manage.py runserver 0.0.0.0:3000



The api list:

* localhost:3000/admin/
* localhost:3000/api/user/
* localhost:3000/api/user/create/
* localhost:3000/api/user/token/
* localhost:3000/api/user/me/
* localhost:3000/api/oj/problist/
* localhost:3000/api/oj/problist2/URI/
* localhost:3000/api/oj/problist2/UVA/
