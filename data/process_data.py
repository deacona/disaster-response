import sys
import pandas as pd
from sqlalchemy import create_engine


def load_data(messages_filepath, categories_filepath):
    """
    INPUT:
        messages_filepath - Filepath (including filename) for messages data file
        categories_filepath - Filepath (including filename) for categories data file
        
    OUTPUT:
        df - Dataframe of combined messages and categories data
    """

    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)

    df = pd.merge(messages, categories, on="id", how="inner")

    return df


def clean_data(df):
    """
    INPUT:
        df - Dataframe of combined messages and categories data
        
    OUTPUT:
        df - Dataframe of cleaned data
    """

    categories = df.categories.str.split(";", expand=True)

    row = categories.head(1)
    # use this row to extract a list of new column names for categories.
    category_colnames = row.apply(lambda x: x.str.split("-")[0][0]).values
    categories.columns = category_colnames

    for column in categories:
        # set each value to be the last character of the string
        categories[column] = categories[column].str[-1:]

        # convert column from string to numeric
        categories[column] = pd.to_numeric(categories[column])

    # replace any integers > 1 with 1
    categories.replace([2, 3, 4, 5, 6, 7, 8, 9], 1, inplace=True)

    df.drop(columns="categories", inplace=True)

    # concatenate the original dataframe with the new `categories` dataframe
    df = pd.concat([df, categories], axis=1)

    # drop complete data duplicates
    df = df[~df.duplicated(keep="first")]

    # drop message duplicates
    df = df[~df.message.duplicated(keep="last")]

    # drop corrupted messages
    df = df[~(df.message == "#NAME?")]

    return df


def save_data(df, database_filename):
    """
    INPUT:
        df - Dataframe of combined messages and categories data
        database_filename - Name of SQLite file to save dataframe to
        
    OUTPUT:
        None
    """

    engine = create_engine("sqlite:///{0}".format(database_filename))
    df.to_sql("Message", engine, index=False)


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print(
            "Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}".format(
                messages_filepath, categories_filepath
            )
        )
        df = load_data(messages_filepath, categories_filepath)

        print("Cleaning data...")
        df = clean_data(df)

        print("Saving data...\n    DATABASE: {}".format(database_filepath))
        save_data(df, database_filepath)

        print("Cleaned data saved to database!")

    else:
        print(
            "Please provide the filepaths of the messages and categories "
            "datasets as the first and second argument respectively, as "
            "well as the filepath of the database to save the cleaned data "
            "to as the third argument. \n\nExample: python process_data.py "
            "disaster_messages.csv disaster_categories.csv "
            "DisasterResponse.db"
        )


if __name__ == "__main__":
    main()
