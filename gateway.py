from fastapi import FastAPI
from src.controller.invoke import llm_invoke

app = FastAPI()
    
app.include_router(llm_invoke)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

