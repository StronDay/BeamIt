from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import main_route
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
    
   app.include_router(main_route)
   return app

app = create_app()