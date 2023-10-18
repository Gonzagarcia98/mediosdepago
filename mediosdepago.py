import streamlit as st

col1, col2= st.columns([2,2])

with col2:

    with st.expander("Mercado Pago", True):
        st.write()
    with st.expander("PayWay", True):
        st.write()
    with st.expander("Modo", True):
        st.write()
    with st.expander("Uala", True):
        st.write()

with col1:

    st.write()