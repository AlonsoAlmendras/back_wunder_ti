FROM python:3

# Directorio virtual de la aplicacion
WORKDIR /app

# Node
RUN wget -qO- https://deb.nodesource.com/setup_14.x  | bash -

# Yarn
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee /etc/apt/sources.list.d/yarn.list

# Instalacion de dependencias del sistema
RUN apt-get update -qq && apt-get install -y nodejs yarn zsh postgresql

# Entorno de variables
ENV PYTHONUNBUFFERED=1

#COPY requirements.txt .
#RUN pip install -r requirements.txt

# Puerto virtual expuesto
EXPOSE 8000

RUN pip3 install django psycopg2 djangorestframework
# Start the main process.
CMD ["zsh"]
# manage.py runserver 0.0.0.0:8000