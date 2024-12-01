from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import users_routers
from app.routes import auth_routes

from .config import Config

def create_app():
   app = FastAPI()

   app.add_middleware(
      CORSMiddleware,
      allow_origins=["*"],
      allow_methods=["*"],
      allow_headers=["*"],
      allow_credentials=True,
   )
    
   app.include_router(users_routers)
   app.include_router(auth_routes)
   
   return app

app = create_app()