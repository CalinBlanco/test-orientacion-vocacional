import streamlit as st

def generar_checkbox():
  areas = ['am','ic']
  preguntas=['q1','q2','q3']
  alternativas = ['agrado','indiferente','desagrado']
  # cn.run()
  # result = st.session_state.result
  # survey = st.session_state.survey

  if 'num' not in st.session_state:
    st.session_state.num = 0
  # st.write(st.session_state)
  for area in areas:
    placeholder = st.empty()
    num = st.session_state.num
    # st.write(area)
    # cols = st.columns(4)
    with placeholder.form(key=f"form_{num}"):
      st.write(areas[num].upper())
      for pregunta in preguntas:
        # cols[0].write(pregunta)
        st.write(pregunta)
        cols = st.columns(3)
        for i, alternativa in enumerate(alternativas):
          session_variable = area+"_"+pregunta+"_"+alternativa
          # session_puntaje = area+"_"+pregunta+"_"+alternativa+"_puntaje"
          if session_variable not in st.session_state:
              st.session_state[session_variable] = False
              # st.session_state[session_puntaje] = 0
          # cols[i+1].checkbox(label=alternativa.capitalize(), value=st.session_state[session_variable], key=session_variable, on_change=asignar,args=[session_variable,])
          # st.checkbox(label=alternativa.capitalize(), value=st.session_state[session_variable], key=session_variable, on_change=asignar,args=[session_variable,])
          cols[i].checkbox(label=alternativa.capitalize(), key=session_variable, value=st.session_state[session_variable])
    
      submit = st.form_submit_button(label="Siguiente", on_click=imprimir_sesion_state)
      if submit:
        st.session_state.num += 1
        if st.session_state.num >= 2:
            st.session_state.num = 0 
        placeholder.empty()
      else:
        # pass
        st.stop()


def asignar(llave):
    opcion = llave.split("_")[2]
    area_preg = llave.split("_")[0]+"_"+ llave.split("_")[1]

    if opcion == "agrado":
        st.session_state[area_preg+"_"+"indiferente"] = False
        st.session_state[area_preg+"_"+"desagrado"] = False
        if st.session_state[area_preg+"_"+"agrado"]:
            st.session_state[area_preg+"_"+"agrado_puntaje"] += 1
            if st.session_state[area_preg+"_"+"indiferente_puntaje"] > 0:
                st.session_state[area_preg+"_"+"indiferente_puntaje"] -= 1
            if st.session_state[area_preg+"_"+"desagrado_puntaje"] > 0:
                st.session_state[area_preg+"_"+"desagrado_puntaje"] -= 1
        else:
            st.session_state[area_preg+"_"+"agrado_puntaje"] -= 1

    if opcion == "indiferente":
        st.session_state[area_preg+"_"+"agrado"] = False
        st.session_state[area_preg+"_"+"desagrado"] = False
        if st.session_state[area_preg+"_"+"indiferente"]:
            st.session_state[area_preg+"_"+"indiferente_puntaje"] += 1
            if st.session_state[area_preg+"_"+"agrado_puntaje"] > 0:
                st.session_state[area_preg+"_"+"agrado_puntaje"] -= 1
            if st.session_state[area_preg+"_"+"desagrado_puntaje"] > 0:
                st.session_state[area_preg+"_"+"desagrado_puntaje"] -= 1
        else:
            st.session_state[area_preg+"_"+"indiferente_puntaje"] -= 1

    if opcion == "desagrado":
        st.session_state[area_preg+"_"+"agrado"] = False
        st.session_state[area_preg+"_"+"indiferente"] = False
        if st.session_state[area_preg+"_"+"desagrado"]:
            st.session_state[area_preg+"_"+"desagrado_puntaje"] += 1
            if st.session_state[area_preg+"_"+"indiferente_puntaje"] > 0:
                st.session_state[area_preg+"_"+"indiferente_puntaje"] -= 1
            if st.session_state[area_preg+"_"+"agrado_puntaje"] > 0:
                st.session_state[area_preg+"_"+"agrado_puntaje"] -= 1
        else:
            st.session_state[area_preg+"_"+"desagrado_puntaje"] -= 1


def generar_radiobuttons():
  areas = ['am','ic','ac']
  # areas = ['am']
  preguntas=['q1','q2','q3']
  alternativas = ['agrado','indiferente','desagrado']

  if 'num' not in st.session_state:
    st.session_state.num = 0
    # st.session_state.opt = False
    # cn.run()
    # result = st.session_state.result
    # survey = st.session_state.survey
  
  for area in areas:
    placeholder = st.empty()
    num = st.session_state.num
    with placeholder.form(key=str(num)):
      st.write(areas[num].upper())
      for i, pregunta in enumerate(preguntas):
          st.radio(f"{i+1}.- {pregunta}", key=f"radio_{area}_{pregunta}", options=alternativas, horizontal=True)

      if st.form_submit_button(label="Siguiente", on_click=imprimir_sesion_state):
        st.session_state.num += 1
        if st.session_state.num >= 3:
            st.session_state.num = 0 
        placeholder.empty()
      else:
        # pass
        st.stop()

def imprimir_sesion_state():
  st.write(st.session_state)


if __name__=='__main__':
    generar_checkbox()