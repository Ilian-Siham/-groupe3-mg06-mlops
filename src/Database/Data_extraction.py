import pandas as pd 
import streamlit as st
import os 

@st.cache_data
def Load_job_dataset():
    """
    Docstring for data load
    """
    # Dynamique localisation of actual folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Define path for database
    base_path = os.path.join(current_dir, 'Job_database')
    job_path =  os.path.join(base_path, 'jobs.csv')

    try:
        # Lecture du fichier job
        job = pd.read_csv(job_path)
        return job
    
    except FileNotFoundError as e:
        st.error(f"Erreur : Le fichier de données job est manquant.{e}")
        return None
    
    except Exception as e:
        st.error(f"Une erreur inattendue est survenue lors du chargement du fichier job : {e}")
        return None
    
def Load_competence_dataset():
    """
    Docstring for data load
    """
    # Dynamique localisation of actual folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Define path for database
    base_path = os.path.join(current_dir, 'Job_database')
    competence_path =  os.path.join(base_path, 'competencies.csv')

    try:
        # Lecture des fichiers
        df_competence = pd.read_csv(competence_path)
        return df_competence
    
    except FileNotFoundError as e:
        st.error(f"Erreur : Le fichier de données competence est manquant.{e}")
        return None

    except Exception as e:
        st.error(f"Une erreur inattendue est survenue lors du chargement du fichier competence: {e}")
        return None
    

def Load_job_competence_dataset():
    """
    Docstring for data load
    """
    # Dynamique localisation of actual folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Define path for database
    base_path = os.path.join(current_dir, 'Job_database')
    job_competence_path =  os.path.join(base_path, 'job_competencies.csv')

    try:
        # Lecture des fichiers
        df_job_competence = pd.read_csv(job_competence_path)
        return df_job_competence
    
    except FileNotFoundError as e:
        st.error(f"Erreur : Un fichier de données job_competence est manquant.{e}")
        return None

    except Exception as e:
        st.error(f"Une erreur inattendue est survenue lors du chargement du fichier job_competence: {e}")
        return None
    

def Load_qcm_dataset():
    """
    Docstring for data load
    """
    # Dynamique localisation of actual folder
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Define path for database
    base_path = os.path.join(current_dir, 'Job_database')
    qcm_path = os.path.join(base_path, 'questionnary.csv')

    try:
        # Lecture des fichiers
        df_qcm = pd.read_csv(qcm_path, sep=';')

        return df_qcm
    
    except FileNotFoundError as e:
        st.error(f"Erreur : Le fichier de données qcm est manquant.{e}")
        return None

    except Exception as e:
        st.error(f"Une erreur inattendue est survenue lors du chargement du fichier qcm: {e}")
        return None