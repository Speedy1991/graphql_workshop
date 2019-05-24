# Exercise 4

Fix the [schema](https://github.com/Speedy1991/graphql_workshop/blob/master/graphql_workshop/settings.py#L51): `exercise4.schema.schema`

## Query with Arguments and add custom fields

- In the last exercise we lost our `modules`
- We also can add Arguments to queries (e.g. filtering)

Example:
```
modules(startsWith: "Ma") {
  name
}
```


## TODO

- [types.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise4/schema/types.py)
- [query.py](https://github.com/Speedy1991/graphql_workshop/blob/master/exercise4/schema/query.py)

## Questions
- Why can't we use a DjangoObjectType on the main Query?
- Is this a valid query? Why? Why not?

```
students {
  name
  age
  modules(startsWith: "NotExistingSubject"){
    name
  }
}
```

## Sample

Query:
```
{
  modules(startsWith: "Ma") {
    id
    name
  }
}

```

Result:

```
{
  "data": {
    "modules": [
      {
        "id": "1",
        "name": "Math"
      }
    ]
  }
}
```