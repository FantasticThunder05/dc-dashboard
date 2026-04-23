import streamlit as st

st.set_page_config(page_title="Security Standards", layout="wide")

st.title("Security & Compliance (U3)")
st.markdown("### Infrastructure Standards & Physical Controls")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Physical Security Checklist")
    st.checkbox("Biometric Access (Mantrap)", value=True)
    st.checkbox("CCTV 24/7 Monitoring", value=True)
    st.checkbox("Fire Suppression (Inergen/FM200)", value=True)
    st.checkbox("Water Leak Detection", value=True)

with col2:
    st.subheader("Standards & Certifications")
    st.success("**TIA-942:** Rated 3 (Concurrently Maintainable)")
    st.success("**ISO 27001:** Information Security Management")
    st.info("**SLA Commitment:** 99.982% Availability")

st.divider()
st.caption("Note: Compliance audits performed annually for Tier III validation.")