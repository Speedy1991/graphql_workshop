# Exercise 1

Fix the [schema](https://github.com/Speedy1991/graphql_workshop/blob/master/graphql_workshop/settings.py#L55): `exercise1.schema.schema`

## 1) Write TypeDefs
- Open [types.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise1/schema/types.py)
- Fill the fields with the related scalar types

## 2) Write resolvers
- [query.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise1/schema/query.py)

## Questions

```
resolve_random_names(self, info, **kwargs):
    return ["Peter", "Paul", "Amy"]
    
resolve_number(self, info, **kwargs):
    return 5
```

Do you know the related field definitions?


## Sample

Query:
```
{
  students {
    id
    age
    name
    semester
  }
}
```

Result:

```
{
  "data": {
    "students": [
      {
        "id": "1",
        "age": 22,
        "name": "John",
        "semester": 1
      },
      {
        "id": "2",
        "age": 32,
        "name": "Ponnappa",
        "semester": 3
      },
      ...
```