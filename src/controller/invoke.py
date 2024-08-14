
import requests
from fastapi import Request, HTTPException
from fastapi.responses import StreamingResponse
from fastapi import APIRouter
from src.resolver.service_resolver import resolve_service

llm_invoke = APIRouter()

@llm_invoke.post("/gateway/{model_name}/{rest_of_path:path}")
async def gateway(model_name: str, 
                  rest_of_path: str, 
                  request: Request):
    payload = await request.json()
    try:
        headers = {
            "Content-Type": "application/json",
            "api-key": request.headers.get("api-key"),
            "x-api-key": request.headers.get("x-api-key"),
            "authorization": request.headers.get("authorization")
        }
        azure = resolve_service(model_name)
        response: requests.Response = await azure.chat_completion(
            payload=payload, 
            headers=headers,
            params=request.query_params
        )
        response.raise_for_status()
        if payload["stream"] == True:
             return StreamingResponse(response.iter_content(chunk_size=8192), headers=dict(response.headers))
        return response.json()
    except requests.exceptions.RequestException as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))