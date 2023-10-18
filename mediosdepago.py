import streamlit as st



with st.expander("Mercado Pago", False):
    st.write("Info sobre costos de Mercado Pago")
with st.expander("PayWay", False):    
    st.write("Info sobre costos de PayWay")
with st.expander("Modo", False):
    st.write("Info sobre costos de Modo")
with st.expander("Uala", False):
    st.write("Info sobre costos de Uala")

st.write(
    """
    <style>
        .expander-label {
            font-size: 24px; /* Cambia el tamaño de la fuente según tus preferencias */
        }
        .expander-content {
            font-size: 18px; /* Cambia el tamaño de la fuente del contenido según tus preferencias */
        }
    </style>
    """
)

# Crear el expander
with st.expander("Expander con fuente personalizada", expanded=True):
    st.write("Este es el contenido del expander.")