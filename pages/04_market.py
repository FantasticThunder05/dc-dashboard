import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Mexico Market", layout="wide")

st.title("🇲🇽 Mexico DC Market Intelligence (U4)")

# Regional Data (Customized for your research)
market_data = pd.DataFrame({
    'Region': ['Querétaro', 'Estado de México', 'Nuevo León', 'Yucatán (Mérida)'],
    'Capacity (MW)': [150, 45, 30, 15],
    'Status': ['Primary Hub', 'Established', 'Growing', 'Emerging']
})

st.subheader("Data Center Capacity by Region (2026)")
fig = px.bar(market_data, x='Region', y='Capacity (MW)', color='Status',
             title="Installed Capacity in MW",
             color_discrete_sequence=px.colors.qualitative.Antique)
st.plotly_chart(fig, use_container_width=True)

st.info("**Insight:** Querétaro holds 70% of the hyperscale market, but Mérida is growing due to submarine cable proximity.")