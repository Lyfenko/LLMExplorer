import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from api.routes import auth, healthcheck, user

app = FastAPI(title="LLMExplorer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(healthcheck.route)
app.include_router(auth.router)
app.include_router(user.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
