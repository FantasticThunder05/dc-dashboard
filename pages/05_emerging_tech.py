import streamlit as st

st.set_page_config(page_title="Future Tech", layout="wide")

st.title("Emerging Technologies (U4)")
st.subheader("Technology Adoption Radar 2026-2030")

t1, t2 = st.columns(2)

with t1:
    st.write("#### High Priority (Now)")
    st.warning("Liquid Cooling (DLC)")
    st.markdown("- Essential for AI workloads and high-density racks (>30kW).")
    
    st.warning("Edge Computing")
    st.markdown("- Decentralized nodes for 5G and IoT latency reduction.")

with t2:
    st.write("#### Emerging (Future)")
    st.info("Hydrogen Fuel Cells")
    st.markdown("- Replacing diesel generators for sustainable backup power.")
    
    st.info("Quantum Readiness")
    st.markdown("- Preparing cooling and security for quantum processors.")

st.error("**Strategic Recommendation:** Implement AI-driven DCIM for predictive maintenance by Q4 2026.")