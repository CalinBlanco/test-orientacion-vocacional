# import SessionState
import streamlit as st
import io
# from application import conn_data as cn

st.set_page_config(
    page_icon=":shark:",
    layout="wide",

)

def pageZero(sesh):
    st.title('This is page zero! welcome')
    st.write('some text for zeroth page. Welcome to the app. Follow the nav buttons above to move forward and backwards one page')

def pageOne(sesh):
    st.title('page ONE')
    st.write('one')

def pageTwo(sesh):
    st.title('TWO')
    st.write('two')

if "curr_page" not in st.session_state:
#   sesh = SessionState.get(curr_page = 0)
  st.session_state.curr_page = 0

PAGES = [pageZero, pageOne, pageTwo]

def main():
    ####SIDEBAR STUFF
    # st.sidebar.title("this is an app:")

    # st.sidebar.markdown('Might be easier to import the pageOne/pageTwo/pageThree from a separate file to make the code cleaner')

    #####MAIN PAGE NAV BAR:
    st.markdown(' ### Navigation')
    st.markdown('Click Next to go to the next page')
    if st.button('Back'):
        if st.session_state.curr_page >0:
            st.session_state.curr_page -= 1
    if st.button('Next page'):
        # sesh.curr_page = min(len(PAGES)-1, sesh.curr_page+1)
        if st.session_state.curr_page <len(PAGES)-1:
            st.session_state.curr_page += 1
    
    st.slider('', 0, len(PAGES)-1, st.session_state.curr_page)

    st.markdown('----------------------------------')


    #####MAIN PAGE APP:
    st.write('PAGE NUMBER:', st.session_state.curr_page)
    page_turning_function = PAGES[st.session_state.curr_page]
    # st.write(st.session_state.curr_page)
    page_turning_function(st.session_state.curr_page)

def otro():
    areas=['ml','ic']
    preguntas = ['q1', 'q2']

    data=[]
    for area in areas:
        for pregunta in preguntas:
            item = {area: pregunta}
            print(item[area])
            # if area.pregunta == pregunta:
            #     item[area.pregunta.name] = pregunta.value
        data.append(item)
        # print(data)
    # print(data)
    # st.write(st.session_state)


    if 'a' not in st.session_state:
        st.session_state.a = 0
        st.session_state.b = 0
        st.session_state.c = 0

    def cambiar_agrada():
        st.session_state.a,st.session_state.b,st.session_state.c = 1,0,0
    def cambiar_indiferente():
        st.session_state.a,st.session_state.b,st.session_state.c = 0,1,0
    def cambiar_desagrada():
        st.session_state.a,st.session_state.b,st.session_state.c = 0,0,1
    
    col1, col2, col3, col4, col5 = st.columns([1,4,1,1,1])

    with col1:
        st.write("1")
    with col2:
        if "Me agrada" or "Indiferente" or "Me desagrada":
            st.write('You selected: ',st.session_state.a*'Me agrada',st.session_state.b*'Indiferente',st.session_state.c*'Me desagrada')
        else:
            st.write('No selection')

    with col3:
        st.checkbox('Me agrada', value = st.session_state.a, on_change = cambiar_agrada)
    with col4:
        st.checkbox('Indiferente', value = st.session_state.b, on_change = cambiar_indiferente)
    with col5:
        st.checkbox('Me desagrada', value = st.session_state.c, on_change = cambiar_desagrada) 

def formulario_session_state():
    """
    Todo list app
    """
    st.title("Todo list app")

    # 1. Create a variable to store todos.
    if not 'todolist' in st.session_state:
        st.session_state.todolist = []

    # 2. Prompt the user in the form
    with st.form(key='form'):
        todo = st.text_input(label='Enter todo description')
        is_submit = st.form_submit_button('submit')

    # 3. Store todo in todolist when submit button is hit.
    if is_submit:
        st.session_state.todolist.append(todo)
        
    # 4. Display the contents of todolist
    with st.expander(label='List of todos', expanded=True):
        for i, todo_text in enumerate(st.session_state.todolist):
            st.checkbox(label=f'{todo_text}', key=i)


if __name__=='__main__':
    main()