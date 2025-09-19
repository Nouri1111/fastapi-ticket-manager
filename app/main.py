from fastapi import FastAPI
from app.routers.ticket_router import router
from app.core.middleware import ProfilingMiddleware

app = FastAPI()

# Add middleware
app.add_middleware(ProfilingMiddleware)

# Include routers
app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "ok"}