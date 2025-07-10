from fastapi import FastAPI
from routes import router
import uvicorn

app = FastAPI(title="AI Agent Router", version="1.0.0")

# Include routes
app.include_router(router)

@app.get("/")
async def root():
    return {"message": "AI Agent Router API", "status": "running"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
