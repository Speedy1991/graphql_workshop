# Introduction to GraphQL and Graphene
## A workshop for PyconWeb 2019

#### Pre requirements
- python >= 3.6
- pip

#### Installation
- `git clone https://github.com/speedy1991/pyconweb2019graphql.git`
- `cd pyconweb2019graphql`
- If you want to use a virtual environment: https://virtualenv.pypa.io/en/stable/userguide/
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py loaddata`

#### Test if everything works fine:
- `python -v`
- `pip -v`
- `python manage.py runserver`
- Open your browser and visit `http://127.0.0.1:8000/admin` and try to login with `admin:12345`

This is the minimum workshop setup. Please prepare the project as describe above.

## Intro
- What are TypeDefs
- What is a Query
- What is a Mutation
- GraphQL Schema Language
- Concurrency


## Exercise 1
- Write your first TypeDefs and resolvers

## Exercise 2
- Extend your TypeDefs with more complex resolvers

## Exercise 3
- Refactor: use `django-graphene`

## Exercise 4
- Write a custom resolver
- Query Arguments

## Exercise 5
- Write a mutation
- Use the EnumType

## Exercise 6
- Refactor: replace arguments with an `InputType`

## Exercise 7 
- Refactor: clean up your code with 'AbstractType'

## Exercise 8
- Interfaces and Polymorphic


### License
This material is available for private, non-commercial use under the [GPL version 3](https://www.gnu.org/licenses/gpl-3.0-standalone.html).

If you would like to use this material to conduct your own workshop, please contact me at arthur.holz.91@gmail.com
