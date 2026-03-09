import sys
import os

# Make sure the project root is on the path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from starlette.applications import Starlette
from starlette.routing import Mount
from backend.app.main import app as fastapi_app

# Mount FastAPI at /api so Vercel's rewrite (/api/* → this file) works correctly.
# Starlette strips /api from the path before passing to FastAPI,
# so all existing routes (/habits/, /users/, etc.) continue to work unchanged.
app = Starlette(routes=[Mount("/api", app=fastapi_app)])
