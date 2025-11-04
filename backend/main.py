import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.router import router as api_router
from backend.conf.app import config as cfg_app

# Create FastAPI instance
app = FastAPI(
    debug=cfg_app.DEBUG,
    title=cfg_app.APP_TITLE,
    contact={
        "name": cfg_app.APP_NAME,
        "url": str(cfg_app.APP_URL),
        "email": str(cfg_app.APP_EMAIL),
    },
    on_startup=[],
)

# Add middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(api_router, prefix="/api")

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        reload=cfg_app.DEBUG,
        host="0.0.0.0",  # noqa: S104
        port=cfg_app.APP_PORT,
    )
