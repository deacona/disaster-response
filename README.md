# Disaster Response Pipeline Project
 (Udacity DSND Project: Disaster Response Pipeline)

## Table of Contents

1. [Instructions](#instructions)
2. [Motivation](#motivation)
3. [Project Organisation](#project)
5. [Licensing, Authors, and Acknowledgements](#licensing)


## Instructions <a name="instructions"></a>

This project requires Python 3.x and all the libraries found in the [requirements.txt](requirements.txt) file.

1. Run the following commands in the project's root directory to set up your database and model.

    - To run ETL pipeline that cleans data and stores in database
        `python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db`
    - To run ML pipeline that trains classifier and saves
        `python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl`

2. Run the following command in the app's directory to run your web app.
    `python run.py`

3. Go to http://0.0.0.0:3001/


## Motivation <a name="motivation"></a>

This project is intended to analyze disaster data from Figure Eight to build a model for an API that classifies disaster messages.

Message are categorised into none, one or more of the following 36 categories: 

| | | | | | |
| --- | --- | --- | --- | --- | --- |
|related|request|offer|aid_related|medical_help|medical_products|
|search_and_rescue|security|military|child_alone|water|food|
|shelter|clothing|money|missing_people|refugees|death|
|other_aid|infrastructure_related|transport|buildings|electricity|tools|
|hospitals|shops|aid_centers|other_infrastructure|weather_related|floods|
|storm|fire|earthquake|cold|other_weather|direct_report|


## Project Organisation <a name="project"></a>

    ├── LICENSE                         <- Standard license file
    ├── README.md                       <- The top-level README for developers using this project.
    ├── requirements.txt                <- The requirements file for reproducing the analysis environment,
    │                                       generated with `pip freeze > requirements.txt`
    │
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
    └── models                          
        ├── classifier.pkl              <- Saved model (not included in repo)
        └── train_classifier.py         <- Builds, trains, evaluates and outputs model


## Licensing, Authors, Acknowledgements <a name="licensing"></a>

Acknowledgement to Figure Eight for sharing the dataset. Thanks also to my course mentor [NicoEssi](https://github.com/NicoEssi) for his advice and support. The code is available to use as you would like.
