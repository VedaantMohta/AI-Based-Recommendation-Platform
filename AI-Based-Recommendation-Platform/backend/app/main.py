from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.routes_users import router as users_router
from app.api.routes_items import router as items_router
from app.api.routes_recos import router as recos_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this as needed for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/users", tags=["users"])
app.include_router(items_router, prefix="/items", tags=["items"])
app.include_router(recos_router, prefix="/recommendations", tags=["recommendations"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the RecoHub API!"}