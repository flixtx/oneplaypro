import requests
import re
from urllib.parse import quote_plus, quote
from bs4 import BeautifulSoup
import base64

def canais_list(server):
    canais = [
    {
        "id": "oneplay:globosp",
        "type": "tv",
        "name": "Globo SP",
        "poster": f"{server}https://embehub.com/img/globo.png",
        "background": f"{server}https://embehub.com/img/globo.png",
        "description": "Canal Globo SP ao vivo.",
        "genres": ["Canais Abertos"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/globosp/video.m3u8",
                "title": "Globo SP",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:globoba",    
        "type": "tv",
        "name": "Globo BA",
        "poster": f"{server}https://embehub.com/img/globo.png",
        "background": f"{server}https://embehub.com/img/globo.png",
        "description": "Canal Globo BA ao vivo.",
        "genres": ["Canais Abertos"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/globoba/video.m3u8",
                "title": "Globo BA",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:sbtsp", 
        "type": "tv",
        "name": "SBT SP",
        "poster": f"{server}https://embehub.com/img/thumb-sbt.jpg",
        "background": f"{server}https://embehub.com/img/thumb-sbt.jpg",
        "description": "Canal SBT ao vivo.",
        "genres": ["Canais Abertos"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/sbtsp/video.m3u8",
                "title": "SBT SP",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:bandsp",       
        "type": "tv",
        "name": "BAND SP",
        "poster": f"{server}https://embehub.com/img/thumb-band.jpg",
        "background": f"{server}https://embehub.com/img/thumb-band.jpg",
        "description": "Canal BAND ao vivo.",
        "genres": ["Canais Abertos"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/bandsp/video.m3u8",
                "title": "BAND SP",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:redetv",      
        "type": "tv",
        "name": "REDE TV",
        "poster": f"{server}https://embehub.com/img/thumb-redetv.jpg",
        "background": f"{server}https://embehub.com/img/thumb-redetv.jpg",
        "description": "Canal REDE TV ao vivo.",
        "genres": ["Canais Abertos"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/redetv/video.m3u8",
                "title": "REDE TV",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:tvbrasil",
        "type": "tv",
        "name": "TV BRASIL",
        "poster": f"{server}https://embehub.com/img/thumb-tvbrasil.jpg",
        "background": f"{server}https://embehub.com/img/thumb-tvbrasil.jpg",
        "description": "Canal TV BRASIL ao vivo.",
        "genres": ["Canais Abertos"],
        "streams": [
            {
                "url": "https://tvbrasil-stream.ebc.com.br/EBC_HD-avc1_900000=10003.m3u8",
                "title": "TV BRASIL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedmax.site",
                            "Referer": "https://embedmax.site/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:futura",
        "type": "tv",
        "name": "FUTURA",
        "poster": f"{server}https://embehub.com/img/thumb-futura.png",
        "background": f"{server}https://embehub.com/img/thumb-futura.png",
        "description": "Canal FUTURA ao vivo.",
        "genres": ["Canais Abertos"],
        "streams": [
            {
                "url": "https://play.embehub.com/FUTURA/index.fmp4.m3u8",
                "title": "FUTURA",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/FUTURA/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:recordsp",
        "type": "tv",
        "name": "RECORD SP",
        "poster": f"{server}https://embehub.com/img/thumb-record.jpg",
        "background": f"{server}https://embehub.com/img/thumb-record.jpg",
        "description": "Canal RECORD SP ao vivo.",
        "genres": ["Canais Abertos"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/recordsp/video.m3u8",
                "title": "RECORD SP",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:viva",
        "rc": {"token": "c0hIM0JOdlZVRk1mRVRoWDNFaGw=", "channel": "viva"},
        "type": "tv",
        "name": "VIVA",
        "poster": f"{server}https://embehub.com/img/thumb-viva.jpg",
        "background": f"{server}https://embehub.com/img/thumb-viva.jpg",
        "description": "Canal VIVA ao vivo.",
        "genres": ["Variedades"],
        "streams": [
            {
                "url": "",
                "title": "VIVA",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:bis",
        "rc": {"token": "c0hIM0JOdlZWMVFZRnpoRDNFMD0=", "channel": "bis"},
        "type": "tv",
        "name": "BIS",
        "poster": f"{server}https://embehub.com/img/biz.png",
        "background": f"{server}https://embehub.com/img/biz.png",
        "description": "Canal BIS ao vivo.",
        "genres": ["Variedades"],
        "streams": [
            {
                "url": "",
                "title": "BIS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:gnt",
        "type": "tv",
        "name": "GNT",
        "poster": f"{server}https://embehub.com/img/gnt.jpg",
        "background": f"{server}https://embehub.com/img/gnt.jpg",
        "description": "Canal GNT ao vivo.",
        "genres": ["Variedades"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/gnt/video.m3u8",
                "title": "GNT",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:multishow",
        "type": "tv",
        "name": "MULTISHOW",
        "poster": f"{server}https://embehub.com/img/multishow.png",
        "background": f"{server}https://embehub.com/img/multishow.png",
        "description": "Canal MULTISHOW ao vivo.",
        "genres": ["Variedades"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/multishow/video.m3u8",
                "title": "MULTISHOW",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:off",
        "rc": {"token": "c0hIM0JOdlVXRk1jRlRoTzAxZz0=", "channel": "off"},
        "type": "tv",
        "name": "Canal OFF",
        "poster": f"{server}https://embehub.com/img/canaloff.webp",
        "background": f"{server}https://embehub.com/img/canaloff.webp",
        "description": "Canal OFF ao vivo.",
        "genres": ["Variedades"],
        "streams": [
            {
                "url": "",
                "title": "Canal OFF",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:adultswim",
        "type": "tv",
        "name": "ADULT SWIM",
        "poster": f"{server}https://embehub.com/img/thumb-adultswim.jpg",
        "background": f"{server}https://embehub.com/img/thumb-adultswim.jpg",
        "description": "Canal ADULT SWIM ao vivo.",
        "genres": ["Variedades"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/adultswim/video.m3u8",
                "title": "MULTISHOW",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:amc",
        "type": "tv",
        "name": "AMC",
        "poster": f"{server}https://embehub.com/img/AMC.jpg",
        "background": f"{server}https://embehub.com/img/AMC.jpg",
        "description": "Canal AMC ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/amc/video.m3u8",
                "title": "AMC",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:animalplanet",
        "type": "tv",
        "name": "ANIMAL PLANET",
        "poster": f"{server}https://embehub.com/img/thumb-animalplanet.jpg",
        "background": f"{server}https://embehub.com/img/thumb-animalplanet.jpg",
        "description": "Canal ANIMAL PLANET ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/animalplanet/video.m3u8",
                "title": "ANIMAL PLANET",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:arte1",
        "rc": {"token": "c0hIM0JOdmVWVllkRVRoQXgwcGhzUT09", "channel": "arte1"}, 
        "type": "tv",
        "name": "ARTE 1",
        "poster": f"{server}https://embehub.com/img/thumb-arte1.jpg",
        "background": f"{server}https://embehub.com/img/thumb-arte1.jpg",
        "description": "Canal ARTE 1 ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "",
                "title": "ARTE 1",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:axn",
        "type": "tv",
        "name": "AXN",
        "poster": f"{server}https://embehub.com/img/thumb-axn.jpg",
        "background": f"{server}https://embehub.com/img/thumb-axn.jpg",
        "description": "Canal AXN ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/axn/video.m3u8",
                "title": "AXN",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:canalbrasil",
        "rc": {"token": "c0hIM0JOdmZVbG9kRlRoQzFGQmw3Q1haaHM1NkR3PT0=", "channel": "canalbrasil"},
        "type": "tv",
        "name": "Canal BRASIL",
        "poster": f"{server}https://embehub.com/img/thumb-canalbrasil.jpg",
        "background": f"{server}https://embehub.com/img/thumb-canalbrasil.jpg",
        "description": "Canal BRASIL ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "",
                "title": "Canal BRASIL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:discoverychannel",
        "type": "tv",
        "name": "DISCOVERY CHANNEL",
        "poster": f"{server}https://embehub.com/img/thumb-discovery.jpg",
        "background": f"{server}https://embehub.com/img/thumb-discovery.jpg",
        "description": "Canal DISCOVERY CHANNEL ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/discoverychannel/video.m3u8",
                "title": "DISCOVERY CHANNEL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:discoveryheh",
        "type": "tv",
        "name": "DISCOVERY HOME & HEALTH",
        "poster": f"{server}https://embehub.com/img/thumb-discoveryhomeihealth.jpg",
        "background": f"{server}https://embehub.com/img/thumb-discoveryhomeihealth.jpg",
        "description": "Canal DISCOVERY HOME & HEALTH ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/discoveryhh/video.m3u8",
                "title": "DISCOVERY HOME & HEALTH",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:discoveryturbo",
        "type": "tv",
        "name": "DISCOVERY TURBO",
        "poster": f"{server}https://embehub.com/img/discoveryturbo.png",
        "background": f"{server}https://embehub.com/img/discoveryturbo.png",
        "description": "Canal DISCOVERY TURBO ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/discoveryturbo/video.m3u8",
                "title": "DISCOVERY TURBO",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:discoverytheater",
        "type": "tv",
        "name": "DISCOVERY THEATER",
        "poster": f"{server}https://embehub.com/img/discoverytheather.webp",
        "background": f"{server}https://embehub.com/img/discoverytheather.webp",
        "description": "Canal DISCOVERY THEATER ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/discoverytheater/video.m3u8",
                "title": "DISCOVERY THEATER",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:discoveryworld",
        "type": "tv",
        "name": "DISCOVERY WORLD",
        "poster": f"{server}https://embehub.com/img/discoveryworld.png",
        "background": f"{server}https://embehub.com/img/discoveryworld.png",
        "description": "Canal DISCOVERY WORLD ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/discoveryworld/video.m3u8",
                "title": "DISCOVERY WORLD",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:discoveryscience",
        "type": "tv",
        "name": "DISCOVERY SCIENCE",
        "poster": "https://static.wikia.nocookie.net/logopedia/images/6/63/Discovery_Science_LA_2011.png",
        "background": "https://static.wikia.nocookie.net/logopedia/images/6/63/Discovery_Science_LA_2011.png",
        "description": "Canal DISCOVERY SCIENCE ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/discoveryscience/video.m3u8",
                "title": "DISCOVERY SCIENCE",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:fx",
        "type": "tv",
        "name": "FX",
        "poster": f"{server}https://embehub.com/img/thumb-fx.jpg",
        "background": f"{server}https://embehub.com/img/thumb-fx.jpg",
        "description": "Canal FX ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/fx/video.m3u8",
                "title": "FX",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:hbo",
        "type": "tv",
        "name": "HBO",
        "poster": f"{server}https://embehub.com/img/thumb-hbo.jpg",
        "background": f"{server}https://embehub.com/img/thumb-hbo.jpg",
        "description": "Canal HBO ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/hbo/video.m3u8",
                "title": "HBO",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:hbo2",
        "type": "tv",
        "name": "HBO 2",
        "poster": f"{server}https://embehub.com/img/thumb-hbo2.jpg",
        "background": f"{server}https://embehub.com/img/thumb-hbo2.jpg",
        "description": "Canal HBO 2 ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/hbo2/video.m3u8",
                "title": "HBO 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:hbofamily",
        "type": "tv",
        "name": "HBO FAMILY",
        "poster": f"{server}https://embehub.com/img/thumb-hbofamily.jpg",
        "background": f"{server}https://embehub.com/img/thumb-hbofamily.jpg",
        "description": "Canal HBO FAMILY ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/hbofamily/video.m3u8",
                "title": "HBO FAMILY",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:hboplus",
        "type": "tv",
        "name": "HBO PLUS",
        "poster": f"{server}https://embehub.com/img/thumb-hboplus.jpg",
        "background": f"{server}https://embehub.com/img/thumb-hboplus.jpg",
        "description": "Canal HBO PLUS ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/hboplus/video.m3u8",
                "title": "HBO PLUS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:hboxtreme',
        'type': 'tv',
        'name': 'HBO XTREME',
        'poster': f"{server}https://embehub.com/img/hboextreme.webp",
        'background': f"{server}https://embehub.com/img/hboextreme.webp",
        'description': 'Canal HBO XTREME ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/hboxtreme/video.m3u8",
                'title': "HBO XTREME",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:hbosignature',
        'type': 'tv',
        'name': 'HBO SIGNATURE',
        'poster': "https://simg.nicepng.com/png/small/233-2333073_hbo-signature-latin-atlansia-hbo-signature-logo-png.png",
        'background': "https://simg.nicepng.com/png/small/233-2333073_hbo-signature-latin-atlansia-hbo-signature-logo-png.png",
        'description': 'Canal HBO SIGNATURE ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/hbosignature/video.m3u8",
                'title': "HBO SIGNATURE",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:hbopop',
        'type': 'tv',
        'name': 'HBO POP',
        'poster': "https://embedcanaistv.com/player3/imgs-videos/Canais/hbopop.jpg",
        'background': "https://embedcanaistv.com/player3/imgs-videos/Canais/hbopop.jpg",
        'description': 'Canal HBO POP ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/hbopop/video.m3u8",
                'title': "HBO POP",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },    
    {
        'id': 'oneplay:history',
        'type': 'tv',
        'name': 'HISTORY',
        'poster': f"{server}https://embehub.com/img/thumb-history.jpg",
        'background': f"{server}https://embehub.com/img/thumb-history.jpg",
        'description': 'Canal HISTORY ao vivo.',
        'genres': ['Documentarios'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/history/video.m3u8",
                'title': "HISTORY",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:history2',
        'type': 'tv',
        'name': 'HISTORY 2',
        'poster': f"{server}https://embehub.com/img/thumb-history2.jpg",
        'background': f"{server}https://embehub.com/img/thumb-history2.jpg",
        'description': 'Canal HISTORY 2 ao vivo.',
        'genres': ['Documentarios'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/history2/video.m3u8",
                'title': "HISTORY 2",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:mtv',
        'type': 'tv',
        'name': 'MTV',
        'poster': f"{server}https://embehub.com/img/thumb-mtv.jpg",
        'background': f"{server}https://embehub.com/img/thumb-mtv.jpg",
        'description': 'Canal MTV ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/mtv/video.m3u8",
                'title': "MTV",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:nationalgeographic',
        'type': 'tv',
        'name': 'NATIONAL GEOGRAPHIC',
        'poster': f"{server}https://embehub.com/img/thumb-natgeo.jpg",
        'background': f"{server}https://embehub.com/img/thumb-natgeo.jpg",
        'description': 'Canal NATIONAL GEOGRAPHIC ao vivo.',
        'genres': ['Documentarios'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/nationalgeografic/video.m3u8",
                'title': "NATIONAL GEOGRAPHIC",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:paramountnetwork',
        "rc": {"token": "c0hIM0JOdmVVMUFmR3poUjFFeGw3U2plaWNrPQ==", "channel": "paramount"},
        'type': 'tv',
        'name': 'PARAMOUNT NETWORK',
        'poster': f"{server}https://embehub.com/img/thumb-paramount.jpg",
        'background': f"{server}https://embehub.com/img/thumb-paramount.jpg",
        'description': 'Canal PARAMOUNT NETWORK ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "",
                'title': "PARAMOUNT NETWORK",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com/",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:space',
        'type': 'tv',
        'name': 'SPACE',
        'poster': f"{server}https://embehub.com/img/thumb-space.jpg",
        'background': f"{server}https://embehub.com/img/thumb-space.jpg",
        'description': 'Canal SPACE ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/space/video.m3u8",
                'title': "SPACE",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:tnt',
        'type': 'tv',
        'name': 'TNT',
        'poster': f"{server}https://embehub.com/img/thumb-tnt.jpg",
        'background': f"{server}https://embehub.com/img/thumb-tnt.jpg",
        'description': 'Canal TNT ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tnt/video.m3u8",
                'title': "TNT",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:tntseries',
        'type': 'tv',
        'name': 'TNT SERIES',
        'poster': f"{server}https://embedcanaistv.com/player3/imgs-videos/Canais/tntseries.jpg",
        'background': f"{server}https://embedcanaistv.com/player3/imgs-videos/Canais/tntseries.jpg",
        'description': 'Canal TNT SERIES ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tntseries/video.m3u8",
                'title': "TNT SERIES",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:tntnovelas',
        'type': 'tv',
        'name': 'TNT NOVELAS',
        'poster': f"{server}https://embedcanaistv.com/player3/imgs-videos/Canais/tntnovelas.jpg",
        'background': f"{server}https://embedcanaistv.com/player3/imgs-videos/Canais/tntnovelas.jpg",
        'description': 'Canal TNT NOVELAS ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tntnovelas/video.m3u8",
                'title': "TNT NOVELAS",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },         
    {
        'id': 'oneplay:telecineaction',
        'type': 'tv',
        'name': 'TELECINE ACTION',
        'poster': f"{server}https://embehub.com/img/thumb-telecineaction.jpg",
        'background': f"{server}https://embehub.com/img/thumb-telecineaction.jpg",
        'description': 'Canal TELECINE ACTION ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tcaction/video.m3u8",
                'title': "TELECINE ACTION",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:telecinecult',
        'type': 'tv',
        'name': 'TELECINE CULT',
        'poster': f"{server}https://embehub.com/img/thumb-telecinecult.jpg",
        'background': f"{server}https://embehub.com/img/thumb-telecinecult.jpg",
        'description': 'Canal TELECINE CULT ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tccult/video.m3u8",
                'title': "TELECINE CULT",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:telecinefun',
        'type': 'tv',
        'name': 'TELECINE FUN',
        'poster': f"{server}https://embehub.com/img/thumb-telecinefun.jpg",
        'background': f"{server}https://embehub.com/img/thumb-telecinefun.jpg",
        'description': 'Canal TELECINE FUN ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tcfun/video.m3u8",
                'title': "TELECINE FUN",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:telecinepipoca',
        'type': 'tv',
        'name': 'TELECINE PIPOCA',
        'poster': f"{server}https://embehub.com/img/thumb-telecinepipoca.jpg",
        'background': f"{server}https://embehub.com/img/thumb-telecinepipoca.jpg",
        'description': 'Canal TELECINE PIPOCA ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tcpipoca/video.m3u8",
                'title': "TELECINE PIPOCA",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:telecinepremium',
        'type': 'tv',
        'name': 'TELECINE PREMIUM',
        'poster': f"{server}https://embehub.com/img/thumb-telecinepremium.jpg",
        'background': f"{server}https://embehub.com/img/thumb-telecinepremium.jpg",
        'description': 'Canal TELECINE PREMIUM ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tcpremium/video.m3u8",
                'title': "TELECINE PREMIUM",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:telecinetouch',
        'type': 'tv',
        'name': 'TELECINE TOUCH',
        'poster': f"{server}https://embehub.com/img/thumb-telecinetouch.jpg",
        'background': f"{server}https://embehub.com/img/thumb-telecinetouch.jpg",
        'description': 'Canal TELECINE TOUCH ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/tctouch/video.m3u8",
                'title': "TELECINE TOUCH",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:universal',
        'type': 'tv',
        'name': 'UNIVERSAL TV',
        'poster': f"{server}https://embehub.com/img/thumb-universal.jpg",
        'background': f"{server}https://embehub.com/img/thumb-universal.jpg",
        'description': 'Canal UNIVERSAL ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/universaltv/video.m3u8",
                'title': "UNIVERSAL TV",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:syfy',
        'type': 'tv',
        'name': 'SYFY',
        'poster': f"{server}https://embehub.com/img/syfy.jpg",
        'background': f"{server}https://embehub.com/img/syfy.jpg",
        'description': 'Canal SYFY ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://play.embehub.com/SYFY/index.fmp4.m3u8",
                'title': "SYFY",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Referer': "https://play.embehub.com/SYFY/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:cinemax',
        'type': 'tv',
        'name': 'CINEMAX',
        'poster': f"{server}https://embehub.com/img/thumb-cinemax.jpg",
        'background': f"{server}https://embehub.com/img/thumb-cinemax.jpg",
        'description': 'Canal CINEMAX ao vivo.',
        'genres': ['Filmes e Series'],
        'streams': [
            {
                'url': "https://embedcanaistv.live/cinemax/video.m3u8",
                'title': "CINEMAX",
                'behaviorHints': {
                    'notWebReady': True,
                    'proxyHeaders': {
                        'request': {
                            'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            'Origin': "https://embedcanaistv.com",
                            'Referer': "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:comedycentral",       
        "type": "tv",
        "name": "COMEDY CENTRAL",
        "poster": f"{server}https://embehub.com/img/thumb-comedycentral.jpg",
        "background": f"{server}https://embehub.com/img/thumb-comedycentral.jpg",
        "description": "Canal COMEDY CENTRAL ao vivo.",
        "genres": ["Variedades"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/comedycentral/video.m3u8",
                "title": "COMEDY CENTRAL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:sony",
        "type": "tv",
        "name": "SONY CHANNEL",
        "poster": f"{server}https://embehub.com/img/thumb-sony.jpg",
        "background": f"{server}https://embehub.com/img/thumb-sony.jpg",
        "description": "SONY CHANNEL ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/sonychannel/video.m3u8",
                "title": "SONY CHANNEL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:sonymovies",
        "rc": {"token": "c0hIM0JOdmZXRm9ZR3poUzJsQjk3U2pkanRoZw==", "channel": "sonymovies"},
        "type": "tv",
        "name": "SONY MOVIES",
        "poster": f"{server}https://embedcanaistv.com/player3/imgs-videos/Canais/sonymovies.jpg",
        "background": f"{server}https://embedcanaistv.com/player3/imgs-videos/Canais/sonymovies.jpg",
        "description": "SONY MOVIES ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "",
                "title": "SONY MOVIES",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },    
    {
        "id": "oneplay:starchannel",
        "type": "tv",
        "name": "STAR CHANNEL",
        "poster": f"{server}https://embehub.com/img/thumb-starchannel.jpg",
        "background": f"{server}https://embehub.com/img/thumb-starchannel.jpg",
        "description": "STAR CHANNEL ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/starchannel/video.m3u8",
                "title": "STAR CHANNEL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:warnertv",
        "type": "tv",
        "name": "WARNER TV",
        "poster": f"{server}https://embehub.com/img/thumb-warner.jpg",
        "background": f"{server}https://embehub.com/img/thumb-warner.jpg",
        "description": "Canal WARNER TV ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/warner/video.m3u8",
                "title": "WARNER TV",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:aie",
        "type": "tv",
        "name": "A&E",
        "poster": f"{server}https://embehub.com/img/A&E_Network_logo.png",
        "background": f"{server}https://embehub.com/img/A&E_Network_logo.png",
        "description": "Canal A&E ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/aee/video.m3u8",
                "title": "A&E",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:investigacao",
        "type": "tv",
        "name": "INVESTIGAÇÃO DISCOVERY",
        "poster": f"{server}https://embehub.com/img/iddiscovery.jpeg",
        "background": f"{server}https://embehub.com/img/iddiscovery.jpeg",
        "description": "Canal INVESTIGAÇÃO DISCOVERY ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/discoveryid/video.m3u8",
                "title": "INVESTIGAÇÃO DISCOVERY",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:tlc",
        "type": "tv",
        "name": "TLC",
        "poster": f"{server}https://embehub.com/img/discoverytlc.png",
        "background": f"{server}https://embehub.com/img/discoverytlc.png",
        "description": "Canal TLC ao vivo.",
        "genres": ["Documentarios"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/tlc/video.m3u8",
                "title": "TLC",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:megapix",
        "type": "tv",
        "name": "MEGAPIX",
        "poster": f"{server}https://embehub.com/img/megapix.jpg",
        "background": f"{server}https://embehub.com/img/megapix.jpg",
        "description": "Canal MEGAPIX ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/megapix/video.m3u8",
                "title": "MEGAPIX",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:studiouniversal",
        "type": "tv",
        "name": "STUDIO UNIVERSAL",
        "poster": f"{server}https://embehub.com/img/universalstudios.png",
        "background": f"{server}https://embehub.com/img/universalstudios.png",
        "description": "Canal STUDIO UNIVERSAL ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/studiouniversal/video.m3u8",
                "title": "STUDIO UNIVERSAL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:lifetime",
        "type": "tv",
        "name": "LIFETIME",
        "poster": f"{server}https://i.ibb.co/jGXbx1x/lifetime.jpg",
        "background": f"{server}https://i.ibb.co/jGXbx1x/lifetime.jpg",
        "description": "Canal LIFETIME ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/lifetime/video.m3u8",
                "title": "LIFETIME",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:cinecanal",
        "rc": {"token": "c0hIM0JOdmVVMU1kR3poQzNGQmg0eWJGaHRFPQ==", "channel": "cinecanal"},
        "type": "tv",
        "name": "CINE CANAL",
        "poster": f"{server}https://seeklogo.com/images/C/Cinecanal-logo-C68A0CF747-seeklogo.com.png",
        "background": f"{server}https://seeklogo.com/images/C/Cinecanal-logo-C68A0CF747-seeklogo.com.png",
        "description": "CINE Canal ao vivo.",
        "genres": ["Filmes e Series"],
        "streams": [
            {
                "url": "",
                "title": "CINE CANAL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:eentertainment",
        "rc": {"token": "c0hIM0JOdlZWVllmRnpoQzFGQmw3Q0k9", "channel": "canale"},
        "type": "tv",
        "name": "!E",
        "poster": f"{server}https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/E%21_Logo.svg/1200px-E%21_Logo.svg.png",
        "background": f"{server}https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/E%21_Logo.svg/1200px-E%21_Logo.svg.png",
        "description": "Canal !E ao vivo.",
        "genres": ["Variedades"],
        "streams": [
            {
                "url": "",
                "title": "!E",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:amazonprime",
        "type": "tv",
        "name": "AMAZON PRIME",
        "poster": f"{server}https://igormiranda.com.br/wp-content/uploads/2024/02/amazon-prime-logo-696x364.jpg",
        "background": f"{server}https://igormiranda.com.br/wp-content/uploads/2024/02/amazon-prime-logo-696x364.jpg",
        "description": "Canal AMAZON PRIME ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/amazonprimevideo/video.m3u8",
                "title": "AMAZON PRIME",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },    
    {
        "id": "oneplay:bandsports",
        "type": "tv",
        "name": "BANDSPORTS",
        "poster": f"{server}https://embehub.com/img/thumb-bandsports.jpg",
        "background": f"{server}https://embehub.com/img/thumb-bandsports.jpg",
        "description": "Canal BANDSPORTS ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/bandsports/video.m3u8",
                "title": "BANDSPORTS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:espn",
        "type": "tv",
        "name": "ESPN",
        "poster": f"{server}https://embehub.com/img/thumb-espn.jpg",
        "background": f"{server}https://embehub.com/img/thumb-espn.jpg",
        "description": "Canal ESPN ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/espn/video.m3u8",
                "title": "ESPN",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:espn2",
        "type": "tv",
        "name": "ESPN 2",
        "poster": f"{server}https://embehub.com/img/thumb-espn2.jpg",
        "background": f"{server}https://embehub.com/img/thumb-espn2.jpg",
        "description": "Canal ESPN 2 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/espn2/video.m3u8",
                "title": "ESPN 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:espn3",
        "type": "tv",
        "name": "ESPN 3",
        "poster": f"{server}https://embehub.com/img/thumb-espn3.jpg",
        "background": f"{server}https://embehub.com/img/thumb-espn3.jpg",
        "description": "Canal ESPN 3 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/espn3/video.m3u8",
                "title": "ESPN 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:espn4",
        "type": "tv",
        "name": "ESPN 4",
        "poster": f"{server}https://embehub.com/img/thumb-espn4.jpg",
        "background": f"{server}https://embehub.com/img/thumb-espn4.jpg",
        "description": "Canal ESPN 4 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/espn4/video.m3u8",
                "title": "ESPN 4",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:espn5",
        "type": "tv",
        "name": "ESPN 5",
        "poster": f"{server}https://embehub.com/img/thumb-espn5.jpg",
        "background": f"{server}https://embehub.com/img/thumb-espn5.jpg",
        "description": "Canal ESPN 5 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/espn5/video.m3u8",
                "title": "ESPN 5",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:espn6",
        "type": "tv",
        "name": "ESPN 6",
        "poster": f"{server}https://embehub.com/img/thumb-espn6.jpg",
        "background": f"{server}https://embehub.com/img/thumb-espn6.jpg",
        "description": "Canal ESPN 6 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/espn6/video.m3u8",
                "title": "ESPN 6",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:sportv",
        "type": "tv",
        "name": "SPORTV",
        "poster": f"{server}https://embehub.com/img/thumb-sportv1.jpg",
        "background": f"{server}https://embehub.com/img/thumb-sportv1.jpg",
        "description": "Canal SPORTV ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/sportv/video.m3u8",
                "title": "SPORTV",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:sportv2",
        "type": "tv",
        "name": "SPORTV 2",
        "poster": f"{server}https://embehub.com/img/thumb-sportv2.jpg",
        "background": f"{server}https://embehub.com/img/thumb-sportv2.jpg",
        "description": "Canal SPORTV 2 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/sportv2/video.m3u8",
                "title": "SPORTV 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:sportv3",
        "type": "tv",
        "name": "SPORTV 3",
        "poster": f"{server}https://embehub.com/img/thumb-sportv3.jpg",
        "background": f"{server}https://embehub.com/img/thumb-sportv3.jpg",
        "description": "Canal SPORTV 3 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/sportv3/video.m3u8",
                "title": "SPORTV 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:premiereclubes",
        "type": "tv",
        "name": "PREMIERE CLUBES",
        "poster": f"{server}https://embehub.com/img/thumb-premiereclubes.jpg",
        "background": f"{server}https://embehub.com/img/thumb-premiereclubes.jpg",
        "description": "Canal PREMIERE CLUBES ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/premiereclubes/video.m3u8",
                "title": "PREMIERE CLUBES",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:premiere2",
        "type": "tv",
        "name": "PREMIERE 2",
        "poster": f"{server}https://embehub.com/img/thumb-premiere2.jpg",
        "background": f"{server}https://embehub.com/img/thumb-premiere2.jpg",
        "description": "Canal PREMIERE 2 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/premiere2/video.m3u8",
                "title": "PREMIERE 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:premiere3",
        "type": "tv",
        "name": "PREMIERE 3",
        "poster": f"{server}https://embehub.com/img/thumb-premiere3.jpg",
        "background": f"{server}https://embehub.com/img/thumb-premiere3.jpg",
        "description": "Canal PREMIERE 3 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/premiere3/video.m3u8",
                "title": "PREMIERE 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:premiere4",
        "type": "tv",
        "name": "PREMIERE 4",
        "poster": f"{server}https://embehub.com/img/thumb-premiere4.jpg",
        "background": f"{server}https://embehub.com/img/thumb-premiere4.jpg",
        "description": "Canal PREMIERE 4 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/premiere4/video.m3u8",
                "title": "PREMIERE 4",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:premiere5",
        "type": "tv",
        "name": "PREMIERE 5",
        "poster": f"{server}https://embehub.com/img/thumb-premiere5.jpg",
        "background": f"{server}https://embehub.com/img/thumb-premiere5.jpg",
        "description": "Canal PREMIERE 5 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/premiere5/video.m3u8",
                "title": "PREMIERE 5",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:premiere6",
        "type": "tv",
        "name": "PREMIERE 6",
        "poster": f"{server}https://embehub.com/img/thumb-premiere6.jpg",
        "background": f"{server}https://embehub.com/img/thumb-premiere6.jpg",
        "description": "Canal PREMIERE 6 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/premiere6/video.m3u8",
                "title": "PREMIERE 6",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:premiere7",       
        "type": "tv",
        "name": "PREMIERE 7",
        "poster": f"{server}https://embehub.com/img/thumb-premiere7.jpg",
        "background": f"{server}https://embehub.com/img/thumb-premiere7.jpg",
        "description": "Canal PREMIERE 7 ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/premiere7/video.m3u8",
                "title": "PREMIERE 7",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        "id": "oneplay:paramountplus",
        "type": "tv",
        "name": "PARAMOUNT+",
        "poster": f"{server}https://embehub.com/img/thumb-paramountplus1.jpg",
        "background": f"{server}https://embehub.com/img/thumb-paramountplus1.jpg",
        "description": "Canal PARAMOUNT+ ao vivo.",
        "genres": ["Esportes"],
        "streams": [
            {
                "url": "https://embedcanaistv.live/paramountplus/video.m3u8",
                "title": "PARAMOUNT+",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:paramountplus2',
        'type': 'tv',
        'name': 'PARAMOUNT+ 2',
        'poster': f"{server}https://embehub.com/img/thumb-paramountplus2.jpg",
        'background': f"{server}https://embehub.com/img/thumb-paramountplus2.jpg",
        'description': 'Canal PARAMOUNT+ 2 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/PARAMOUNT+2/index.fmp4.m3u8",
                "title": "PARAMOUNT+ 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/PARAMOUNT+2/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:paramountplus3',
        'type': 'tv',
        'name': 'PARAMOUNT+ 3',
        'poster': f"{server}https://embehub.com/img/thumb-paramountplus3.jpg",
        'background': f"{server}https://embehub.com/img/thumb-paramountplus3.jpg",
        'description': 'Canal PARAMOUNT+ 3 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/PARAMOUNT+3/index.fmp4.m3u8",
                "title": "PARAMOUNT+ 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/PARAMOUNT+3/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:paramountplus4',
        'type': 'tv',
        'name': 'PARAMOUNT+ 4',
        'poster': f"{server}https://embehub.com/img/thumb-paramountplus4.jpg",
        'background': f"{server}https://embehub.com/img/thumb-paramountplus4.jpg",
        'description': 'Canal PARAMOUNT+ 4 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/PARAMOUNT+4/index.fmp4.m3u8",
                "title": "PARAMOUNT+ 4",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/PARAMOUNT+4/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:combate',
        'type': 'tv',
        'name': 'COMBATE',
        'poster': f"{server}https://embehub.com/img/thumb-combate.jpg",
        'background': f"{server}https://embehub.com/img/thumb-combate.jpg",
        'description': 'Canal COMBATE ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://embedcanaistv.live/combate/video.m3u8",
                "title": "COMBATE",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:cazetv1',
        'type': 'tv',
        'name': 'CAZE TV 1',
        'poster': f"{server}https://embehub.com/img/cazetv.png",
        'background': f"{server}https://embehub.com/img/cazetv.png",
        'description': 'Canal CAZE TV 1 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://embedcanaistv.live/cazetv/video.m3u8",
                "title": "CAZE TV 1",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:cazetv2',
        'type': 'tv',
        'name': 'CAZE TV 2',
        'poster': f"{server}https://embehub.com/img/cazetv.png",
        'background': f"{server}https://embehub.com/img/cazetv.png",
        'description': 'Canal CAZE TV 2 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/CAZETV2/index.fmp4.m3u8",
                "title": "CAZE TV 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/CAZETV2/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:cazetv3',
        'type': 'tv',
        'name': 'CAZE TV 3',
        'poster': f"{server}https://embehub.com/img/cazetv.png",
        'background': f"{server}https://embehub.com/img/cazetv.png",
        'description': 'Canal CAZE TV 3 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/CAZETV3/index.fmp4.m3u8",
                "title": "CAZE TV 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/CAZETV3/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:goat1',
        'type': 'tv',
        'name': 'Canal GOAT 1',
        'poster': f"{server}https://embehub.com/img/canalgoat.jpg",
        'background': f"{server}https://embehub.com/img/canalgoat.jpg",
        'description': 'Canal GOAT 1 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/CANALGOAT1/index.fmp4.m3u8",
                "title": "Canal GOAT 1",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/CANALGOAT1/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:goat2',
        'type': 'tv',
        'name': 'Canal GOAT 2',
        'poster': f"{server}https://embehub.com/img/canalgoat.jpg",
        'background': f"{server}https://embehub.com/img/canalgoat.jpg",
        'description': 'Canal GOAT 2 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/CANALGOAT2/index.fmp4.m3u8",
                "title": "Canal GOAT 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/CANALGOAT2/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:goat3',
        'type': 'tv',
        'name': 'Canal GOAT 3',
        'poster': f"{server}https://embehub.com/img/canalgoat.jpg",
        'background': f"{server}https://embehub.com/img/canalgoat.jpg",
        'description': 'Canal GOAT 3 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/CANALGOAT3/index.fmp4.m3u8",
                "title": "Canal GOAT 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/CANALGOAT3/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:goat4',
        'type': 'tv',
        'name': 'Canal GOAT 4',
        'poster': f"{server}https://embehub.com/img/canalgoat.jpg",
        'background': f"{server}https://embehub.com/img/canalgoat.jpg",
        'description': 'Canal GOAT 4 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/CANALGOAT4/index.fmp4.m3u8",
                "title": "Canal GOAT 4",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/CANALGOAT4/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:ufcfightpass1',
        'type': 'tv',
        'name': 'UFC FIGHT PASS 1',
        'poster': f"{server}https://embehub.com/img/thumb-ufcfightpass.jpg",
        'background': f"{server}https://embehub.com/img/thumb-ufcfightpass.jpg",
        'description': 'Canal UFC FIGHT PASS 1 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/UFCFIGHTPASS1/index.fmp4.m3u8",
                "title": "UFC FIGHT PASS 1",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/UFCFIGHTPASS1/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:ufcfightpass2',
        'type': 'tv',
        'name': 'UFC FIGHT PASS 2',
        'poster': f"{server}https://embehub.com/img/thumb-ufcfightpass.jpg",
        'background': f"{server}https://embehub.com/img/thumb-ufcfightpass.jpg",
        'description': 'Canal UFC FIGHT PASS 2 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/UFCFIGHTPASS2/index.fmp4.m3u8",
                "title": "UFC FIGHT PASS 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/UFCFIGHTPASS2/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:ufcfightpass3',
        'type': 'tv',
        'name': 'UFC FIGHT PASS 3',
        'poster': f"{server}https://embehub.com/img/thumb-ufcfightpass.jpg",
        'background': f"{server}https://embehub.com/img/thumb-ufcfightpass.jpg",
        'description': 'Canal UFC FIGHT PASS 3 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/UFCFIGHTPASS3/index.fmp4.m3u8",
                "title": "UFC FIGHT PASS 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/UFCFIGHTPASS3/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:disneyplus1',
        'type': 'tv',
        'name': 'DISNEY+ 1',
        'poster': f"{server}https://embehub.com/img/disney+.png",
        'background': f"{server}https://embehub.com/img/disney+.png",
        'description': 'Canal DISNEY+ 1 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DISNEY+1/index.fmp4.m3u8",
                "title": "DISNEY+ 1",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DISNEY+1/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:disneyplus2',
        'type': 'tv',
        'name': 'DISNEY+ 2',
        'poster': f"{server}https://embehub.com/img/disney+.png",
        'background': f"{server}https://embehub.com/img/disney+.png",
        'description': 'Canal DISNEY+ 2 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DISNEY+2/index.fmp4.m3u8",
                "title": "DISNEY+ 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DISNEY+2/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:disneyplus3',
        'type': 'tv',
        'name': 'DISNEY+ 3',
        'poster': f"{server}https://embehub.com/img/disney+.png",
        'background': f"{server}https://embehub.com/img/disney+.png",
        'description': 'Canal DISNEY+ 3 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DISNEY+3/index.fmp4.m3u8",
                "title": "DISNEY+ 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DISNEY+3/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:disneyplus4',
        'type': 'tv',
        'name': 'DISNEY+ 4',
        'poster': f"{server}https://embehub.com/img/disney+.png",
        'background': f"{server}https://embehub.com/img/disney+.png",
        'description': 'Canal DISNEY+ 4 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DISNEY+4/index.fmp4.m3u8",
                "title": "DISNEY+ 4",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DISNEY+4/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:disneyplus5',
        'type': 'tv',
        'name': 'DISNEY+ 5',
        'poster': f"{server}https://embehub.com/img/disney+.png",
        'background': f"{server}https://embehub.com/img/disney+.png",
        'description': 'Canal DISNEY+ 5 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DISNEY+5/index.fmp4.m3u8",
                "title": "DISNEY+ 5",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DISNEY+5/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:disneyplus6',
        'type': 'tv',
        'name': 'DISNEY+ 6',
        'poster': f"{server}https://embehub.com/img/disney+.png",
        'background': f"{server}https://embehub.com/img/disney+.png",
        'description': 'Canal DISNEY+ 6 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DISNEY+6/index.fmp4.m3u8",
                "title": "DISNEY+ 6",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DISNEY+6/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:eventosextra',
        'type': 'tv',
        'name': 'EVENTOS EXTRAS',
        'poster': "https://i.ibb.co/JFXgB2D/OIP.jpg",
        'background': "https://i.ibb.co/JFXgB2D/OIP.jpg",
        'description': 'Canal EVENTOS EXTRAS ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/Eventos_Extras_01/index.fmp4.m3u8",
                "title": "EVENTOS EXTRAS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/Eventos_Extras_01/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:dazn1',
        'type': 'tv',
        'name': 'DAZN 1',
        'poster': f"{server}https://embehub.com/img/Danz.png",
        'background': f"{server}https://embehub.com/img/Danz.png",
        'description': 'Canal DAZN 1 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DAZN_1/index.fmp4.m3u8",
                "title": "DAZN 1",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DAZN_1/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:dazn2',
        'type': 'tv',
        'name': 'DAZN 2',
        'poster': f"{server}https://embehub.com/img/Danz.png",
        'background': f"{server}https://embehub.com/img/Danz.png",
        'description': 'Canal DAZN 2 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://panel.embehub.com/DAZN_2/index.fmp4.m3u8",
                "title": "DAZN 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://panel.embehub.com/DAZN_2/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:dazn3',
        'type': 'tv',
        'name': 'DAZN 3',
        'poster': f"{server}https://embehub.com/img/Danz.png",
        'background': f"{server}https://embehub.com/img/Danz.png",
        'description': 'Canal DAZN 3 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DAZN_3/index.fmp4.m3u8",
                "title": "DAZN 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DAZN_3/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:dazn4',
        'type': 'tv',
        'name': 'DAZN 4',
        'poster': f"{server}https://embehub.com/img/Danz.png",
        'background': f"{server}https://embehub.com/img/Danz.png",
        'description': 'Canal DAZN 4 ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "https://play.embehub.com/DAZN_4/index.fmp4.m3u8",
                "title": "DAZN 4",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/DAZN_4/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:cartoon',
        "rc": {"token": "c0hIM0JOdlZWbG9VRkRoQzFFeHc3eWpG", "channel": "cartoon"},
        'type': 'tv',
        'name': 'CARTOON NETWORK',
        'poster': f"{server}https://embehub.com/img/thumb-cartoon.jpg",
        'background': f"{server}https://embehub.com/img/thumb-cartoon.jpg",
        'description': 'Canal CARTOON NETWORK ao vivo.',
        'genres': ['Infantil'],
        'streams': [
            {
                "url": "",
                "title": "CARTOON NETWORK",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:discoverykids',
        "rc": {"token": "c0hIM0JOdmFXVm9WRWpoRjNFMW43ekhPbGNSNENqWHQ=", "channel": "discoverykids"},
        'type': 'tv',
        'name': 'DISCOVERY KIDS',
        'poster': f"{server}https://embehub.com/img/thumb-discoverykids.jpg",
        'background': f"{server}https://embehub.com/img/thumb-discoverykids.jpg",
        'description': 'Canal DISCOVERY KIDS ao vivo.',
        'genres': ['Infantil'],
        'streams': [
            {
                "url": "",
                "title": "DISCOVERY KIDS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:disney',
        "rc": {"token": "c0hIM0JOdlZWVm9ZR3poRjNFMXE1VDQ9", "channel": "disney"},
        'type': 'tv',
        'name': 'DISNEY CHANNEL',
        'poster': f"{server}https://embehub.com/img/thumb-disney.jpg",
        'background': f"{server}https://embehub.com/img/thumb-disney.jpg",
        'description': 'Canal DISNEY CHANNEL ao vivo.',
        'genres': ['Infantil'],
        'streams': [
            {
                "url": "",
                "title": "DISNEY CHANNEL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:nick',
        "rc": {"token": "c0hIM0JOdmFXRkViRXpoUDNGMXY=", "channel": "nick"},
        'type': 'tv',
        'name': 'NICKELODEON',
        'poster': f"{server}https://embehub.com/img/thumb-nick.jpg",
        'background': f"{server}https://embehub.com/img/thumb-nick.jpg",
        'description': 'Canal NICKELODEON ao vivo.',
        'genres': ['Infantil'],
        'streams': [
            {
                "url": "",
                "title": "NICKELODEON",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:nickjr',
        "rc": {"token": "c0hIM0JOdmFWMUViRlRoUDNGMXY2alU9", "channel": "nickjr"},
        'type': 'tv',
        'name': 'NICK JR.',
        'poster': f"{server}https://embehub.com/img/thumb-nickjr.jpg",
        'background': f"{server}https://embehub.com/img/thumb-nickjr.jpg",
        'description': 'Canal NICK JR. ao vivo.',
        'genres': ['Infantil'],
        'streams': [
            {
                "url": "",
                "title": "NICK JR.",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:cartoonito',
        "rc": {"token": "c0hIM0JOdlZVMW9iR2poQzFFeHc3eWpGanNsOA==", "channel": "cartoonito"},
        'type': 'tv',
        'name': 'CARTOONITO',
        'poster': f"{server}https://embehub.com/img/thumb-cartoonito.jpg",
        'background': f"{server}https://embehub.com/img/thumb-cartoonito.jpg",
        'description': 'Canal CARTOONITO ao vivo.',
        'genres': ['Infantil'],
        'streams': [
            {
                "url": "",
                "title": "CARTOONITO",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:gloobinho',
        "rc": {"token": "c0hIM0JOdlVWRk1aRkRoRzJWRnI0aTdGajlJPQ==", "channel": "gloobinho"},
        'type': 'tv',
        'name': 'GLOOBINHO',
        'poster': f"{server}https://embehub.com/img/globinho.png",
        'background': f"{server}https://embehub.com/img/globinho.png",
        'description': 'Canal GLOOBINHO ao vivo.',
        'genres': ['Infantil'],
        'streams': [
            {
                "url": "",
                "title": "GLOOBINHO",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:gloob',
        "rc": {"token": "c0hIM0JOdmFXRklhRmpoRzJWRnI0Zz09", "channel": "gloob"},
        'type': 'tv',
        'name': 'GLOOB',
        'poster': f"{server}https://embehub.com/img/gloob.png",
        'background': f"{server}https://embehub.com/img/gloob.png",
        'description': 'Canal GLOOB ao vivo.',
        'genres': ['Infantil'],
        'streams': [
            {
                "url": "",
                "title": "GLOOB",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bandnews',
        "rc": {"token": "c0hIM0JOdlZVRkFlR3poRDFGQmc3aUxjbEE9PQ==", "channel": "bandnews"},
        'type': 'tv',
        'name': 'BAND NEWS',
        'poster': f"{server}https://embehub.com/img/thumb-bandnews.jpg",
        'background': f"{server}https://embehub.com/img/thumb-bandnews.jpg",
        'description': 'Canal BAND NEWS ao vivo.',
        'genres': ['Noticias'],
        'streams': [
            {
                "url": "",
                "title": "BAND NEWS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:cnnbrasil',
        'type': 'tv',
        'name': 'CNN BRASIL',
        'poster': f"{server}https://embehub.com/img/thumb-cnnbrasil.jpg",
        'background': f"{server}https://embehub.com/img/thumb-cnnbrasil.jpg",
        'description': 'Canal CNN BRASIL ao vivo.',
        'genres': ['Noticias'],
        'streams': [
            {
                "url": "https://video01.soultv.com.br/cnnbrasil/cnnbrasil/chunklist_w2038826838.m3u8",
                "title": "CNN BRASIL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://soultv.com.br",
                            "Referer": "https://soultv.com.br/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:jovempannews',
        'type': 'tv',
        'name': 'JOVEM PAN NEWS',
        'poster': f"{server}https://embehub.com/img/jovempamnews.jpg",
        'background': f"{server}https://embehub.com/img/jovempamnews.jpg",
        'description': 'Canal JOVEM PAN NEWS ao vivo.',
        'genres': ['Noticias'],
        'streams': [
            {
                "url": "https://play.embehub.com/JOVEMPANNEWS/index.fmp4.m3u8",
                "title": "JOVEM PAN NEWS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/JOVEMPANNEWS/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:recordnews',
        "rc": {"token": "c0hIM0JOdlZVRlFaRmpoVDBGMXI4aVBGZ3NwZw==", "channel": "recordnews"},
        'type': 'tv',
        'name': 'RECORD NEWS',
        'poster': f"{server}https://embehub.com/img/recordnews.png",
        'background': f"{server}https://embehub.com/img/recordnews.png",
        'description': 'Canal RECORD NEWS ao vivo.',
        'genres': ['Noticias'],
        'streams': [
            {
                "url": "",
                "title": "RECORD NEWS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:globonews',
        "rc": {"token": "c0hIM0JOdmFWRmNaRnpoRzJWRm03eW5Pa000PQ==", "channel": "globonews"},
        'type': 'tv',
        'name': 'GLOBO NEWS',
        'poster': f"{server}https://embehub.com/imagens/globonews.png",
        'background': f"{server}https://embehub.com/imagens/globonews.png",
        'description': 'Canal GLOBO NEWS ao vivo.',
        'genres': ['Noticias'],
        'streams': [
            {
                "url": "",
                "title": "GLOBO NEWS",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam1',
        "rc": {"token": "c0hIM0JOdmJWMUliRURoRDExdzJ0U1k9", "channel": "bbb25a"},
        'type': 'tv',
        'name': 'BBB 25 CAM 1',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 1 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "",
                "title": "BBB 25 CAM 1",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam2',
        "rc": {"token": "c0hIM0JOdlZWVklVRmpoRDExdzJ0U1U9", "channel": "bbb25b"},
        'type': 'tv',
        'name': 'BBB 25 CAM 2',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 2 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam02/index.fmp4.m3u8",
                "title": "BBB 25 CAM 2",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam3',
        'type': 'tv',
        'name': 'BBB 25 CAM 3',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 3 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam03/index.fmp4.m3u8",
                "title": "BBB 25 CAM 3",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbcam03/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam4',
        'type': 'tv',
        'name': 'BBB 25 CAM 4',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 4 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam04/index.fmp4.m3u8",
                "title": "BBB 25 CAM 4",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbcam04/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam5',
        'type': 'tv',
        'name': 'BBB 25 CAM 5',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 5 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam05/index.fmp4.m3u8",
                "title": "BBB 25 CAM 5",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbcam05/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam6',
        'type': 'tv',
        'name': 'BBB 25 CAM 6',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 6 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam06/index.fmp4.m3u8",
                "title": "BBB 25 CAM 6",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbcam06/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam7',
        'type': 'tv',
        'name': 'BBB 25 CAM 7',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 7 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam07/index.fmp4.m3u8",
                "title": "BBB 25 CAM 7",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbcam07/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam8',
        'type': 'tv',
        'name': 'BBB 25 CAM 8',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 8 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam08/index.fmp4.m3u8",
                "title": "BBB 25 CAM 8",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbcam08/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam9',
        'type': 'tv',
        'name': 'BBB 25 CAM 9',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 9 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam09/index.fmp4.m3u8",
                "title": "BBB 25 CAM 9",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbcam09/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25cam10',
        'type': 'tv',
        'name': 'BBB 25 CAM 10',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 CAM 10 ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbcam10/index.fmp4.m3u8",
                "title": "BBB 25 CAM 10",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbcam10/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:bbb25mosaico',
        'type': 'tv',
        'name': 'BBB 25 MOSAICO',
        'poster': f"{server}https://embehub.com/img/bbb25.png",
        'background': f"{server}https://embehub.com/img/bbb25.png",
        'description': 'Canal BBB 25 MOSAICO ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://play.embehub.com/bbbmosaico/index.fmp4.m3u8",
                "title": "BBB 25 MOSAICO",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Referer": "https://play.embehub.com/bbbmosaico/embed.html"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:kpoptv',
        'type': 'tv',
        'name': 'KPOP TV',
        'poster': f"{server}https://kpoptv.htforum.net/wp-content/uploads/2024/11/logokpoptvplay.png",
        'background': f"{server}https://kpoptv.htforum.net/wp-content/uploads/2024/11/logokpoptvplay.png",
        'description': 'Canal KPOP TV ao vivo.',
        'genres': ['Variedades'],
        'streams': [
            {
                "url": "https://giatv.bozztv.com/giatv/giatv-kpoptvplay/kpoptvplay/playlist.m3u8",
                "title": "KPOP TV",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
                        }
                    }
                }
            }
        ]
    }, 
    {
        'id': 'oneplay:timesbrasil',
        'type': 'tv',
        'name': 'TIMES BRASIL | CNBC',
        'poster': f"{server}https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Times_Brasil_CNBC_logo.svg/2560px-Times_Brasil_CNBC_logo.svg.png",
        'background': f"{server}https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Times_Brasil_CNBC_logo.svg/2560px-Times_Brasil_CNBC_logo.svg.png",
        'description': 'Canal TIMES BRASIL | CNBC ao vivo.',
        'genres': ['Noticias'],
        'streams': [
            {
                "url": "https://video01.soultv.com.br/timesbrasil/timesbrasil/chunklist_w1994015498.m3u8",
                "title": "TIMES BRASIL | CNBC",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://soultv.com.br",
                            "Referer": "https://soultv.com.br/"
                        }
                    }
                }
            }
        ]
    },
    {
        'id': 'oneplay:nossofutebol',
        "rc": {"token": "c0hIM0JOdmFXRkFkRWpoUDJrMTM3eUhlazloeEREMD0=", "channel": "nossofutebol"},
        'type': 'tv',
        'name': 'NOSSO FUTEBOL',
        'poster': f"{server}https://embedcanaistv.com/player3/imgs-videos/Canais/nossofutebol.jpg",
        'background': f"{server}https://embedcanaistv.com/player3/imgs-videos/Canais/nossofutebol.jpg",
        'description': 'Canal NOSSO FUTEBOL ao vivo.',
        'genres': ['Esportes'],
        'streams': [
            {
                "url": "",
                "title": "NOSSO FUTEBOL",
                "behaviorHints": {
                    "notWebReady": True,
                    "proxyHeaders": {
                        "request": {
                            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
                            "Origin": "https://embedcanaistv.com",
                            "Referer": "https://embedcanaistv.com/"
                        }
                    }
                }
            }
        ]
    }                                                                                                                              
    ]
    return canais

# def get_rc(channel,token):
#     stream = ''
#     try:
#         headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0'}
#         page = f'https://oneplayhd.com/rcproxy/rcproxy2.php?channel={quote(channel)}&token={quote(token)}'         
#         r = requests.get(page,headers=headers,allow_redirects=False,timeout=6)
#         if r.status_code in [301, 302]:
#             stream = r.headers.get("Location")
#             if stream.startswith('//'):
#                 stream = 'https:' + stream               
#     except:
#         pass
#     return stream

def unfuck_rc(html):
    try:
        secret = re.findall(r'replace.+?-\s*(\d+)', html)[0]
        soup = BeautifulSoup(html, "html.parser")
        script_content = soup.find('script').string
        base64_values = []
        for line in script_content.splitlines():
            try:
                line = line.split('""')[1]
            except:
                pass
            if '"' in line:
                bases_64 = re.findall(r'"(.*?)"', line)
                if bases_64:
                    for base64_value in bases_64:
                        base64_values.append(str(base64_value))
        nzB = ""
        for value in base64_values:
            decoded = base64.b64decode(value).decode('utf-8')
            number = int(''.join(filter(str.isdigit, decoded)))
            nzB += chr(number - int(secret))
        if nzB:
            html = nzB
    except:
        pass
    return html 

def get_token(channel): 
    token = ''   
    url = f'https://embedcanaistv.com/player3/ch.php?categoria=live&canal={channel}'
    headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
                'Origin': 'https://embedcanaistv.com',
                'Referer': 'https://embedcanaistv.com/',
                'accept-language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin'}
    cookie = {'modalVisited':'true'}
    r = requests.get(url,headers=headers,cookies=cookie)
    if r.status_code == 200:
        src = r.text
        html = unfuck_rc(src)
        try:
            token = re.findall(r"'rctoken':'(.*?)'", html)[-1]
        except:
            pass
    return token

def get_rc(channel,token):
    stream = ''
    try:
        # fix token random
        try:
            token = get_token(channel)
        except:
            pass
        # access channel
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0',
                'Origin': 'https://embedcanaistv.com',
                'Referer': 'https://embedcanaistv.com/',
                'accept-language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-origin',
                'x-requested-with': 'XMLHttpRequest'}
        page = f'https://embedcanaistv.com/player3/chforms.api?canal={channel}'
        cookie = {'modalVisited':'true'}
        data = {'rctoken': token}
        r = requests.post(page,headers=headers,cookies=cookie,data=data,timeout=6)
        if r.status_code == 200:
            #stream = re.findall(r'src:\s*"(.*?)"', src)[-1]
            pattern = r'const CHROMECAST_URL = "(.*?)";'
            stream = re.findall(pattern, r.text)[-1]
            if stream.startswith('//'):
                stream = 'https:' + stream
            # fix stream
            stream = stream.replace('\n', '').replace(' ', '')
        else:
            stream = 'code_' + str(r.status_code)
    except:
        pass
    return stream


##print(get_rc('bobosp', 'c0hIM0JOdmVXVk1VRmpoRDJseHI4emM9'))