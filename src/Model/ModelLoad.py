from sentence_transformers import SentenceTransformer

# Stock global variable
_model = None

def get_semantic_model():
    global _model
    if _model is None:
        # Load model one time after the start of API
        print("Load modèle...")
        _model = SentenceTransformer("all-mpnet-base-v2")
    return _model


'''
Look How the model do to load one time only
'''