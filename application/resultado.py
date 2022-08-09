import streamlit as st
import pandas as pd
import altair as alt
from application import utils as util

def run():
  if "total_area_dic" not in st.session_state:
    st.session_state.total_area_dic={}

  survey = st.session_state.survey
  calcular_puntajes()
  st.write(st.session_state.total_area_dic)
  df_areas = pd.DataFrame.from_dict(st.session_state.total_area_dic, orient='index').sort_values(by=['total'], ascending=False).head(3)
  areas = list(df_areas.index)
  st.table(df_areas)
  st.write(areas)

  grafico =alt.Chart(df_areas.reset_index()).mark_bar().encode(
    x='index',
    y='total'
  ).properties(
    width=200,
    height=150
  )
  st.altair_chart(grafico)

  tabla_result_csv = util.convert_df(df_areas.reset_index())
  st.download_button(
      label="Descargar dataset en CSV",
      data=tabla_result_csv,
      file_name='resultado_encuesta.csv',
      mime='text/csv',
      key="1"
    )
  

def calcular_puntajes():
  num = st.session_state.curr_page

  survey = st.session_state.survey
  areas = list(survey.index)
  preguntas=list(survey.columns[1:])

  area_total = areas[num]+"_total"
  if area_total not in st.session_state:
    st.session_state[area_total] = 0
  
  for area in areas:
    subtotal_agrado = 0
    subtotal_indiferente = 0
    subtotal_desagrado = 0
    for i_pre, pregunta in enumerate(preguntas):
      if type(survey[preguntas[i_pre]][area]) == float:
        continue
      else:
        session_variable = area+"_"+pregunta
        subtotal_agrado += st.session_state[session_variable+"_agrado_puntaje"]
        subtotal_indiferente += st.session_state[session_variable+"_indiferente_puntaje"]
        subtotal_desagrado += st.session_state[session_variable+"_desagrado_puntaje"]

    # st.session_state[area_total] = subtotal_agrado + subtotal_indiferente + subtotal_desagrado
    total_areas = subtotal_agrado + subtotal_indiferente + subtotal_desagrado
  
    st.session_state.total_area_dic[area] = {
      'agrado' : subtotal_agrado,
      'indiferente' : subtotal_indiferente,
      'desagrado' : subtotal_desagrado,
      'total': total_areas
    }
  
