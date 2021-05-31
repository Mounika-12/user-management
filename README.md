# user-management - Getting started
This is the code repository for Django, This repo will generate API's to do CRUD operations on users data.
Below steps are given under setup to run this sample Django application. This app uses a sqlite database by default. If you want to change this to use a specific database then configure DB in settings.py file.


## Following are the HTTP methods that can be performed on users.
* POST - http://localhost:port/users
* GET - http://localhost:port/users
* GET/{id} - http://localhost:port/users/{id}
* PUT/{id) - http://localhost:port/users/{id}
* PATCH/{id} - http://localhost:port/users/{id}
* DELETE/{id} - http://localhost:port/users/{id}

Also below added operations can be performed on users data

* Filtering  - http://localhost:port/users?{field_name}={value}
* Ordering - http://localhost:port/users?ordering={field_name}
* Searching - http://localhost:port/users?search={string}
* pagination - http://localhoost:port/users?limit={page_size}&offset={page}

## Setup

The first thing to do is to clone the repository and install the dependencies:

```sh
$ git clone https://github.com/Mounika-12/user-management.git
$ cd user_management
```
Once the depencies are installed using pip, Run the application using below command.

```sh
$ python manage.py runserver 0.0.0.0:port
```
Run the below commands to do migrations which inturn create tables in the DB.

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

## Swagger documentation

All the API's are documented uder swagger page. Once the appplication starts running launch the swagger url http://localhost:port/swagger to load API's documentaion page

