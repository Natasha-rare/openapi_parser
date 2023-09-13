# API for Cinemas Open Data
API on Django, that uses django-rest-framework technology for providing opportunity to view information about cinemas in Russia. 

The api also makes possible to filter results by words in various fields (by using search), or to make strict filter using one or several fields. To see the output of all info or to do other described actions,you should follow link http://127.0.0.1:8000/api/cinemas/

### !!! API documentation is in _*swagger-open_api.yaml*_ file

You can download docker image here:

https://hub.docker.com/r/natan0lifer/openapi_parser

Or you can build docker container by yourself by opening the terminal
and writing the following commands:

```
docker compose build
```
And than
```
docker compose up -d
```
**Warning** First, you shoul download this repo and than open the twrminal in the folder, 
where you see [docker-compose.yml](docker-compose.yml) file.

To ensure hat service is working, you can follow link:
http://localhost:8000/api/cinemas/ or http://127.0.0.1:8000/api/cinemas/ 

![Пример ответа](https://i.ibb.co/KhRFyVG/2023-09-13-16-56-28.png)

---
You also can apply filters and add id in your link search, 
to select some concrete cinemas (for example inputting search or 
following http://localhost:8000/api/cinemas/5/, where 5 - is id, that you can change and get any record as you want)
