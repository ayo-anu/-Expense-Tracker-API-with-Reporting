from fastapi import FastAPI
from app.config import settings

def create_application()->FastAPI:
    application = FastAPI(
        title="Expense Tracker API",
        description="Multi-user expense tracking with reporting",
        version="1.0.0",
        docs_url="/docs",
        redoc_url="/redoc",
    )

    from app.api.v1.router import api_router
    application.include_router(api_router, prefix="/api/v1")

    return application

app = create_application()


@app.get("/health")
def health_check():
    return{
        "status":"ok",
        "environment":settings.APP_ENV
    }

for routes in app.routes:
    print(routes.path)