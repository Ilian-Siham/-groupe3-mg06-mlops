import streamlit as st
import pandas as pd
from datetime import datetime
import os
import requests


def render_form():
    """
    Data & AI Skills Assessment Questionnaire
    Returns a CSV file with questions and answers in two columns
    """

    # Main title
    st.title("Data & AI Skills Assessment Questionnaire")
    st.subheader("Made by : \nIlian ALI BOTO, Sarah SHAHIN, Hafsa REDOUANE, Najlaa ALLIOUI ")
    st.markdown("---")

    # Session state initialization
    if 'submitted' not in st.session_state:
        st.session_state.submitted = False

    # Main form
    with st.form("skills_assessment"):
        
        # === IDENTIFICATION === #
        st.header("Identification")
        user_id = st.text_input("Enter your email or unique identifier*", placeholder="example@email.com")
        st.markdown("---")
        
        # === GENERAL SKILLS === #
        st.header("General Skills")
        q2 = st.number_input("How many years have you been working in Data/AI?", 
                             min_value=0, max_value=50, value=0, step=1)
        
        st.markdown("---")
        
        # === SKILLS ASSESSMENT === #
        st.header("Skills Assessment")
        col1, col2 = st.columns(2)
        
        with col1:
            q3 = st.slider("Data Analysis", 1, 10, 5, key="q3")
            q4 = st.slider("Data Engineering", 1, 10, 5, key="q4")
            q5 = st.slider("Machine Learning / AI", 1, 10, 5, key="q5")
            q10 = st.slider("Big Data and Cloud platforms (Hadoop, Spark, AWS, Azure, GCP)", 1, 10, 5, key="q10")
        
        with col2:
            q15 = st.slider("Data Visualization / BI (Power BI, Tableau, Superset...)", 1, 10, 5, key="q15")
            q17 = st.slider("Statistics and probabilities", 1, 10, 5, key="q17")
            q20 = st.slider("NLP / Computer Vision", 1, 10, 5, key="q20")
        
        st.markdown("---")
        
        # === LANGUAGES AND TOOLS === #
        st.header("Languages and Tools")
        
        q6 = st.multiselect(
            "Programming languages mastered",
            ["Python", "R", "SQL", "Java", "C++", "JavaScript", "Scala", "Julia", "Other"],
            default=[]
        )
        
        q7 = st.text_area(
            "For each language, indicate your level from 1 to 10",
            placeholder="Example: Python:8, SQL:7, R:6",
            height=80
        )
        
        q8 = st.text_area(
            "Libraries / Frameworks used",
            placeholder="Pandas, Numpy, TensorFlow, PyTorch, Scikit-learn, Spark...",
            height=80
        )
        
        q9 = st.multiselect(
            "Databases used",
            ["MySQL", "PostgreSQL", "MongoDB", "Oracle", "SQL Server", "SQLite", "Redis", "Cassandra", "Other"],
            default=[]
        )
        
        q16 = st.text_area(
            "Visualization tools used",
            placeholder="Matplotlib, Seaborn, Power BI, Tableau, Plotly...",
            height=80
        )
        
        q19 = st.multiselect(
            "Workflow / versioning tools",
            ["Git", "Airflow", "Docker", "Kubernetes", "Jenkins", "GitLab CI/CD", "MLflow", "Other"],
            default=[]
        )
        
        st.markdown("---")
        
        # === PROJECTS === #
        st.header("Projects")
        
        q12 = st.text_area(
            "Data Analysis Project (objective, tools, results)",
            placeholder="Describe a significant Data Analysis project...",
            height=120
        )
        
        q13 = st.text_area(
            "Data Engineering Project (objective, tools, results)",
            placeholder="Describe a significant Data Engineering project...",
            height=120
        )
        
        q14 = st.text_area(
            "Machine Learning / AI Project (objective, tools, results)",
            placeholder="Describe a significant ML/AI project...",
            height=120
        )
        
        st.markdown("---")
        
        # === CROSS-FUNCTIONAL SKILLS AND PROFILE === #
        st.header("Cross-functional Skills and Profile")
        
        q18 = st.text_area(
            "Cross-functional skills",
            placeholder="Communication, project management, critical thinking, leadership...",
            height=100
        )
        
        q21 = st.selectbox(
            "Which Data profile best describes you?",
            ["", "Data Analyst", "Data Scientist", "Data Engineer", "ML Engineer", "Data Architect", "Other"]
        )
        
        q22 = st.text_area(
            "Specific goals or interests in Data/AI for your upcoming projects",
            placeholder="Your ambitions, areas of interest, skills to develop...",
            height=100
        )
        
        st.markdown("---")
        
        # Submit button
        submitted = st.form_submit_button("Submit Questionnaire", use_container_width=True)
        
        if submitted:
            # Validation
            errors = []
            
            if not user_id:
                errors.append("Email or unique identifier is required")
            
            if not q6:
                errors.append("Please select at least one programming language")
            
            if not q7.strip():
                errors.append("Please indicate your level for each language")
            
            if not q8.strip():
                errors.append("Please list the libraries/frameworks you use")
            
            if not q9:
                errors.append("Please select at least one database")
            
            if not q16.strip():
                errors.append("Please list the visualization tools you use")
            
            if not q19:
                errors.append("Please select at least one workflow/versioning tool")
            
            if not q12.strip():
                errors.append("Please describe a Data Analysis project")
            
            if not q13.strip():
                errors.append("Please describe a Data Engineering project")
            
            if not q14.strip():
                errors.append("Please describe a Machine Learning/AI project")
            
            if not q18.strip():
                errors.append("Please describe your cross-functional skills")
            
            if not q21:
                errors.append("Please select your Data profile")
            
            if not q22.strip():
                errors.append("Please describe your goals or interests")
            
            # Display errors if any
            if errors:
                st.error("Please complete all required fields:")
                for error in errors:
                    st.warning(f"- {error}")
            else:
                
                # Create data in Question-Answer format
                questions_answers = [
                    ["Timestamp", datetime.now().strftime("%Y-%m-%d %H:%M:%S")],
                    ["Enter your email or unique identifier", user_id],
                    ["How many years have you been working in the Data/AI field?", str(q2)],
                    ["Rate your Data Analysis skills (1-10).", str(q3)],
                    ["Rate your Data Engineering skills (1-10).", str(q4)],
                    ["Rate your Machine Learning / AI skills (1-10).", str(q5)],
                    ["Rate your Big Data and Cloud platform experience (Hadoop, Spark, AWS, Azure, GCP) (1-10).", str(q10)],
                    ["Rate your Data Visualization / BI skills (Power BI, Tableau, Superset…) (1-10).", str(q15)],
                    ["Rate your Statistics and Probability skills (1-10).", str(q17)],
                    ["Rate your NLP / Computer Vision skills (1-10).", str(q20)],
                    ["Programming languages mastered (Python, R, SQL, Java, C++, Other).", ", ".join(q6)],
                    ["For each language, indicate your level from 1 to 10 (e.g., Python:8, SQL:6).", q7],
                    ["Libraries / Frameworks used (Pandas, Numpy, TensorFlow, PyTorch, Scikit-learn, Spark…).", q8],
                    ["Databases used (MySQL, PostgreSQL, MongoDB, Oracle, Other).", ", ".join(q9)],
                    ["Visualization tools used (Matplotlib, Seaborn, Power BI, Tableau, Other).", q16],
                    ["Workflow / versioning tools (Git, Airflow, Docker, Kubernetes, Other).", ", ".join(q19)],
                    ["Data Analysis project (goal, tools, results).", q12],
                    ["Data Engineering project (goal, tools, results).", q13],
                    ["Machine Learning / AI project (goal, tools, results).", q14],
                    ["Cross-functional skills (communication, project management, critical thinking…).", q18],
                    ["Which Data profile best describes you? (Data Analyst, Data Scientist, Data Engineer, Other).", q21],
                    ["Goals or specific interests in Data/AI for your future projects.", q22]

                    
                ]
                
                # Convert to DataFrame
                df = pd.DataFrame(questions_answers, columns=["Question", "Answer"])
                
                # Look for the database folder
                current_dir = os.path.dirname(os.path.abspath(__file__))
                src_dir = os.path.dirname(current_dir)
                Job_Database_dir = os.path.join(src_dir, 'Database','Job_database')
                file = os.path.join(Job_Database_dir, "questionnary.csv")

                # Save CSV (overwrite if exists)
                df.to_csv(file, index=False, encoding='utf-8', sep=';')

                try: 
                    with st.spinner("Analyzing your profile with Semantic AI..."):

                        # Call API for prediction
                        url_api = "http://localhost:8000/predict" ############## Change if needed ################
                        #url_api = "http://127.0.0.1:8000/predict" # Test local
                        response = requests.post(url_api)

                        if response.status_code == 200:
                            # Stock the result of prediction in streamlit session
                            st.session_state['results'] = response.json()

                            st.success('Questionnaire submitted successfully!')
                            st.balloons()
                            st.session_state.submitted = True
                            # Change page after submission
                            st.session_state['page']  = 'visualize'   
                            st.rerun()

                        else:
                            st.error("The API of prediction doesn't respond.")
                except Exception as e:
                    st.error(f"Détail de l'erreur : {e}")    

    # Outside form
    st.markdown("---")
    st.caption("*All fields marked with an asterisk are required*")