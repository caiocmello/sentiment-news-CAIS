import os
import os

_path = os.path.dirname(__file__)

_error_message = '''
Please provide a text as an input.
You can either provide the text as an argument: python -m subjectivity.classify this is my opinion.
Or pipe the text from the command line: python -m subjectivity.classify < data/random_text.txt
'''

from subjectivity_classifier import SubjectivityClassifier
print(_path)
classifier = SubjectivityClassifier(model_filename=os.path.join(_path, '..','data/save/subj-29.tf'),
                                    word_filename=os.path.join(_path, '..','data/word_embeddings/glove.6B.50d.txt'))

def _aggregate_sentence(args):
    return_str = ''
    for argument in args:
        return_str += argument + ' '
    return return_str


def _get_subj_or_obj_sentences_from_text(text):
    return classifier.classify_sentences_in_text(text)


def print_sentences(sentences_dict):
    print('\nOBJECTIVE SENTENCES:')
    [print(item) for item in sentences_dict['objective']]
    print('\nSUBJECTIVE SENTENCES:')
    [print(item) for item in sentences_dict['subjective']]

def get_final_subjectivity_classification(text):
    classification_result = _get_subj_or_obj_sentences_from_text(text)
    final_subjectivity_class = []
    if len(classification_result["subjective"])>0:
        final_subjectivity_class.append("subjective")
    if len(classification_result["objective"])>0:
        final_subjectivity_class.append("objective")

    return ",".join(final_subjectivity_class)

def get_final_subjectivity_text(text):
    classification_result = _get_subj_or_obj_sentences_from_text(text)
    final_subjectivity_text = []
    if len(classification_result["subjective"])>0:
        final_subjectivity_text.append("subjective: "+ " ".join(classification_result["subjective"]))
    if len(classification_result["objective"])>0:
        final_subjectivity_text.append("objective: "+ " ".join(classification_result["objective"]))

    return ",".join(final_subjectivity_text)

if __name__ == '__main__':
    import os
    import sys
    import pandas as pd

    df = pd.read_csv("data/guardian_london.csv")
    df["subjectivity_label"] = df["Title"].astype(str).apply(get_final_subjectivity_classification)
    df["subjectivity_text"] = df["Title"].astype(str).apply(get_final_subjectivity_text)
    df.to_csv("data/guardian_london_subjectivity.csv",index=False)
    
   