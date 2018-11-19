[![Build Status](https://travis-ci.org/Deekerubo/Store-Manager-API.svg?branch=develop)](https://travis-ci.org/Deekerubo/Store-Manager-API)
[![Maintainability](https://api.codeclimate.com/v1/badges/b856b0a4882e0f62f42b/maintainability)](https://codeclimate.com/github/Deekerubo/Store-Manager-API/maintainability)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Coverage Status](https://coveralls.io/repos/github/Deekerubo/Store-Manager-API/badge.svg?branch=ch-add-readMe-161500877)](https://coveralls.io/github/Deekerubo/Store-Manager-API?branch=ch-add-readMe-161500877)

# Store-Manager-API
Store Manager is a web application that helps store owners manage sales and product inventory records. This application is meant for use in a single store.
The API is hosted [here](https://storemanger2-api.herokuapp.com/)<br>
The UI is hosted [here](https://deekerubo.github.io/Store-Manager/UI/)<br>

# Prerequisites
-[Python3](https://www.python.org/) (A programming language).<br>
-[Flask](ht-[Python3](https://www.python.org/) (A programming language).<br>
-[Flask](http://flask.pocoo.org/) (A Python microframework).<br>
-[PostgreSQL](http://www.postgresqltutorial.com/) (Database)
-[Virtualenv](https://virtualenv.pypa.io/en/latest/) (Stores all dependencies used in the project)
-[Pivotal Tracker](https://www.pivotaltracker.com/dashboard) (A project management tool)
-[Pytest](https://docs.pytest.org/en/latest/) (Framework for testing)tp://flask.pocoo.org/) (A Python microframework).
-[PostgreSQL](http://www.postgresqltutorial.com/) (Database)
-[Virtualenv](https://virtualenv.pypa.io/en/latest/) (Stores all dependencies used in the project)
-[Pivotal Tracker](https://www.pivotaltracker.com/dashboard) (A project management tool)
-[Pytest](https://docs.pytest.org/en/latest/) (Framework for testing)

# Required Features
```
-Store attendant can search and add products to buyer’s cart.
-Store attendant can see his/her sale records but can’t modify them.
-App should show available products, quantity and price.
-Store owner can see sales and can filter by attendants.
-Store owner can add, modify and delete products.
-Store owner can give admin rights to a store attendant.
-Products should have categories.
-Store attendants should be able to add products to specific catego
```
# Installation
Clone this Repository.
```
    $ git clone https://github.com/Deekerubo/Store-Manager-API.git
```
Create the virtual Environment
```
    $ virtualenv venv
```
Activate the virtual environment
```
    $ . venv/bin/activate
```
Install all the requirements
```
    $ pip install -r requirements.txt
```
View all Endpoints hosted on Heroku:
    `https://storemanger2-api.herokuapp.com/`
Run my version 2 testS
`python -m pytest --cov=app/tests/v2'

#Endpoints

EndPoint | Functionality | Notes
---------|---------------|-------
POST /products | Create a product|
GET /products | Fetch all products | 
GET /products/<productId> | Fetch a single product record|
PUT /products | Modify a Product|
DELETE /products | Delete a product|
GET /sales|  Fetch all sale records| 
GET /sales/<saleId> | Fetch a single sale record|
POST /sales | Create a sale order|
PUT /sales | Modify a sale|
DELETE /sales | Delete a sale|



export ENV="development"
export ENV='testing'

python -m pytest --cov=app/api/v2

pytest --cov-report term-missing --cov=app/api/v2