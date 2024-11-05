from fastapi import FastAPI
from app.api.v1.ftool import router as ftool_router
app = FastAPI()

async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

# 注册 API 路由
app.include_router(ftool_router, prefix="/api/v1")  # 可以根据需要设置前缀

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)