# Exercise 6

Fix the [schema](https://github.com/Speedy1991/graphql_workshop/blob/master/graphql_workshop/settings.py#L55): `exercise6.schema.schema`

## Mutations

Let's refactor the mutations!!


## TODO

- [create.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise6/schema/mutations/create.py)
- [input_types.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise6/schema/mutations/input_types.py)
- [types.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise6/schema/types.py)

## Questions
What are inputTypes good for?

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
  addStudent(studentInput: {name: "Paulaner", age: 22, semester: FIRST}) {
    student {
      name
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
        "name": "Paulaner"
      }
    }
  }
}
```