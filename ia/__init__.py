import requests as rq
import os
import xml.etree.ElementTree as ET
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
import re



def send_pdf_to_grobid(pdf_path):
    # URL de la API de Grobid
    url = 'http://grobid:8070/api/processFulltextDocument'

    # Se abre el archivo PDF en modo lectura binaria
    with open(pdf_path, 'rb') as pdf_file:
        # Se envía el archivo PDF a Grobid
        response = rq.post(url, files={'input': pdf_file})

    # Se verifica que la respuesta de Grobid sea exitosa (código 200)
        if response.status_code == 200:
            # Se devuelve el contenido de la respuesta en formato XML
            return response.content.decode('utf-8')
        else:
            # En caso de error, se devuelve None
            return None


xml_data='' # Cadena donde almacenaremos los resumenes de los XML
links = ''
folder_path = '/IA/ia/resources'
pdf_names = []  # Lista para guardar los nombres de los PDFs
images_n = []  # Lista para guardar el número de imágenes por PDF

# Se recorre la carpeta leyendo todos los archivos PDF
for filename in os.listdir(folder_path):
    if filename.endswith('.pdf'):
        # Ruta completa del archivo PDF
        pdf_path = os.path.join(folder_path, filename)
        
        # Se envía el archivo PDF a Grobid
        xml_grob = send_pdf_to_grobid(pdf_path)
        if xml_grob is not None:
            # root = ET.fromstring(xml_grob)
            # abstract = root.find(".//abstract")
            soup = BeautifulSoup(xml_grob, 'lxml')
            abstract = soup.find('text').text
            if abstract is not None:
                xml_data += abstract
            num_images = len(soup.find_all('figure'))
            pdf_names.append(filename)
            images_n.append(num_images)
            txt=soup.get_text()
            patron_url = re.compile(r'(?:http[s]?://)?(www.[^\s]+)')
            urls_encontradas = re.findall(patron_url, txt)
            if len(urls_encontradas) == 0:
                print(f'El archivo {filename} no contiene URLs')
            else:
                print(f'El archivo {filename} tiene los URL: ' + str(urls_encontradas))
        else:
            # En caso de error, se muestra un mensaje de error
            print(f'Error al procesar el archivo {pdf_path}')

 #nltk.download('stopwords')  # Diccionario de palabras que no aportan significado
stop_words = set(stopwords.words('english'))

# Eliminar de xml_data todas las stopwords
words = abstract.split()
filtered_words = [word for word in words if word.lower() not in stop_words]
processed_text = ' '.join(filtered_words)

# Crear la nube de palabras clave
wordcloud = WordCloud(width=800, height=800, background_color='white', max_words=50, contour_width=3, contour_color='steelblue')
wordcloud.generate(xml_data)

# Visualizar la nube de palabras clave
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.savefig(folder_path+'/wordcloud.png') 

# Visualizar el numero de imagenes por PDF
plt.bar(pdf_names, images_n)
plt.xticks(rotation=90)  # Rotamos los nombres de los PDFs para que se vean mejor
plt.xlabel('Nombre del PDF')
plt.ylabel('Número de imágenes')
plt.title('Número de imágenes por PDF')
plt.savefig(folder_path+'/images.png')
