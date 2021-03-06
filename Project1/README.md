# Project: Data Modeling with Postgres

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.


They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.


## ETL Pipeline

- Run create_table.py script in terminal.
    - Create and Initialize sparikifydb database.
    - create_table.py will call all create table query in sql_queries.py
- Run test.ipynb 
    - Test if the tables were created successfully.
- Run etl.ipynb to develope ETL process for each table
    - Use tips and guide here to prepare for etl.py file, which will process all datasets.
- Run etl.py from terminal.
    - Connect to sparkifydb databse 
    - Extracts and process log_data and song_data
    - Loads data into five tables by queries in sql_queries.py
- Run test.ipynb to confirm it was successful inserted into databse tables.


