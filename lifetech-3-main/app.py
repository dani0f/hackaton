import streamlit as st
import time
import generator


#Función que agrega el link con foontawesome
def format_html(styled_html):
  init_html = """<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">\n"""
  end_html = ""  
  return init_html + "".join(styled_html) + end_html

#Función que recibe un string con html/css y lo convierte en un componente. Segundo input es el tiempo que se mostrara la diapositiva.
def generate_diap(styled_html, show_time):    
  component = st.components.v1.html(styled_html, width=800, height=600)
  component
  time.sleep(show_time)
  component.empty()



# styled_html
styled_html = """                                                                                         
<div class="slide">
  <style>
    /* Estilos de la diapositiva */
    .slide {
      width: 100%;
      height: 100vh;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      text-align: center;
      background-color: #f2f2f2;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 0;
    }

    .slide h1 {
      font-size: 36px;
      margin-bottom: 20px;
    }

    .slide h2 {
      font-size: 24px;
      margin-bottom: 10px;
    }

    .slide .icon {
      font-size: 48px;
      margin-bottom: 10px;
      color: #333;
    }
  </style>

  <h1>Instructivo de Seguridad para Empleados</h1>
  <h2>Promoviendo un entorno de trabajo seguro</h2>
  <div class="icon">
    <i class="fas fa-shield-alt"></i>
  </div>
</div>
"""


# Ejemplo de resultado del promp que resume los datos a ppt
# with open('example_design_and_content.txt') as f:
#     styled_html = f.readlines()




for diap in generator.diapositivas:
  result = format_html(diap)
  print(result)
  component = st.components.v1.html(result, width=800, height=600)
  time.sleep(9)
  component.empty()
  

st.divider()
user_input = st.text_area("Pregunta", "¿Qué hago en caso de accidente?'")



