import streamlit as st



dashboard = st.Page("fitur/dashboard.py", title="dashboard")
kerkom = st.Page("fitur/kerkom.py", title="aplikasi parkir")

pg = st.navigation(
    {
        "menu utama": [dashboard],
        "menghitung biaya parkir": [kerkom],
    }
)

if 'riwayat' not in st.session_state:
    st.session_state['riwayat'] =[]

pg.run()