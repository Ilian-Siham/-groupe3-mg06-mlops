from src.Database.Data_extraction import Load_competence_dataset, Load_qcm_dataset
from src.Database.DataProcessing import comp_Processing, QCM_Processing
from src.Database.Load_final_corpus import save_comp_corpus, save_user_corpus

def run_data_skill_pipeline():

    print(" Start Data Pipeline...")

    # 1. Get datasets
    df_competence = Load_competence_dataset()
    print(df_competence)

    # 2. Transform data
    comp_corpus = comp_Processing(df_competence)

    # Final load
    save_comp_corpus(competence_corpus=comp_corpus)

    print(" Data Pipeline end with success.")

def run_data_user_pipeline():

    print(" Start Data Pipeline...")

    # 1. Get datasets
    df_qcm = Load_qcm_dataset()

    # 2. Transform data
    user_corpus = QCM_Processing(df_qcm)

    # Final load
    save_user_corpus(user_corpus=user_corpus)

    print(" Data Pipeline end with success.")



if __name__ == "__main__":
    run_data_skill_pipeline()


