import uvicorn

if __name__ == "__main__":
    uvicorn.run("graphql_workshop.asgi:application", host="0.0.0.0", port=8000, lifespan='off', loop='asyncio', reload=True)
