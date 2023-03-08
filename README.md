# Grobid PDF management
In this documentation your are going to find out how to install, prepare and run my Grobid based PDF management tool.

## Getting started
To get this project running we are going to need two tools prepared previously: Docker and Grobid docker.

## Installing Grobid
We assume that you have Docker installed correctly on your PC, if not, please do so.

Grobid is an open-source software that extracts and structures information from scholarly documents in various formats. Grobid environment is containerized in a Docker container. To install the Grobid Docker you should follow the instructions from its GitHub repository: https://grobid.readthedocs.io/en/latest/Grobid-docker/#crf-only-image

Once u have it nicely downloaded, u should pull its docker image by running the next command: docker pull lfoppiano/grobid:0.7.2

## Downloading and building the tool
First of all, you are going to download the project by the Clone button from GitHub in this repository. In this repository we will find several files including the Dockerfile (to build the image of our Docker), pyproyect.toml (with all the dependencies of our environment) and a directory /ia containing the script to run.

Once it is downloaded, in a terminal you are going to position yourself in the downloaded folder. Once positioned we are going to build the Docker image by the next command: docker build -t image_name .

Don't forget to change 'image_name' to the name you want to your Docker image.
You can also check that your image has been created correctly with the command: docker images

## Running the tool
Before running anything we are going to define a network to be able to connect Grobid with the Docker of our tool with the following command: docker network create network_name

Una vez tengas la network creada vamos a ejecutar el docker de Grobid: docker run --name grobid --network network_name -t --rm -p 8070:8070 lfoppiano/grobid:0.7.2

When grobid is running, we will open a new terminal, position yourself inside the downloaded folder (where Dockerfile is) and use the following command to run the docker image: docker run -it --network="network_name" --rm -v /Local-path-with-ur-PDFs:/IA/ia/resources image_name

Remember to change /Local-path-with-ur-PDFs to the path where you have saved the PDFs you want to process. This will generate a shared folder inside the docker with your local path.

When you are inside Docker, you are going to place yourself in the script folder: cd ia
After this, we will start the poetry shell: poetry shell
Once we get here, and if everything has gone as expected, we are going to run the tool script: poetry run python3.10 __init__.py

This will display (among other messages) a list of the URLs of each PDF (if any). It will also insert in the Volume, or shared folder, wordcloud.png, which contains a word cloud with the most repeated keywords of all PDFs. In addition to images.png, with a count of the images in each PDF. This can be found in the /IA/ia/resources directory in Docker, or in the local folder where you had your PDFs.
