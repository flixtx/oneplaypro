from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
import requests
from typing import Dict

# Inicializa o aplicativo FastAPI
app = FastAPI()

# Manifesto do addon
manifest = {
    "id": "com.meuteste.m3u8",
    "version": "1.0.0",
    "name": "Teste M3U8 Addon",
    "description": "Addon para testar URLs M3U8 no Stremio",
    "resources": ["stream"],
    "types": ["movie", "series"],
    "catalogs": []
}

# Função para adicionar headers CORS manualmente
def add_cors_headers(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET"
    response.headers["Access-Control-Allow-Headers"] = "*"
    return response

# Rota para o manifesto
@app.get("/manifest.json")
async def get_manifest():
    response = JSONResponse(content=manifest)
    return add_cors_headers(response)

# Rota para streams
@app.get("/stream/{media_type}/{media_id}.json")
async def get_stream(media_type: str, media_id: str):
    # URL M3U8 de teste - substitua pela sua URL
    m3u8_url = "https://sinalprivado.info/m3u8/MQ==/dnotYzIwYTAxMGMtYTk4/M2NmZGNjMDEtODk2NC00YTBjLTk0NmItYzAyNjZjZjhhMWNm.m3u8"
    
    try:
        # Verifica se a URL M3U8 é válida
        # response = requests.head(m3u8_url, timeout=5)
        # if response.status_code != 200:
        #     raise Exception("URL M3U8 inválida")

        # Resposta com o stream
        stream_data = {
            "streams": [{
                "url": m3u8_url,
                "title": "Teste M3U8",
            }]
        }
        response = JSONResponse(content=stream_data)
        return add_cors_headers(response)
    
    except Exception as e:
        error_response = {"error": f"Erro ao processar a URL M3U8: {str(e)}"}
        response = JSONResponse(content=error_response, status_code=500)
        return add_cors_headers(response)

# Inicia o servidor (rodar com uvicorn)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)