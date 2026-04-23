import streamlit as st
import pandas as pd
import numpy as np
from plotly import graph_objects as go

st.set_page_config(page_title="Data Center Operations", layout="wide")

st.title("Data Center Operations (U3)")

# Metrics: Uptime SLA Gauges
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Global Uptime", "99.992%", "0.001%")
with col2:
    st.metric("Active Incidents", "2", "-1")
with col3:
    st.metric("MAC Processes", "14", "4")

st.divider()

# Incident Log (Customized Data)
st.subheader("Recent Incident Log")
incident_data = pd.DataFrame({
    'Timestamp': ['2026-04-21 14:20', '2026-04-22 09:15', '2026-04-22 18:40'],
    'Severity': ['Critical', 'Low', 'Medium'],
    'System': ['Cooling Unit 4', 'Network Switch B1', 'UPS Backup'],
    'Status': ['Resolved', 'Investigating', 'In Progress']
})
st.table(incident_data)