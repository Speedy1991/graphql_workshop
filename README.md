# Introduction to GraphQL and Graphene

## Workshop Outline
- _TypeDefs_
- _Query_
- _Mutation_
- _GraphQL Schema Language_
- _Concurrency_


#### System Requirements
- [git](https://git-scm.com/) v2 or greater
- [python3.5](https://www.python.org/downloads/) or greater + pip

#### Pre-Workshop Instructions/Requirements
- `git clone https://github.com:Speedy1991/graphql_workshop.git`
- `cd graphql-workshop`
- If you want to use a virtual environment click [here](https://virtualenv.pypa.io/en/stable/userguide/) for instructions 
- `pip install -r requirements.txt`
- `python manage.py migrate`
- `python manage.py loaddata`

#### Test your setup
- `python -v`
- `python manage.py runserver`
- Open your browser and visit `http://127.0.0.1:8000/admin` and try to login with `admin:12345`

This is the minimum workshop setup. Please prepare the project as describe above.

## Exercise overview
1) Write your first TypeDefs and resolvers
2) Extend your TypeDefs with more complex resolvers
3) Refactor with `django-graphene`
4) Write a custom resolver
    * Add Query Arguments
5) Write a mutation
6) Refactor
    * Replace mutation arguments with an _InputType_
    * Use _EnumType_
7) Some LiveCoding with AbstractTypes, Interfaces, Polymorphic, etc.

## Working through it
This is a very exercise-heavy workshop. You'll finde the exercises in the _graphql_workshop/exercise[number]_ directory.
Don't forget to change the used schema in the core settings (L51).

## Helpful shortcuts
- _TODO:_ This is **your** job
- _DOCS:_ This will give you a link to the specific doc page
- _DJANGO:_ This will help you with some django specific code
- _HINT:_ This will give you some useful tips
- _QUESTION:_ Try to answer the question yourself - if you don't find the answer, feel free to ask :)

## Django Cheatsheet
- `SELECT * FROM <table>` -> `<ModelName>.objects.all()`
- `SELECT * FROM <table> WHERE id=<id>` -> `<ModelName>.objects.get(id=id)` (raises if not exist)


#### License
This material is available for private, non-commercial use under the [GPL version 3](https://www.gnu.org/licenses/gpl-3.0-standalone.html).

If you would like to use this material to conduct your own workshop, please contact me at arthur.holz.91@gmail.com
