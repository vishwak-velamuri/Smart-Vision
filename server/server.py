from fastapi import FastAPI
from .config.database import engine, SessionLocal
from .config.settings import settings
from .routes import user_routes, medication_routes, hazard_detection_routes

# Create the FastAPI app
app = FastAPI(title=settings.PROJECT_NAME, version=settings.VERSION)

# Include routers
app.include_router(user_routes.router)
app.include_router(medication_routes.router)
app.include_router(hazard_detection_routes.router)

# Dependency for getting a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Optional: Create database tables
@app.on_event("startup")
def startup_event():
    import app.models  # Ensure models are imported to create tables
    app.state.database = engine

@app.get("/")
def read_root():
    return {"message": "Welcome to Smart Vision API!"}
