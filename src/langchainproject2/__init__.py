from fastapi import FastAPI

from .api.response_service import router as output_router
from .api.upload import router as upload_router
from .utils.load_env import load_env

# Initialize the FastAPI app
app = FastAPI()

# Load environment variables

load_env()


app.include_router(upload_router)
app.include_router(output_router)
