import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
from src.Model.ModelPrediction import Build_semantic_model
from src.Database.Data_extraction import Load_job_dataset

def Visualize():
    st.title("🎯 Your Job Profile Analysis")
    st.markdown("___")

    """
    # === Load data and metrics === #
    with st.spinner("Analyzing your profile with Semantic AI..."): 
        #######################################################
        ##   read the result of prediction in st.state[]     ##
        
        # Call the function to analyze the user profile
        df_skill, df_byjob = Build_semantic_model()

        ##                                                   ##
        #######################################################
    """

    # Check if the results are already there
    if 'results' not in st.session_state:
        st.warning("No data to display. Please complete the questionnaire.")
        return

    # Get the stocked data
    data = st.session_state['results']
    df_byjob = pd.DataFrame(data["job_matches"])
    df_skill = pd.DataFrame(data["skills_details"])

    # Load reference tables
    job = Load_job_dataset()

    # === Prepare data for the Top Job description === #
    df_byjob = df_byjob.merge(job, on='job_id', how='left')

    # Select top jobs by coverage score
    maxJscore = df_byjob.sort_values(by='coverage_score', ascending=False).iloc[:6]
    top_job = maxJscore.iloc[0]
    nameJ = top_job['job_title']
    scoreJ = top_job['coverage_score']
    Jid = top_job['job_id']

    # df_skill already contains competency_name, no need to merge again
    # Filter competencies for the top job
    target_skills = (
        df_skill[df_skill['job_id'] == Jid]
        .sort_values(by='similarity score', ascending=False)
        #.drop_duplicates(subset='competency_id')
        .iloc[:8]  # Top 8 competencies
    )

    # === Streamlit page layout === #
    st.title("Your Job Profile!")
    st.header("Result of your job profile:")
    st.markdown("---")

    # Two columns: Pie chart + description
    col1, col2 = st.columns([1, 1])

    with col1:
        # Donut Chart of the top jobs
        fig = px.pie(
            maxJscore,
            values='coverage_score',
            names='job_title',
            hole=0.4,
            title="Top Job Matches",
            color_discrete_sequence=px.colors.sequential.RdBu
        )
        fig.update_traces(textinfo='percent+label')
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Add a description text
        st.write("### Recommended Role")
        st.metric(label="Primary Match", value=nameJ, delta=f"{scoreJ*100}% Match")
        st.info(f"""
Based on our analysis, your skills align most closely with the **{nameJ}** profile.
This score reflects the coverage of your against the industry requirements for this role.
                """)
    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Job comparaison --- #
    st.subheader("Market Comparaison")
    df_byjob_sorted = df_byjob.sort_values(by='coverage_score')

    # Horizontal bar chart of job coverage scores
    fig2, ax2 = plt.subplots(figsize=(7, 4))
    plt.hlines(y=df_byjob_sorted['job_title'], xmin=0, xmax=df_byjob_sorted['coverage_score'], color='skyblue')
    plt.plot(df_byjob_sorted['coverage_score'], df_byjob_sorted['job_title'], "o")
    ax2.set_xlabel("Coverage Score")
    ax2.set_title("How you match other Data & AI roles")
    st.pyplot(fig2)

    st.markdown("---")
    st.markdown("<br>", unsafe_allow_html=True)

    # --- competencies information for the top job --- #
    st.subheader(f"Competency Breakdown for {nameJ}")

    fig3, ax3 = plt.subplots(figsize=(8, 4))
    sns.barplot(
        y='competency_name',
        x='similarity score',
        data=target_skills,
        palette='ch:start=.2,rot=-.3',
        ax=ax3
    )
    ax3.set_xlabel("Competency Score")
    ax3.set_ylabel("Competency Name")
    ax3.set_title(f"Top Competencies for {nameJ}")
    st.pyplot(fig3)


# Main execution
if __name__ == "__main__":
    Visualize()
