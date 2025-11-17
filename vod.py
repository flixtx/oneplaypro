import encode_string
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, quote_plus, quote
import re


class ondemand:
    def __init__(self):
        self.proxy_image = 'https://da5f663b4690-proxyimage.baby-beamup.club/proxy-image/?url='
        self.vod_site = 'https://flixapi.brunoflix9.workers.dev/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)

    def movies_catalog(self):
        url = f'{self.vod_site}movies'
        catalog = []
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # movies watched
            try:
                section = soup.find_all('section', {'class': 'listContent mb-5'})
            except:
                section = []
            try:
                movies_w = section[1].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                movies_w = []
            # movies releases
            try:
                movies_r = section[2].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                movies_r = []
            # trending movies
            try:
                trending_movies = section[3].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                trending_movies = []
            # Little darlings movies   
            try:
                little_darlings_movies = section[4].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                little_darlings_movies = []
            # Family movies  
            try:
                family_movies = section[5].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                family_movies = []
            # Brazilian movies  
            try:
                brazilian_movies = section[6].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                brazilian_movies = []                                                             
        except:
            movies_w = []
            movies_r = []
            trending_movies = []
            little_darlings_movies = []
            family_movies = []
            brazilian_movies = []
        if movies_r:
            for n, movie in enumerate(movies_r):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    runtime = movie.find_all('span')[0].text.replace('Min', 'min')
                except:
                    runtime = ''
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'movie', 
                     'name': title, 
                     'year': year,
                     'runtime': runtime,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Lançamentos"]}
                catalog.append(m)  

        if movies_w:
            for n, movie in enumerate(movies_w):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    runtime = movie.find_all('span')[0].text.replace('Min', 'min')
                except:
                    runtime = ''
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'movie', 
                     'name': title, 
                     'year': year,
                     'runtime': runtime,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Filmes mais Vistos do Dia"]}
                catalog.append(m)

        if trending_movies:
            for n, movie in enumerate(trending_movies):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    runtime = movie.find_all('span')[0].text.replace('Min', 'min')
                except:
                    runtime = ''
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'movie', 
                     'name': title, 
                     'year': year,
                     'runtime': runtime,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Filmes em Alta"]}
                catalog.append(m)

        if little_darlings_movies:
            for n, movie in enumerate(little_darlings_movies):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    runtime = movie.find_all('span')[0].text.replace('Min', 'min')
                except:
                    runtime = ''
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'movie', 
                     'name': title, 
                     'year': year,
                     'runtime': runtime,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Queridinhos"]}
                catalog.append(m)

        if family_movies:
            for n, movie in enumerate(family_movies):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    runtime = movie.find_all('span')[0].text.replace('Min', 'min')
                except:
                    runtime = ''
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'movie', 
                     'name': title, 
                     'year': year,
                     'runtime': runtime,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Família"]}
                catalog.append(m) 

        if brazilian_movies:
            for n, movie in enumerate(brazilian_movies):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    runtime = movie.find_all('span')[0].text.replace('Min', 'min')
                except:
                    runtime = ''
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'movie', 
                     'name': title, 
                     'year': year,
                     'runtime': runtime,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Filmes Brasileiros"]}
                catalog.append(m)                                                                      
        return catalog                  
   
    
    def get_meta_movie(self, id):
        meta = {}
        try:
            id_ = id.replace('oneplay:', '')
            url = encode_string.decode_base32(id_)
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            info = soup.find('div', {'class': 'infoPoster mb-5'})
        except:
            info = None
        if info:
            try:
                image = info.find('div', {'class': 'poster'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '').replace("'", "")
            except:
                image = ''      
            if image:
                image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                image = self.proxy_image + quote(image) if self.proxy_image else image
            name = info.find('h1', {'class': 'fw-bolder mb-0'}).text
            extra_info = info.find('p', {'class': 'log py-4 mb-0'})
            try:
                runtime = extra_info.find_all('span')[0].text.replace('Min', 'min')
            except:
                runtime = ''
            try:
                year = int(extra_info.find_all('span')[1].text)
            except:
                year = 0
            try:
                imdb_rating = extra_info.find_all('span')[4].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                if imdb_rating == '0':
                    imdb_rating = 0.0
                imdb_rating = float(imdb_rating)                
            except:
                imdb_rating = 0.0
            try: 
                description = info.find('p', {'class': 'small linefive'}).text.replace('\n', '').replace('\r', '').replace('\t', '').replace('                    ', '').replace('                ', '')
            except:
                description = ''
            try:
                generos_ = info.find('p', {'class': 'lineone'}).find_all('span')
            except:
                generos_ = []
            if generos_:
                genres = [genero.text for genero in generos_[2:]]
            else:
                genres = []
            # try:
            #     href = info.find('a', {'class': 'btn free fw-bold'}).get('href', '')
            #     if href:
            #         id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
            # except:
            #     id_page = ''
            meta = {'id': id, 
                        'type': 'movie', 
                        'name': name, 
                        'year': year,
                        'runtime': runtime,
                        'imdbRating': imdb_rating,
                        'poster': image,
                        'logo': image,
                        'background': image,
                        'genres': genres,
                        'trailers': [],
                        'description': description,
                        'behaviorHints': {'defaultVideoId': id,
                                          'hasScheduledVideos': False}
            }
        return meta
    
    def get_search_movie(self, key):
        catalog = []
        url = f'{self.vod_site}search.php?q={quote_plus(key)}'
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'class': 'items break'})
        if div:
            movies = div.find_all('div', {'class': 'item poster'})
            if movies:
                for n, movie in enumerate(movies):
                    try:
                        runtime = movie.find_all('span')[0].text.replace('Min', 'min')
                    except:
                        runtime = ''
                    if not 'temporadas' in runtime.lower():
                        title = movie.find('h6').text
                        try:
                            year = int(movie.find_all('span')[1].text)
                        except:
                            year = 0                        
                        try:
                            imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                            if imdb_rating == '0':
                                imdb_rating = 0.0
                            imdb_rating = float(imdb_rating)                
                        except:
                            imdb_rating = 0.0
                        href = movie.find('a').get('href', '')
                        try:
                            image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                        except:
                            image = ''
                        if image:
                            image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                            image = self.proxy_image + quote(image) if self.proxy_image else image
                        id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                        m = {'id': id_page, 
                            'type': 'movie', 
                            'name': title, 
                            'year': year,
                            'runtime': runtime,
                            'imdbRating': imdb_rating,
                            'poster': image,
                            'background': image,
                            'genres': []}
                        catalog.append(m)
        return catalog

                
    
    def get_stream_movie(self, id):
        #url = encode_string.decode_base32(id)
        #url = 'http://www.playcinevs.info/m/14063'
        streams = []
        try:
            id_ = id.replace('oneplay:', '')
            url = encode_string.decode_base32(id_)
            response = self.session.get(url)
            src = response.text
            soup1 = BeautifulSoup(src, 'html.parser')
            info = soup1.find('div', {'class': 'infoPoster mb-5'})
            href = info.find('a', {'class': 'btn free fw-bold'}).get('href', '')
            response = self.session.get(href)
            src = response.text
            soup = BeautifulSoup(src, 'html.parser')            
            title = soup.title.string
            try:
                title = title.split('Assistindo: ')[1]
            except:
                title = 'Assista agora'
            try:    
                stream = re.findall(r"initializePlayer\('(.*?)'", src)[0]
            except:
                stream = ''
            stream_ = {
                    'name': 'OnePlay',
                    'title': title, 
                    'url': stream}
            streams.append(stream_)            
        except:
            pass
        return streams
    
    def series_catalog(self):
        url = f'{self.vod_site}tvseries'
        catalog = []
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # series watched
            try:
                section = soup.find_all('section', {'class': 'listContent mb-5'})
            except:
                section = []
            try:
                series_w = section[1].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                series_w = []
            # series releases
            try:
                series_r = section[2].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                series_r = []
            # Little darlings movies 
            try:
                little_darlings_series = section[3].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                little_darlings_series = []
            # series doramas 
            try:
                series_doramas = section[4].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                series_doramas = []
            # Brazilian series 
            try:
                brazilian_series = section[5].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                brazilian_series = []                                                             
        except:
            series_w = []
            series_r = []
            little_darlings_series = []
            series_doramas = []
            brazilian_series = []
        if series_r:
            for n, movie in enumerate(series_r):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Lançamentos"]}
                catalog.append(m)
                
        if series_w:
            for n, movie in enumerate(series_w):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Séries mais Vistas do Dia"]}
                catalog.append(m)  

        if little_darlings_series:
            for n, movie in enumerate(little_darlings_series):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Queridinhos"]}
                catalog.append(m)

        if series_doramas:
            for n, movie in enumerate(series_doramas):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Doramas"]}
                catalog.append(m)

        if brazilian_series:
            for n, movie in enumerate(brazilian_series):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Produções Brasileiras"]}
                catalog.append(m)                                                                      
        return catalog 

    def get_meta_serie(self, id):
        meta = {}
        try:
            id_ = id.replace('oneplay:', '')
            url = encode_string.decode_base32(id_)
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            info = soup.find('div', {'class': 'infoPoster mb-5'})
        except:
            info = None
        if info:
            try:
                image = info.find('div', {'class': 'poster'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '').replace("'", "")
            except:
                image = ''      
            if image:
                image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                image = self.proxy_image + quote(image) if self.proxy_image else image
            name = info.find('h1', {'class': 'fw-bolder mb-0'}).text
            extra_info = info.find('p', {'class': 'log py-4 mb-0'})
            try:
                t = extra_info.find_all('span')[0].text
            except:
                t = ''
            if 'temporadas' in t.lower():
                try:
                    year = int(extra_info.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = extra_info.find_all('span')[4].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                try: 
                    description = info.find('p', {'class': 'small linefive'}).text.replace('\n', '').replace('\r', '').replace('\t', '').replace('                    ', '').replace('                ', '')
                except:
                    description = ''
                try:
                    generos_ = info.find('p', {'class': 'lineone'}).find_all('span')
                except:
                    generos_ = []
                if generos_:
                    genres = [genero.text for genero in generos_[2:]]
                else:
                    genres = []
                # try:
                #     href = info.find('a', {'class': 'btn free fw-bold'}).get('href', '')
                #     if href:
                #         id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                # except:
                #     id_page = ''
                videos = []
                seasons = soup.find('select', {'id': 'seasons-view'}).find_all('option')
                for sn, season in enumerate(seasons, start=1):
                    id_season = season.get('value', '')
                    episodes_url = f'https://flixapi.brunoflix9.workers.dev/ajax/episodes.php?season={id_season}&page=1&_=1741914620310'
                    r_episodes = self.session.get(episodes_url)
                    soup_episodes = BeautifulSoup(r_episodes.text, 'html.parser')
                    buttons = soup_episodes.find_all('a', {'class': 'btn free fw-bold rounded-circle'})
                    cache_episodes = set()
                    ne = 0  # Número do episódio
                    for button in buttons:
                        link_ep = button.get('href', '')

                        if link_ep in cache_episodes:
                            continue  # Se o link já foi adicionado, ignoramos
                            
                        cache_episodes.add(link_ep)  # Adiciona o link no conjunto para evitar duplicatas
                        ne += 1  # Incrementa corretamente o número do episódio
                        # meta videos
                        ep_meta = {
                            'id': id + ':' + str(sn) + ':' + str(ne), 
                            'season': sn, 
                            'number': ne, 
                            'episode': ne, 
                            'name': f'Episódio {str(ne)}', 
                            'thumbnail': image
                            }
                        videos.append(ep_meta)
                meta = {'id': id, 
                            'type': 'series', 
                            'name': name, 
                            'year': year,
                            'imdbRating': imdb_rating,
                            'poster': image,
                            'logo': image,
                            'background': image,
                            'genres': genres,
                            'trailers': [],
                            'description': description,
                            'videos': videos,
                            'behaviorHints': {'hasScheduledVideos': False}
            }
        return meta 
    
    def get_search_serie(self, key):
        catalog = []
        url = f'{self.vod_site}search.php?q={quote_plus(key)}'
        response = self.session.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        div = soup.find('div', {'class': 'items break'})
        if div:
            movies = div.find_all('div', {'class': 'item poster'})
            if movies:
                for n, movie in enumerate(movies):
                    try:
                        runtime = movie.find_all('span')[0].text.replace('Min', 'min')
                    except:
                        runtime = ''
                    if 'temporadas' in runtime.lower():
                        title = movie.find('h6').text
                        try:
                            year = int(movie.find_all('span')[1].text)
                        except:
                            year = 0                        
                        try:
                            imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                            if imdb_rating == '0':
                                imdb_rating = 0.0
                            imdb_rating = float(imdb_rating)                
                        except:
                            imdb_rating = 0.0
                        href = movie.find('a').get('href', '')
                        try:
                            image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                        except:
                            image = ''
                        if image:
                            image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                            image = self.proxy_image + quote(image) if self.proxy_image else image
                        id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                        m = {'id': id_page, 
                            'type': 'series', 
                            'name': title, 
                            'year': year,
                            'imdbRating': imdb_rating,
                            'poster': image,
                            'background': image,
                            'genres': []}
                        catalog.append(m)
        return catalog
    
    def animes_catalog(self):
        url = f'{self.vod_site}animes'
        catalog = []
        try:
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            # animes watched
            try:
                section = soup.find_all('section', {'class': 'listContent mb-5'})
            except:
                section = []
            try:
                series_w = section[1].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                series_w = []
            # animes releases
            try:
                series_r = section[2].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                series_r = []
            # Little darlings animes
            try:
                little_darlings_series = section[3].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                little_darlings_series = []
            # animes classics
            try:
                series_classic = section[4].find("div", class_=re.compile("items$")).find_all("div", class_=re.compile("^swiper-slide"))
            except:
                series_classic = []                                                          
        except:
            series_w = []
            series_r = []
            little_darlings_series = []
            series_classic = []
        if series_r:
            for n, movie in enumerate(series_r):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Lançamentos"]}
                catalog.append(m)
                
        if series_w:
            for n, movie in enumerate(series_w):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Animes mais Vistos do Dia"]}
                catalog.append(m)  

        if little_darlings_series:
            for n, movie in enumerate(little_darlings_series):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Queridinhos"]}
                catalog.append(m)

        if series_classic:
            for n, movie in enumerate(series_classic):
                title = movie.find('h6').text
                try:
                    year = int(movie.find_all('span')[1].text)
                except:
                    year = 0
                try:
                    imdb_rating = movie.find_all('span')[2].text.replace('IMDb: ', '').replace(' ', '').replace('IMDb', '')
                    if imdb_rating == '0':
                        imdb_rating = 0.0
                    imdb_rating = float(imdb_rating)                
                except:
                    imdb_rating = 0.0
                href = movie.find('a').get('href', '')
                try:
                    image = movie.find('div', {'class': 'content'}).get('style').replace('background-image: url(', '').replace(');', '').replace(')', '')
                except:
                    image = ''
                if image:
                    image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                    image = self.proxy_image + quote(image) if self.proxy_image else image
                id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''
                m = {'id': id_page, 
                     'type': 'series', 
                     'name': title, 
                     'year': year,
                     'imdbRating': imdb_rating,
                     'poster': image,
                     'background': image,
                     'genres': ["Clássicos"]}
                catalog.append(m)                                                                     
        return catalog 
    
    def doramas_catalog(self, skip=0):
        number_itens = 24
        page = (int(skip) // number_itens) + 1
        url = f'{self.vod_site}ajax/genre.php?genre=197&page={str(page)}'
        catalog = []
        try:
            r = self.session.get(url).json()
            if r:
                for i in r:
                    try:
                        title = i['title']
                        image = i['image']
                        year = i['release']
                        t = i['time']
                        if 'temporadas' in t.lower():
                            if image:
                                image = image.replace('//uploads/', '/uploads/').replace('/w300//', '/w300/')
                                image = self.proxy_image + quote(image) if self.proxy_image else image
                            href = f'{self.vod_site}watch/' + i['slug']
                            imdb_rating = i['imdb_rating']
                            id_page = 'oneplay:' + encode_string.encode_base32(href) if href else ''                        
                            m = {'id': id_page, 
                                'type': 'series', 
                                'name': title, 
                                'year': year,
                                'imdbRating': imdb_rating,
                                'poster': image,
                                'background': image,
                                'genres': []}
                            catalog.append(m)
                    except:
                        pass

        except:
            pass
        return catalog


    def get_stream_serie(self, id):
        streams = []
        try:
            id_ = id.replace('oneplay:', '')
            serie_id = id_.split(':')
            url = encode_string.decode_base32(serie_id[0])
            season_number = serie_id[1]
            episode_number = serie_id[2]
            response = self.session.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            info = soup.find('div', {'class': 'infoPoster mb-5'})
        except:
            info = None
        if info:
            extra_info = info.find('p', {'class': 'log py-4 mb-0'})
            try:
                t = extra_info.find_all('span')[0].text
            except:
                t = ''
            if 'temporadas' in t.lower():
                stream_final = ''
                seasons = soup.find('select', {'id': 'seasons-view'}).find_all('option')
                for sn, season in enumerate(seasons, start=1):
                    if int(season_number) == sn:
                        id_season = season.get('value', '')
                        episodes_url = f'https://flixapi.brunoflix9.workers.dev/ajax/episodes.php?season={id_season}&page=1&_=1741914620310'
                        r_episodes = self.session.get(episodes_url)
                        soup_episodes = BeautifulSoup(r_episodes.text, 'html.parser')
                        buttons = soup_episodes.find_all('a', {'class': 'btn free fw-bold rounded-circle'})
                        cache_episodes = set()
                        ne = 0  # Número do episódio
                        for button in buttons:
                            link_ep = button.get('href', '')

                            if link_ep in cache_episodes:
                                continue  # Se o link já foi adicionado, ignoramos
                                
                            cache_episodes.add(link_ep)  # Adiciona o link no conjunto para evitar duplicatas
                            ne += 1  # Incrementa corretamente o número do episódio
                            if int(episode_number) == ne:
                                stream_final += link_ep
                                break
                        break
                # raspar link stream
                response = self.session.get(stream_final)
                src = response.text
                soup = BeautifulSoup(src, 'html.parser')            
                title = soup.title.string
                try:
                    title = title.split('Assistindo: ')[1]
                except:
                    title = 'Assista agora'
                try:    
                    stream = re.findall(r"initializePlayer\('(.*?)'", src)[0]
                except:
                    stream = ''
                stream_ = {
                        'name': 'OnePlay',
                        'title': title, 
                        'url': stream}
                streams.append(stream_)
        return streams
        

