import pandas as pd 
import os

def save_user_corpus(user_corpus,  output_dir=None):
    """
    Docstring for save_final_corpus

    :param user_corpus: Corpus questionnary
    :param output_dir: output directory
    """

    # If no output_dir specified, use the default path
    if output_dir is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_dir, 'Corpus_database')

    # Création of output path if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Transform list in DataFrame to save the corpus
    df_user = pd.DataFrame({'processed_text': user_corpus})

    # File path
    user_path = os.path.join(output_dir, 'user_corpus.csv')

    # Save Final load
    df_user.to_csv(user_path, index=False, sep=';', encoding='utf-8')

    print(f"Corpus sauvegardés avec succès dans : {output_dir}")
    return user_path



def save_comp_corpus( competence_corpus, output_dir=None):
    """
    Docstring for save_final_corpus

    :param competence_corpus: Corpus competency
    :param output_dir: output directory
    """

    # If no output_dir specified, use the default path
    if output_dir is None:
        current_dir = os.path.dirname(os.path.abspath(__file__))
        output_dir = os.path.join(current_dir, 'Corpus_database')

    # Création of output path if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Transform list in DataFrame to save the corpus
    df_comp = pd.DataFrame({'processed_text': competence_corpus})

    # File path
    comp_path = os.path.join(output_dir, 'competence_corpus.csv')

    # Save Final load
    df_comp.to_csv(comp_path, index=False, sep=';', encoding='utf-8')

    print(f"Corpus sauvegardés avec succès dans : {output_dir}")
    return comp_path
