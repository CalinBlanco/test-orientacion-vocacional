import streamlit as st
from application import conn_data as cn, encuesta, resultado as result_page


def run():
  cn.run()
  result = st.session_state.result
  st.title('Test de Orientación Vocacional')
  st.markdown('<strong>IMPORTANTE: </strong><i>'+result.content['note']+'</i>', unsafe_allow_html=True)

  if 'num' not in st.session_state:
    st.session_state.curr_page = 0
    st.session_state.result_page = False
    st.session_state.num = 0

  with st.container():
    if st.session_state.result_page:
      result_page.run()
    else:
      encuesta.run()

