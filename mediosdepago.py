import streamlit as st

st.title("Tarifas de medios de pago")

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
    st.write("Info sobre costos de Uala")
st.write("---")
