from cgitb import reset
from unittest.mock import patch
import streamlit as st
import pandas as pd

def run():
  if "result" not in st.session_state:
    st.session_state.result = get_results()
  if "survey" not in st.session_state:
    st.session_state.survey = get_survey()

def get_results():
  file = "results.json"
  path = '../dataset/'+file
  results = pd.read_json(path, orient='index',encoding = 'utf-8')
  # dataset = pd.read_json(path, orient='split',encoding = 'utf-8')
  # dataset.reset_index(inplace=True)
  return results

def get_survey():
  file = "survey.json"
  path = 'dataset/'+file
  survey = pd.read_json(path, orient='index',encoding = 'utf-8')
  # dataset = pd.read_json(path, orient='split',encoding = 'utf-8')
  # dataset.reset_index(inplace=True)
  return survey

def get_resultado():
  path = '../fuente/resultado_encuesta.csv'
  result = pd.read_csv(path, encoding = 'utf-8', sep=',')
  return result

# if __name__ == "__main__":
#     run()
