import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mayab-Data Ops Intelligence", layout="wide")

# Personalización de colores (Estilo Dark/Pro)
st.markdown("""
    <style>
    .stApp { background-color: #0b0d11; color: white; }
    h1 { color: #00fbff; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.title("Navegación")
page = st.sidebar.radio("Ir a:", ["Market Intelligence (U4)", "DC Administration (U3)", "Calculadora Pro"])

if page == "Market Intelligence (U4)":
    st.title("Análisis de Mercado - Data Centers México")
    st.info("Fuente: DatacenterDynamics & Market Intelligence 2026")
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Inversión Estimada (MXN)", "$4.2B", "+15%")
    with col2:
        st.metric("Hub Principal", "Querétaro / Mérida", "Creciente")
    
    st.write("### Tendencias 2026")
    st.line_chart({"Inversión": [10, 25, 45, 80, 120]}) # Datos de ejemplo

elif page == "DC Administration (U3)":
    st.title("Administración & Cumplimiento")
    st.success("Estado: Operativo - Hunucmá Node")
    
    st.checkbox("Certificación TIER III - Activa")
    st.checkbox("Protocolo de Enfriamiento - OK")
    st.checkbox("Seguridad Física - Perímetro Activo")

elif page == "Calculadora Pro":
    st.title("  Herramienta de Ingeniería")
    st.write("Calculadora de PUE (Power Usage Effectiveness)")
    total = st.number_input("Energía Total (kW)", value=100)
    it = st.number_input("Energía IT (kW)", value=80)
    if it > 0:
        st.subheader(f"PUE Resultante: {total/it:.2f}")