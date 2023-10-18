import streamlit as st


st.image("imagenes/MERCADOPAGO.png")
with st.expander("Mercado Pago", False):
    st.write("Info sobre costos de Mercado Pago")

st.image("imagenes/PAYWAY.png")
with st.expander("PayWay", False):    
    st.write("Info sobre costos de PayWay")

st.image("imagenes/MODO.png")
with st.expander("Modo", False):
    st.write("Info sobre costos de Modo")

st.image("imagenes/UALA.png")
with st.expander("Uala", False):
    st.write("Info sobre costos de Uala")
