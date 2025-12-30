from nltk.corpus import stopwords
import re

## ========================= ##
#  Tokenize & normalize data  #
## ========================= ##

def clean_dataset(text):

    # Remove noise and normalize
    stop_words = set(stopwords.words("english"))

    text = text.lower()
    # Get rid of non words and extra space
    text = re.sub('\\W', ' ', text)
    text = re.sub('\n', '', text)
    text = re.sub(' +', ' ', text)
    text = re.sub('^ ', '', text)
    text = re.sub(' $', '', text)
    text = " ".join([word for word in text.split() if word not in stop_words])
    #Convert nbr text into

    return text


def comp_Processing(competence):

    # Create a new columns with the cleaned answer
    competence.loc[:, 'competency_name_clean'] = competence['competency_name'].apply(clean_dataset)
    competence.loc[:, 'description_clean'] = competence['description'].apply(clean_dataset)
    competence.loc[:, 'keyword_clean'] = competence['keywords'].apply(clean_dataset)

    competence_texts = (competence['competency_name_clean'] + " " + competence['description_clean'] + " " + competence['keyword_clean']).tolist()

    return competence_texts


def QCM_Processing(df_QCM):

    # Create a new columns with the cleaned answer
    df_QCM.loc[:, 'Output_cleaned'] = df_QCM['Answer'].apply(clean_dataset)
    df_QCM.loc[:, 'question_cleaned'] = df_QCM['Question'].apply(clean_dataset)

    question_anwser = []
    for idx, val in df_QCM.iterrows():
        if idx>=2 and idx<=9 and int(df_QCM.iloc[idx,1])>6:
            text = df_QCM.iloc[idx,0] + ' ' + df_QCM.iloc[idx,1]
            question_anwser.append(text)
        else :

              question_anwser.append(df_QCM.iloc[idx,1])

    return question_anwser




