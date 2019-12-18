import sys
# import numpy as np
import pandas as pd
from sqlalchemy import create_engine
import pickle

# import nltk
# nltk.download(['punkt', 'wordnet'])
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier #, GradientBoostingClassifier
# from sklearn.ensemble.weight_boosting import AdaBoostClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split#, GridSearchCV
from sklearn.metrics import classification_report
# from sklearn.multioutput import MultiOutputClassifier


def load_data(database_filepath):
    """
    INPUT:
        database_filepath - Name of SQLite file to load dataframe from
        
    OUTPUT:
        X - Input Features
        Y - Target labels
        category_names - Column names for target labels
    """
    engine = create_engine('sqlite:///{0}'.format(database_filepath))
    df = pd.read_sql_table("Message", con=engine)
    X = df.message.values

    non_cat = ["id", "message", "original", "genre"]
    Y = df.drop(columns=non_cat).values
    category_names = df.drop(columns=non_cat).columns

    return X, Y, category_names


def tokenize(text):
    """
    INPUT:
        text - Single message as text string 
        
    OUTPUT:
        clean_tokens - Cleaned, normalized, tokenized and lemmatized words
    """
    tokens = word_tokenize(text)
    lemmatizer = WordNetLemmatizer()

    clean_tokens = []
    for tok in tokens:
        clean_tok = lemmatizer.lemmatize(tok).lower().strip()
        clean_tokens.append(clean_tok)

    return clean_tokens


def build_model():
    """
    INPUT:
        None
        
    OUTPUT:
        pipeline - Classification model pipeline
    """
    pipeline = Pipeline([
            ("vect", CountVectorizer(tokenizer=tokenize)),
            ("tfidf", TfidfTransformer()),
            ("clf", RandomForestClassifier()),
        ])

    return pipeline


def evaluate_model(model, X_test, Y_test, category_names):
    """
    INPUT:
        model - Trained classification model
        X_test - Input Features (test data only)
        Y_test - Target labels (test data only)
        category_names - Column names for target labels
        
    OUTPUT:
        None
    """
    Y_pred = model.predict(X_test)

    for i, col in enumerate(category_names):
        print("\n\n#########\n\n")
        print("{0}: {1}\n".format(i, col))
        print(classification_report(Y_test[i], Y_pred[i]))


def save_model(model, model_filepath):
    """
    INPUT:
        model - Trained classification model
        model_filepath - Filepath (including filename) for model pickle file
        
    OUTPUT:
        None
    """
    with open(model_filepath, "wb") as p:
        pickle.dump(model, p)


def main():
    if len(sys.argv) == 3:
        database_filepath, model_filepath = sys.argv[1:]
        print('Loading data...\n    DATABASE: {}'.format(database_filepath))
        X, Y, category_names = load_data(database_filepath)
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)
        
        print('Building model...')
        model = build_model()
        
        print('Training model...')
        model.fit(X_train, Y_train)
        
        print('Evaluating model...')
        evaluate_model(model, X_test, Y_test, category_names)

        print('Saving model...\n    MODEL: {}'.format(model_filepath))
        save_model(model, model_filepath)

        print('Trained model saved!')

    else:
        print('Please provide the filepath of the disaster messages database '\
              'as the first argument and the filepath of the pickle file to '\
              'save the model to as the second argument. \n\nExample: python '\
              'train_classifier.py ../data/DisasterResponse.db classifier.pkl')


if __name__ == '__main__':
    main()