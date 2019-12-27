# Disaster Response Pipeline Project
 (Udacity DSND Project: Disaster Response Pipeline)

 This project is intended to analyze disaster data from Figure Eight to build a model for an API that classifies disaster messages.


## Table of Contents

1. [Instructions](#instructions)
2. [Results](#results)
3. [Project Organisation](#project)
5. [Licensing, Authors, and Acknowledgements](#licensing)


## Instructions <a name="instructions"></a>

This project requires Python 3.x and the libraries found in the [requirements.txt](requirements.txt) file.

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


## Results <a name="results"></a>

### Data processing

* Combine message and category data sources
* Split categories into separate category columns with binary values (Note some of the training data had 2s which I modifed to 1s)
* Remove duplicated messages
* Remove meaningless messages (There is a #NAME? in the training data which looks like a spreadsheet error)
* Save processed data

### Classifier training

* Load processed data
* Clean, normalize, tokenize and lemmatize words
* Vectorize word counts
* Transform to a TF-IDF representation
* Use a Random Forest classifier within a multi-output strategy
* Perform Grid Search cross-validation to tune the hyperparameters
* Fit, evaluate and then save the model


### Web app

Inputted messages are categorised into none, one or more of the following 36 categories: 

| | | | | | |
| --- | --- | --- | --- | --- | --- |
|related|request|offer|aid_related|medical_help|medical_products|
|search_and_rescue|security|military|child_alone|water|food|
|shelter|clothing|money|missing_people|refugees|death|
|other_aid|infrastructure_related|transport|buildings|electricity|tools|
|hospitals|shops|aid_centers|other_infrastructure|weather_related|floods|
|storm|fire|earthquake|cold|other_weather|direct_report|

![Distribution of Message Categories](plot_categories.png)

Some of the categories were much more prevalent in the training data so we are likely to have more reliable results for these than some of the less frequently occuring ones. None of the training data was flagged with "child_alone" so we cannot currently use the model to predict this category.

![Distribution of Message Genres](plot_genres.png)


## Project Organisation <a name="project"></a>

    ├── app                             
    │   ├── templates                    
    │   |   ├── go.html                 <- Classification result page of web app
    │   |   └── master.html             <- Main page of web app
    │   └── run.py                      <- Flask file that runs app
    │
    ├── data                            
    │   ├── disaster_categories.csv     <- Data to process
    │   ├── disaster_messages.csv       <- Data to process
    │   ├── DisasterResponse.db         <- SQLite database to save clean data to (not included in repo)
    │   └── process_data.py             <- Loads, cleans and stores the data
    │
    ├── models                          
    │   ├── classifier.pkl              <- Saved model (not included in repo)
    │   └── train_classifier.py         <- Builds, trains, evaluates and outputs model
    │
    ├── LICENSE                         <- Standard license file
    ├── plot_categories.png             <- Category distribution plot (downloaded from app)
    ├── plot_genres.png                 <- Genre distribution plot (downloaded from app)
    ├── README.md                       <- The top-level README for developers using this project.
    └── requirements.txt                <- The requirements file for reproducing the analysis environment,
                                            generated with `pip freeze > requirements.txt`


## Licensing, Authors, Acknowledgements <a name="licensing"></a>

Acknowledgement to Figure Eight for sharing the dataset. Thanks also to my course mentor [NicoEssi](https://github.com/NicoEssi) for his advice and support. The code is available to use as you would like.
