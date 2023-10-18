import streamlit as st

st.markdown("<h1 style='text-align: center; font-size: 54px; font-family: Verdana, sans-serif;'>Tarifas de medios de pago</h1>", unsafe_allow_html=True)

st.write("---")
st.image("imagenes/MERCADOPAGO.png")
with st.expander("Mercado Pago", False):
    st.write("Info sobre costos de Mercado Pago")
st.write("---")

st.image("imagenes/PAYWAY.png")
with st.expander("PayWay", False):    
    st.write("Info sobre costos de PayWay")
st.write("---")

st.image("imagenes/MODO.png")
with st.expander("Modo", False):
    st.write("Info sobre costos de Modo")
st.write("---")

st.image("imagenes/UALA.png")
with st.expander("Uala", False):
    st.image("imagenes/TARIFAS - UALA.png")
    st.write("Para más información ingresar en https://www.ualabis.com.ar/")
st.write("---")
