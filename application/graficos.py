import streamlit as st
import conn_data as cn
import plotly.express as px

def run():
  _,col,_ = st.columns([1,1,1])
  with col:
    st.markdown("<h1>Resultados</h1>", unsafe_allow_html=True)
  st.balloons()
  resultado_tabla = cn.get_resultado()
  # st.write(resultado_tabla)
  grafico(resultado_tabla)


def grafico(df):
  fig = px.bar(df, x="index", y="total", color="index", text_auto=True)
  fig.update_xaxes(title_text="Orientación Vocacional")
  fig.update_yaxes(title_text="Total")
  fig.update_layout(
    # title_text="Resultados Numéricos de la encuesta",
    showlegend=False
  )
  # fig.show()
  st.plotly_chart(fig)

  # st.write(df['index'].head(1)[0])
  get_resultado_carreras(df['index'].head(1)[0])

def get_resultado_carreras(index):
  resultado_carreras = cn.get_results()
  resultado_carreras.reset_index(inplace=True)
  st.markdown("<h3>Interpretación del resultado:</h3>", unsafe_allow_html=True)
  st.write(f"Obtuviste mayor puntaje en en área de {index.upper()}")
  st.caption(f"{index.upper()}, quiere decir que tienes {resultado_carreras['description'].loc[resultado_carreras['index'] == index].values[0]}.")
  with st.expander(f"Más iformación sobre {index.upper()}"):
    st.write(f"{resultado_carreras['content'].loc[resultado_carreras['index'] == index].values[0]}.")
  
  carreras = resultado_carreras['careers'].loc[resultado_carreras['index'] == index].values[0]
  with st.expander(f"Carreras relacionadas con {index.upper()}"):
    for carrera in carreras:
      st.write(f"- {carrera.capitalize()}")
  # st.write(resultado_carreras.loc[resultado_carreras['index'] == index])



if __name__=='__main__':
    run()