# Utiliza la imagen de Ubuntu como imagen base
FROM ubuntu:lunar

# Copia todo el código fuente al contenedor
COPY . /IA

# Instalando python y pip
RUN apt-get update 
RUN apt-get update && apt-get install -y curl
RUN apt-get install -y python3.10 python3.10-distutils
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python3.10

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /IA

# Instalamos y corremos poetry
RUN pip install poetry
RUN poetry install

