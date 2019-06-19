# API
A REST API for creating and managing user accounts made with Django.

# Technologies Used 

 - Django = 2.2.2
 - djangorestframework = 3.9.4
 - djangorestframework-jwt = 1.11.0
 - Python = 3.6+

# How to use

Download the files in your comupter then run  ```pip install -r requirements.txt``` This will download all the required dependencies in your system. 

Next navigate to the API-master directory where the ```manage.py``` scrpit exists. 

Run ```python manage.py runserver``` this will start the django's built in devlopment server, now in your browser go the address http://127.0.0.1:8000/user/signup/ and this is what you should see.

![image](https://user-images.githubusercontent.com/38559396/59752103-5b41b900-929f-11e9-95fd-38e66ab56e71.png)

Using this browsable API you can create a user providing the valid data in the given fields and hitting the POST button this will return a json object of the user along with the **user id**


Navigate to http://127.0.0.1:8000/user/login/ here you have to provide the username and password of a valid user this view will return a **JWT-token** in return of a successful call. 

![image](https://user-images.githubusercontent.com/38559396/59752513-018dbe80-92a0-11e9-90c8-267dcd9d26fd.png)
