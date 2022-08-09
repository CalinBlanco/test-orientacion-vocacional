import streamlit as st
from application import conn_data as cn

def run():
    cn.run()
    result = st.session_state.result
    survey = st.session_state.survey
    st.title('Test de Orientación Vocacional')
    # st.markdown(result.content['note'])
    st.markdown('<strong>IMPORTANTE: </strong><i>'+result.content['note']+'</i>', unsafe_allow_html=True)
  
    with st.form("my_form"):
        for i in range(len(survey.columns)):
            indice = survey.index[i]
            # st.write(survey.loc[indice][0])

            respuesta = st.radio(
                str(i+1)+".- "+ survey.loc[indice][i+1],
            ('Agrado', 'Indiferente', 'Desagrado'))

            if respuesta == 'Agrado':
                st.write('Seleccionaste Agrado.')
            elif respuesta == 'Indiferente':
                st.write('Seleccionaste Indiferente.')
            else:
                st.write('Seleccionaste Desagrado.')

            if i==7:
                break

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider")