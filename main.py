from fastapi import FastAPI
import json

app = FastAPI()

# Load student marks from the JSON file
with open("q-vercel-python.json", "r") as f:
    data = json.load(f)

@app.get("/api")
async def get_marks(name: list[str]):
    marks = [data.get(n, None) for n in name]
    return {"marks": marks}

# Enable CORS
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_methods=["GET"],  # Allow only GET requests
    allow_headers=["*"],
)
