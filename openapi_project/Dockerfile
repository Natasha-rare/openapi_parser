FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DJANGO_SETTINGS_MODULE openapi_project.settings

RUN mkdir /app
WORKDIR /app
COPY . /app/

RUN pip install -r requirements.txt
RUN python parcer.py

RUN python /app/manage.py inspectdb > /app/api/models.py
COPY admin.py /app/api/admin.py

####
#EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "localhost:8000"]