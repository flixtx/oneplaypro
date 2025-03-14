from fastapi import FastAPI, Request, Response
from fastapi.responses import JSONResponse, HTMLResponse
from jinja2 import Environment, FileSystemLoader
import encode_string
import canais
from vod import ondemand

templates = Environment(loader=FileSystemLoader("templates"))
app = FastAPI()

# addon do https://visioncine-1.com.br/
proxy_images_url = 'https://da5f663b4690-proxyimage.baby-beamup.club/proxy-image/?url='

manifest = {
    'id': 'app.com.oneplay',
    'version': '1.0.1',
    'name': 'OnePlay',
    "description": "Prepare a pipoca e divirta-se com o melhor do entretenimento",
    "logo": "https://i.imgur.com/WyZ8dSQ.png",
    "resources": ["catalog", "meta", "stream"],
    "types": ["tv", "movie", "series"],
    "idPrefixes": ["oneplay"],
    "catalogs": [
        {   # Catalogo de TV
            "id": "oneplay.tv", 
            "type": "tv", 
            "name": "OnePlay - TV ao vivo",
            "extra": [
                    {
                        "name": "genre",
                        "isRequired": False,
                        "options": [
                            "Canais Abertos",
                            "Variedades",
                            "Filmes e Series",
                            "Documentarios",
                            "Esportes",
                            "Infantil",
                            "Noticias"
                        ],
                        "optionsLimit": 1
                        
                    }
                ]
        },
        {   # Catalogo de Filmes
            "id": "oneplay.movies", 
            "type": "movie", 
            "name": "OnePlay - Filmes",
            "extra": [
                    {
                        "name": "genre",
                        "isRequired": False,
                        "options": [
                            "Filmes mais Vistos do Dia",
                            "Lançamentos",
                            "Filmes em Alta",
                            "Queridinhos",
                            "Família",
                            "Filmes Brasileiros"
                        ],
                        "optionsLimit": 1                        
                    },
                    {
                        "name": "search",
                        "isRequired": False,
                        "options": [],
                        "optionsLimit": 1
                    }                
                ]
        },
        {   # Catalogo de Series
            "id": "oneplay.series", 
            "type": "series", 
            "name": "OnePlay - Séries",
            "extra": [
                    {
                        "name": "genre",
                        "isRequired": False,
                        "options": [
                            "Séries mais Vistas do Dia",
                            "Lançamentos",
                            "Queridinhos",
                            "Doramas",
                            "Produções Brasileiras"
                        ],
                        "optionsLimit": 1
                        
                    },
                    {
                        "name": "search",
                        "isRequired": False,
                        "options": [],
                        "optionsLimit": 1
                    }                
                ]
        },
        {   # Catalogo de Animes
            "id": "oneplay.animes", 
            "type": "series", 
            "name": "OnePlay - Animes",
            "extra": [
                    {
                        "name": "genre",
                        "isRequired": False,
                        "options": [
                            "Animes mais Vistos do Dia",
                            "Lançamentos",
                            "Queridinhos",
                            "Clássicos"
                        ],
                        "optionsLimit": 1
                        
                    }               
                ]
        },
        {   # Catalogo de Doramas
            "id": "oneplay.doramas", 
            "type": "series", 
            "name": "OnePlay - Doramas",
            "extra": [
                    {
                        "name": "skip",
                        "isRequired": False,
                        "options": [],
                        "optionsLimit": 1
                    }                              
                ]
        }                                   
    ]
    }  

