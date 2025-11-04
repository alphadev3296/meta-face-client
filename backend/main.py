import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from backend.api.router import router as api_router
from backend.conf.app import config as cfg_app
from backend.conf.fs import config as cfg_fs

# Create FastAPI instance
app = FastAPI(
    debug=cfg_app.DEBUG,
    title=cfg_app.APP_TITLE,
    version=cfg_app.APP_VERSION,
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

# Mount static files
app.mount("/", StaticFiles(directory=cfg_fs.STATIC_DIR), name="static")

if __name__ == "__main__":
    uvicorn.run(
        "backend.main:app",
        reload=cfg_app.DEBUG,
        host="0.0.0.0",  # noqa: S104
        port=cfg_app.APP_PORT,
    )
