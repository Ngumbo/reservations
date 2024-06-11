import uvicorn

from fastapi import FastAPI

from app.api.api_v1.routers.clients import clients_router


app = FastAPI(title="Reservations", docs_url="/api/docs", openapi_url="/api")


@app.get("/api/v1")
async def root():
    return {"message": "Hello World"}


# Routers
api_prefix = "/api/v1"
app.include_router(clients_router, prefix=api_prefix, tags=["clients"])


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8080)
