import streamlit as st

col1, col2= st.columns([2,2])

with col2:

    with st.expander("Mercado Pago", True):
        st.write("Info sobre costos de Mercado Pago")
    with st.expander("PayWay", True):
        st.write("Info sobre costos de PayWay")
    with st.expander("Modo", True):
        st.write("Info sobre costos de Modo")
    with st.expander("Uala", True):
        st.write("Info sobre costos de Uala")

with col1:

    st.write()