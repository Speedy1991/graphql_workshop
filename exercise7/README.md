# Exercise 7

Fix the [schema](https://github.com/Speedy1991/graphql_workshop/blob/master/graphql_workshop/settings.py#L55): `exercise7.schema.schema`

## Interfaces

Let's write our first interface

## TODO

- [query.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise7/schema/types.py)
- [types.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise7/schema/query.py)


## Sample

Query:
```
{
  persons {
    id
    name
    age
    __typename
    ... on StudentType {
      semester
      favouriteModule {
        id
        name
      }
    }
  }
}

```

Result:

```
{
  "data": {
    "persons": {
     ...
           {
        "id": "3",
        "name": "Prof. Emily",
        "age": "66",
        "__typename": "ProfessorType"
      },
      {
        "id": "1",
        "name": "John",
        "age": "22",
        "__typename": "StudentType",
        "semester": "FIRST",
        "favouriteModule": {
          "id": "1",
          "name": "Math"
        }
      },
      ...
    }
  }
}
```

# Question:
Why is it important to query the `__typename` in the interface?
