import math
import streamlit as st
import pandas as pd
from application import conn_data as cn, resultado as result_page


def asignar(llave):
  opcion = llave.split("_")[2]
  area_preg = llave.split("_")[0]+"_"+ llave.split("_")[1]

  if opcion == "agrado":
    st.session_state[area_preg+"_"+"indiferente"] = False
    st.session_state[area_preg+"_"+"desagrado"] = False
    if st.session_state[area_preg+"_"+"agrado"]:
        st.session_state[area_preg+"_"+"agrado_puntaje"] += 3
        if st.session_state[area_preg+"_"+"indiferente_puntaje"] > 0:
            st.session_state[area_preg+"_"+"indiferente_puntaje"] -= 2
        if st.session_state[area_preg+"_"+"desagrado_puntaje"] > 0:
            st.session_state[area_preg+"_"+"desagrado_puntaje"] -= 1
    else:
        st.session_state[area_preg+"_"+"agrado_puntaje"] -= 3

  if opcion == "indiferente":
    st.session_state[area_preg+"_"+"agrado"] = False
    st.session_state[area_preg+"_"+"desagrado"] = False
    if st.session_state[area_preg+"_"+"indiferente"]:
        st.session_state[area_preg+"_"+"indiferente_puntaje"] += 2
        if st.session_state[area_preg+"_"+"agrado_puntaje"] > 0:
            st.session_state[area_preg+"_"+"agrado_puntaje"] -= 3
        if st.session_state[area_preg+"_"+"desagrado_puntaje"] > 0:
            st.session_state[area_preg+"_"+"desagrado_puntaje"] -= 1
    else:
        st.session_state[area_preg+"_"+"indiferente_puntaje"] -= 2

  if opcion == "desagrado":
    st.session_state[area_preg+"_"+"agrado"] = False
    st.session_state[area_preg+"_"+"indiferente"] = False
    if st.session_state[area_preg+"_"+"desagrado"]:
        st.session_state[area_preg+"_"+"desagrado_puntaje"] += 1
        if st.session_state[area_preg+"_"+"indiferente_puntaje"] > 0:
            st.session_state[area_preg+"_"+"indiferente_puntaje"] -= 2
        if st.session_state[area_preg+"_"+"agrado_puntaje"] > 0:
            st.session_state[area_preg+"_"+"agrado_puntaje"] -= 3
    else:
        st.session_state[area_preg+"_"+"desagrado_puntaje"] -= 1


def area_pagina():
  survey = st.session_state.survey
  areas = list(survey.index)
  preguntas=list(survey.columns[1:])
  alternativas = ['agrado','indiferente','desagrado']
  
  num = st.session_state.curr_page
  
  # st.markdown(f"### {areas[num].upper()}")
  # col1 = st.columns()
  st.markdown(f"### {num+1}.- {survey['description'][areas[num]].capitalize()}")  # Muestra e pantalla la descripción del área.
  # col2.write(f"Página {st.session_state.curr_page + 1} de {len(areas)}")  # Muestra en pantalla la paginación.

  st.markdown('----------------------------------')
  for i_pre, pregunta in enumerate(preguntas):
      # print(type(survey[preguntas[i_pre]][areas[num]]))
    if type(survey[preguntas[i_pre]][areas[num]]) == float:
      continue
    else:
      st.markdown(f"###### {i_pre+1}.- {survey[preguntas[i_pre]][areas[num]]}") # Muestra en pantalla el enunciado de cada pregunta. 
      cols = st.columns(5)
      for i, alternativa in enumerate(alternativas):
        session_variable = areas[num]+"_"+pregunta+"_"+alternativa
        session_puntaje = areas[num]+"_"+pregunta+"_"+alternativa+"_puntaje"
        if session_variable not in st.session_state:
            st.session_state[session_variable] = False
            st.session_state[session_puntaje] = 0
        cols[i].checkbox(label=alternativa.capitalize(), value=st.session_state[session_variable], key=session_variable, on_change=asignar,args=[session_variable,])  # Muestra en pantalla las alternativas en checkbox

def run():
    
  cn.run()
  result = st.session_state.result
  survey = st.session_state.survey

  if 'num' not in st.session_state:
    st.session_state.curr_page = 0
    st.session_state.result_page = False
    st.session_state.num = 0

  with st.container():
    if st.session_state.result_page:
      result_page.run()
    else:
      area_pagina()

      st.markdown('----------------------------------')

      col3,_,col4 = st.columns([4,1,1])
      if col3.button('Siguiente'):
        respuesta, valor = validar_respuestas()
        if respuesta:
          if st.session_state.curr_page < len(st.session_state.survey.index)-1:
            st.session_state.curr_page += 1
          else:
            # st.session_state.curr_page = 0
            st.session_state.result_page = True
            # return True
          st.experimental_rerun()
        else:
          st.warning(f"Te falta responder la pregunta {valor}")
      
      col4.write(f"Página {st.session_state.curr_page + 1} de {len(list(survey.index))}")  # Muestra en pantalla la paginación.


# Esta función me permite validar las respuestas antes de seguir con la página siguiente
def validar_respuestas():
  num = st.session_state.curr_page

  survey = st.session_state.survey
  areas = list(survey.index)
  preguntas=list(survey.columns[1:])

  for i_pre, pregunta in enumerate(preguntas):
    if type(survey[preguntas[i_pre]][areas[num]]) == float:
      continue
    else:
      session_variable = areas[num]+"_"+pregunta
      if st.session_state[session_variable+"_agrado_puntaje"] <= 0 and st.session_state[session_variable+"_indiferente_puntaje"]  <= 0 and st.session_state[session_variable+"_desagrado_puntaje"] <= 0:
        return False, (i_pre + 1)
  return True , None