def add_cors(response: Response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    response.headers["Access-Control-Allow-Credentials"] = "true"
    return response 


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    template = templates.get_template("index.html")
    response = HTMLResponse(template.render(
        name=manifest['name'],
        types=manifest['types'],
        logo=manifest['logo'],
        description=manifest['description'],
        version=manifest['version']
    ))
    return add_cors(response)

@app.get("/manifest.json")
async def get_manifest(request: Request):
    return add_cors(JSONResponse(content=manifest))

# router tv
@app.get("/catalog/tv/"+manifest['catalogs'][0]['id']+"/genre={id}.json")
async def genres_tv(id: str, request: Request):
    server = proxy_images_url if proxy_images_url else ''
    canais_ = [canal for canal in canais.canais_list(server) if id in canal["genres"]]
    return add_cors(JSONResponse(content={"metas": canais_}))

# router tv
@app.get("/catalog/tv/{id}.json")
async def catalog_tv(id: str, request: Request):
    server = proxy_images_url if proxy_images_url else ''
    canais_ = [canal for canal in canais.canais_list(server)]
    return add_cors(JSONResponse(content={"metas": canais_}))

# router tv
@app.get("/meta/tv/{id}.json")
async def meta_tv(id: str, request: Request):
    server = proxy_images_url if proxy_images_url else ''
    meta_data = next((canal for canal in canais.canais_list(server) if canal["id"] == id), {})
    if meta_data:
        meta_data.pop("streams", None)
    return add_cors(JSONResponse(content={"meta": meta_data}))

# router movie
@app.get("/catalog/movie/"+manifest['catalogs'][1]['id']+"/genre={id}.json")
async def genres_movie(id: str, request: Request):
    catalog_m = ondemand().movies_catalog()
    catalog = [item for item in catalog_m if id in item["genres"]] if catalog_m else []
    return add_cors(JSONResponse(content={"metas": catalog}))

# router movie
@app.get("/catalog/movie/{id}.json")
async def catalog_movie(id: str, request: Request):
    global_catalog = []
    catalog_ = ondemand().movies_catalog()
    if catalog_:
        for m in catalog_:
            if not any(movie['id'] == m['id'] for movie in global_catalog):
                global_catalog.append(m)
    return add_cors(JSONResponse(content={"metas": global_catalog}))

# router movie
@app.get("/catalog/movie/"+manifest['catalogs'][1]['id']+"/skip={number}.json")
async def skip_movie(number: int, request: Request):
    global_catalog_movies = []  
    return add_cors(JSONResponse(content={"metas": global_catalog_movies}))

# router movie search
@app.get("/catalog/movie/"+manifest['catalogs'][1]['id']+"/search={key}.json")
async def search_movie(key: str, request: Request):
    catalog_movies = ondemand().get_search_movie(key)
    return add_cors(JSONResponse(content={"metas": catalog_movies}))

# router movie
@app.get("/meta/movie/{id}.json")
async def meta_movie(id: str, request: Request):
    meta_data = ondemand().get_meta_movie(id)
    return add_cors(JSONResponse(content={"meta": meta_data}))

# router series
@app.get("/catalog/series/"+manifest['catalogs'][2]['id']+"/genre={id}.json")
async def genres_series(id: str, request: Request):
    catalog_s = ondemand().series_catalog()
    catalog = [item for item in catalog_s if id in item["genres"]] if catalog_s else []
    return add_cors(JSONResponse(content={"metas": catalog}))

# router animes
@app.get("/catalog/series/"+manifest['catalogs'][3]['id']+"/genre={id}.json")
async def genres_animes(id: str, request: Request):
    catalog_s = ondemand().animes_catalog()
    catalog = [item for item in catalog_s if id in item["genres"]] if catalog_s else []
    return add_cors(JSONResponse(content={"metas": catalog}))

# router series
@app.get("/catalog/series/{id}.json")
async def catalog_series(id: str, request: Request):
    global_catalog = []
    if id == 'oneplay.series':
        catalog_ = ondemand().series_catalog()
        if catalog_:
            for s in catalog_:
                if not any(serie['id'] == s['id'] for serie in global_catalog):
                    global_catalog.append(s)
    elif id == 'oneplay.animes':
        catalog_ = ondemand().animes_catalog()
        if catalog_:
            for s in catalog_:
                if not any(serie['id'] == s['id'] for serie in global_catalog):
                    global_catalog.append(s)
    elif id == 'oneplay.doramas':
        catalog_ = ondemand().doramas_catalog(skip=0)
        if catalog_:
            for s in catalog_:
                if not any(serie['id'] == s['id'] for serie in global_catalog):
                    global_catalog.append(s)        
    return add_cors(JSONResponse(content={"metas": global_catalog}))

# router series
@app.get("/catalog/series/"+manifest['catalogs'][2]['id']+"/skip={number}.json")
async def skip_series(number: int, request: Request):
    global_catalog_series = []  
    return add_cors(JSONResponse(content={"metas": global_catalog_series}))

# router series search
@app.get("/catalog/series/"+manifest['catalogs'][2]['id']+"/search={key}.json")
async def search_series(key: str, request: Request):
    catalog_series = ondemand().get_search_serie(key)
    return add_cors(JSONResponse(content={"metas": catalog_series}))

# router doramas
@app.get("/catalog/series/"+manifest['catalogs'][4]['id']+"/skip={number}.json")
async def skip_doramas(number: int, request: Request):
    catalog_d = ondemand().doramas_catalog(skip=number) 
    return add_cors(JSONResponse(content={"metas": catalog_d}))

# router series
@app.get("/meta/series/{id}.json")
async def meta_movie(id: str, request: Request):
    meta_data = ondemand().get_meta_serie(id)
    return add_cors(JSONResponse(content={"meta": meta_data}))


@app.get("/stream/{type}/{id}.json")
async def stream(type: str, id: str, request: Request):
    server = proxy_images_url if proxy_images_url else ''
    if type == "tv":
        streams_ = []
        list_canais = canais.canais_list(server)
        for canal in list_canais:
            if canal['id'] == id:
                streams_ = canal['streams']              
                break
    elif type == "movie":
        streams_ = ondemand().get_stream_movie(id)
    elif type == 'series':
        streams_ = ondemand().get_stream_serie(id)
    else:
        streams_ = []
    return add_cors(JSONResponse(content={"streams": streams_}))

