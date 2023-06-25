from fastapi import FastAPI, Response

app = FastAPI()


@app.get("/no-cors")
async def no_cors_headers():
    return {"message": "You should not see an Access-Control-Allow-Origin header"}


@app.get("/with-cors")
async def with_cors_headers(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    return {"message": "You should see an Access-Control-Allow-Origin header"}

@app.get("/with-cors-https")
async def allow_only_https(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "https://*"
    return {"message": "only https://* is allowed"}

@app.get("/with-cors-tistory")
async def allow_only_tistory(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "https://*.tistory.com"
    return {"message": "only tistory sites is allowed"}
