# Exercise 3

Fix the [schema](https://github.com/Speedy1991/graphql_workshop/blob/master/graphql_workshop/settings.py#L55): `exercise3.schema.schema`

## Refactor

We have a lot of boilerplate code - it has to be easier!!


## TODO

- [types.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise3/schema/types.py)

## Questions
- Why can't we use a DjangoObjectType on the main Query?
- What worst cases could happen if you don't limit the fields via `only_fields` or `exclude_fields`?
- Why is `only_fields` better than `exclude_fields`? (IMO)
- Why didn't we implement everything with `django_graphene` from the beginning?


## Sample

Query:
```
{
  students {
    name
    age
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
        "name": "John",
        "age": 22,
        "semester": "A_1"
      },
      {
        "name": "Ponnappa",
        "age": 32,
        "semester": "A_3"
      },
      ...
```