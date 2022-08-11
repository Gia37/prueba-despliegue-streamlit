import streamlit as st

headerSection = st.container()
mainSection = st.container()
LeftNav = st.sidebar

with headerSection:
    st.title('Prueba Streamlit')
    st.markdown('Esta es una prueba para hacer un despliegue')

with mainSection:
    left_col, right_col = st.columns(2)

    with left_col:
        st.header('Columna izquierda')
        st.markdown('Columna izquierda')
        textValue = st.text_input('Ingresar texto', '')
        st.write(textValue)

    with right_col:
        st.header('Columna derecha')
        st.markdown('Columna derecha')

with LeftNav:
    st.button('menu1', on_click=lambda: st.success('menu1'))
    st.button('menu2', on_click=lambda: st.success('menu2'))