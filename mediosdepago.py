import streamlit as st

# Add the background CSS using st.markdown
st.markdown(
    """
    <style>
        body {
            background-image: url("https://github.com/Gonzagarcia98/mediosdepago/blob/main/imagenes/TARIFAS%20UALA%201.png");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# The rest of your Streamlit app content
st.title("Streamlit App with Background Image")
st.write("This is the main content of your app.")


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
with st.expander("Desplegar información", False):
    st.image("imagenes/TARIFAS UALA 1.png")
    st.image("imagenes/TARIFAS UALA 2.png")
    st.write("Para más información ingresar en https://www.ualabis.com.ar/")
st.write("---")
