from fastapi import FastAPI
import routes.user as init
import uvicorn


app = FastAPI()

app.include_router(init.api)

@app.get("/")
async def read_data():
    return {"msg":"Welcome"}

if __name__ == "__main__":
    uvicorn.run(app, host = '127.0.0.1',port = 8000)