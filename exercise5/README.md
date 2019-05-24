# Exercise 5

Fix the [schema](https://github.com/Speedy1991/graphql_workshop/blob/master/graphql_workshop/settings.py#L51): `exercise5.schema.schema`

## Mutations

Let's create some data!


## TODO

- Open [types.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise4/schema/types.py)
- Follow the TODO's in the file
- Fix [mutations/__init__.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise5/schema/mutations/__init__.py)

## Questions
What must be changed to get this mutation result?

```
{
  "data": {
    "addStudent": {
      "number": 5,
      "student": {
        ...
      }
    }
  }
}
```

## Sample

Mutation:
```
mutation {
  addStudent(age: 11, name: "amanda", semester: 1) {
    student {
      id
      name
      semester
    }
  }
}

```

Result:

```
{
  "data": {
    "addStudent": {
      "student": {
        "id": "13",
        "name": "amanda",
        "semester": "A_1"
      }
    }
  }
}
```