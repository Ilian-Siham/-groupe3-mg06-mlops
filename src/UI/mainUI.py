import streamlit as st
from src.UI import Questionnaire_logic, Visualize_streamlit

st.set_page_config(page_title="Data & AI Career Path", layout="wide")

def main():
    # --- INITIALISATION ---
    if 'page' not in st.session_state:
        st.session_state['page'] = 'questionnaire' # On définit la page par défaut
    if 'results' not in st.session_state:
        st.session_state['results'] = None

    # --- LOGIQUE DE NAVIGATION ---
    if st.session_state['page'] =='questionnaire':
        # Call the questionnary form
        Questionnaire_logic.render_form()

    elif st.session_state['page'] == 'visualize':
        # Call the result page
        Visualize_streamlit.Visualize()

        st.markdown("---")
        if st.button("Back to quize"):
            st.session_state['page'] = 'questionnaire'

            # resets the results for a new test
            st.session_state['results'] = None
            st.rerun()

if __name__ == "__main__":
    main()
