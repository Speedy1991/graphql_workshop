# Exercise 2

Fix the [schema](https://github.com/Speedy1991/graphql_workshop/blob/master/graphql_workshop/settings.py#L55): `exercise2.schema.schema`

## Problem
At the moment we can't query anything related (e.g. _modules_) on the _ProfessorType_


## TODO

- [types.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise2/schema/types.py)

## Questions

- What happens if a `favourite_module` is `None`? Can we enforce the field?
- How about Lists?


## Sample

Query:
```
{
  students {
    name
    favouriteModule {
      id
      name
    }
    modules {
      id
      name
    }
  }
}
```

Result:

```
{
  "data": {
    "students": [
      {
        "name": "John",
        "favouriteModule": {
          "id": "1",
          "name": "Math"
        },
        "modules": [
          {
            "id": "1",
            "name": "Math"
          },
          {
            "id": "3",
            "name": "Physics"
          }
        ]
      },
      ...
```