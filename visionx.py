import io
import os
from google.cloud import vision
from google.cloud.vision import types

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "apikey.json"  #--> para que coja la clave directamente desde python
#export GOOGLE_APPLICATION_CREDENTIALS='apikey.json'   --> si lo pones en la terminal de linux la coje desde el S.O

cliente = vision.ImageAnnotatorClient()

nombre_archivo = os.path.join(
	os.path.dirname(__file__),
	'fotos/salamanca.jpg')

with io.open(nombre_archivo,'rb') as archivo_imagen:
	content = archivo_imagen.read()

imagen = types.Image(content=content)

response = cliente.label_detection(image=imagen)

atributos = response.label_annotations

print("Descripcion de la imagen:")

for atributo in atributos:
	print (atributo.description)
