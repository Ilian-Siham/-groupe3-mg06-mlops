import pandas as pd
import numpy as np
import os
from sentence_transformers import util
from src.Database.Data_extraction import Load_competence_dataset, Load_job_competence_dataset
from src.Database.Data_pipeline import run_data_user_pipeline
from src.Model.ModelLoad import get_semantic_model


def similarity_score(answer_embed, skill_embed, df_competence):
    """
    Calcule la similarité de manière matricielle pour plus de rapidité.
    """
    # Calcule toutes les similarités d'un coup (Matrice : N réponses x M compétences)
    # On obtient un tenseur/array de scores
    cos_scores = util.cos_sim(answer_embed, skill_embed)

    # On transforme en DataFrame pour manipuler facilement
    # On prend souvent le max de similarité pour chaque compétence parmi toutes les réponses
    max_scores = cos_scores.max(dim=0).values.tolist()

    # Vérifier que les longueurs correspondent
    num_embeddings = len(max_scores)
    num_competences = len(df_competence)

    if num_embeddings != num_competences:
        print(f"Warning: Mismatch between embeddings ({num_embeddings}) and competences ({num_competences})")
        # Prendre le minimum pour éviter l'erreur
        min_len = min(num_embeddings, num_competences)
        max_scores = max_scores[:min_len]
        df_competence = df_competence.iloc[:min_len]

    # Reconstruction propre du DataFrame
    skill_results = pd.DataFrame({
        'competency_id': df_competence.iloc[:, 0].values,
        'competency_name': df_competence.iloc[:, 1].values,
        'block_weight': df_competence.iloc[:, 7].values,
        'similarity score': max_scores
    })

    return skill_results


def covscore(group):
    """
    Calcul pondéré du score de couverture. 
    Note : 'importance' doit être présent dans le groupement (via merge).
    """
    num = (group['block_weight'] * group['similarity score'] * group['importance']).sum()
    den = (group['block_weight'] * group['importance']).sum()
    return round(num/den, 3) if den != 0 else 0

def load_processed_data():

    # Call user data pipeline
    run_data_user_pipeline()

    # Look for the Corpus directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    src_dir = os.path.dirname(current_dir)
    corpus_dir = os.path.join(src_dir, 'Database', 'Corpus_database')

    comp_corpus_path = os.path.join(corpus_dir, 'competence_corpus.csv')
    user_corpus_path = os.path.join(corpus_dir, 'user_corpus.csv')

    try:
        df_user = pd.read_csv(user_corpus_path, sep=';')
        df_comp = pd.read_csv(comp_corpus_path, sep=';')
        
        # Convert into list
        user_texts = df_user['processed_text'].tolist()
        comp_texts = df_comp['processed_text'].tolist()
        
        return user_texts, comp_texts
    except FileNotFoundError:
        print(" Eroor : No corpus Found. Start Data Pipeline.")
        return [], []

def Build_semantic_model():

    # 1. Extraction et Processing
    competence = Load_competence_dataset()
    job_competence = Load_job_competence_dataset()

    question_answer , competence_texts = load_processed_data()

    # 2. Modèle et Encodage (Le convert_to_tensor permet d'utiliser le GPU si dispo)
    model = get_semantic_model()
    answer_embed = model.encode(question_answer, convert_to_tensor=True)
    skill_embed = model.encode(competence_texts, convert_to_tensor=True)

    # 3. Calcul de similarité
    skill = similarity_score(answer_embed, skill_embed, competence)

    # 4. Jointure et Scores finaux
    df_skill = skill.merge(job_competence, on=['competency_id'], how='left')
    print(df_skill.columns)
    # Calcul par métier
    df_byjob = df_skill.groupby('job_id', group_keys=False).apply(covscore, include_groups=False).reset_index(name='coverage_score')
    df_byjob = df_byjob.replace([np.inf, -np.inf], np.nan).fillna(0)

    # Clean result for JSON conversion
    df_byjob = df_byjob.replace([float('inf'), float('-inf')], 0).fillna(0)

    # Calcul par compétence (optionnel selon ton besoin)
    df_compS = df_skill.copy() # ou un autre groupement si nécessaire

    # Clean df_compS for JSON conversion
    df_compS = df_compS.replace([np.inf, -np.inf, float('inf'), float('-inf')], 0).fillna(0)

    return df_compS, df_byjob