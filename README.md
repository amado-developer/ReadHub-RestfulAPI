# ReadHub API

Restful API for our React-Native / Redux project for the web course. UVG 2020

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

Things you need to install the software and how to install them

```
Clone or download repository https://github.com/amado-developer/ReadHub-RestfulAPI.git
```
```
Create a data base in postgres named ReadHub
```

### Installing

A step by step series of examples that tell you how to get a development env running

**Configure Data base:**\
This would be possible by changing the DATABASES dictionary. Normally you only have to change the password\
**Direction of document:** Your-Directory\ReadHub-RestfulAPI\ReadHub\settings.py


```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'ReadHub',
        'USER': 'postgres',
        'PASSWORD': 'Anikalinda11',
        'HOST' : 'localhost',
        'PORT' : '5432',

    }
}

```

**Create a python3 virtual enviroment**

```
virtualenv env
```

If you have any problem you can see this documentation:\
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/

**Activate your virtual enviroment in your terminal from the path where you have the project**

```
source env/bin/activate
```
Install all the requirements needed
```
pip3 install -r requirements.txt 
```
**Make migrations**

```
python3 manage.py makemigations
```
```
python3 manage.py migrate
```
**Initialize data for the data base**

```
python manage.py shell < initialize.py
```
## Run server
```
python3 manage.py runserver
```



## Authors

* **Amado Garcia** -  - [amado-developer](https://github.com/amado-developer)
* **Sara Zavala** -  - [saritazavala](https://github.com/saritazavala)




## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details







