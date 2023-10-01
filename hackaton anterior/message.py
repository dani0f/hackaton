import openai
from langchain import PromptTemplate
from gtp_conection import get_api_key


key = get_api_key()

openai.api_key = key  # Reemplaza 'TU_API_KEY' con tu propia clave API

plantilla = """Hola, quiero que actues como experto guionista de presentaciones ppt, 
Te pasate arreglo de diapositivas y quiero que me entregues la narración en base a cada diapositiva, 
Dame el resultado separado entre comillas"""
diccionario =  """
[
  {
    "diapositiva1": "<div style='position: relative; width: 800px; height: 600px; font-family: Arial, sans-serif;'>\n<h2 style='font-size: 24px;'>Pasos a seguir antes de un sismo</h2>\n<p style='font-size: 16px;'>Es crucial estar preparado antes de un sismo. Esto incluye tener un plan de emergencia un kit de suministros y conocer las \u00e1reas seguras dentro y fuera de su hogar.</p>\n</div>",
    "diapositiva2": "<div style='position: relative; width: 800px; height: 600px; font-family: Arial, sans-serif;'>\n<h2 style='font-size: 24px;'>C\u00f3mo actuar durante un sismo</h2>\n<p style='font-size: 16px;'>Durante un sismo es importante mantener la calma y seguir las pr\u00e1cticas de seguridad recomendadas como Detenerse Cubrirse y Agarrarse. Evite estar cerca de ventanas o muebles que puedan caer.</p>\n</div>",
    "diapositiva3": "<div style='position: relative; width: 800px; height: 600px; font-family: Arial, sans-serif;'>\n<h2 style='font-size: 24px;'>Preparaci\u00f3n antes de un tsunami</h2>\n<p style='font-size: 16px;'>Al igual que con un sismo es vital tener un plan de emergencia para un tsunami. Conozca las rutas de evacuaci\u00f3n y tenga un kit de suministros listo.</p>\n</div>",
    "diapositiva4": "<div style='position: relative; width: 800px; height: 600px; font-family: Arial, sans-serif;'>\n<h2 style='font-size: 24px;'>C\u00f3mo manejar durante un sismo</h2>\n<p style='font-size: 16px;'>Si se encuentra conduciendo durante un sismo detenga el veh\u00edculo en un lugar seguro y permanezca dentro hasta que el temblor haya cesado.</p>\n</div>",
    "diapositiva5": "<div style='position: relative; width: 800px; height: 600px; font-family: Arial, sans-serif;'>\n<h2 style='font-size: 24px;'>Preparaci\u00f3n antes de un tsunami (Repetici\u00f3n)</h2>\n<p style='font-size: 16px;'>Es importante repetir que la preparaci\u00f3n previa a un tsunami es crucial. Conozca las rutas de evacuaci\u00f3n y tenga un kit de suministros listo.</p>\n</div>"
  }
]
"""


respuesta = openai.Completion.create(
  engine="text-davinci-003",  # Elige el motor adecuado para tus necesidades
  prompt=diccionario,
  max_tokens=1050  # Ajusta la longitud de respuesta según tus necesidades
)

print(respuesta.choices[0].text.strip())