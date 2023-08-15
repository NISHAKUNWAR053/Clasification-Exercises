from env import get_connection
import pandas as pd
import os
import seaborn as sns
import numpy as np
from pydataset import data


# Titanic
def get_titanic_data():
    filename = 'titanic.csv'
    if os.path.isfile(filename):  
        return pd.read_csv(filename)  
    else:
        db_url = get_connection('titanic_db')
        query = '''
                SELECT * FROM passengers
                '''
        titanic = pd.read_sql(query, db_url)
        titanic.to_csv('titanic.csv', index=False)
        return titanic


def new_iris_data():
    """
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the iris_db
    """
    url = get_connection('iris_db')
    query = "select * from species join measurements using(species_id)"
    return pd.read_sql(query, url)


def get_iris_data(filename = "iris.csv"):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output titanic df
    """
    if os.path.exists(filename):
        df = pd.read_csv(filename, index_col=0) 
        print('Found CSV')
        return df
    
    else:
        df = new_iris_data()
        
        #want to save to csv
        df.to_csv(filename)
        print('Creating CSV')
        return df

def new_telco_data():
    """
    This function will:
    - take in a SQL_query
    - create a connect_url to mySQL
    - return a df of the given query from the telco_churn db
    """
    url = get_connection('telco_churn')
    SQL_query = '''
                select *
                from customers
                join contract_types using(contract_type_id)
                join internet_service_types using(internet_service_type_id)
                join payment_types using(payment_type_id)
                '''
    return pd.read_sql(SQL_query, url)


def get_telco_data(filename="telco.csv"):
    """
    This function will:
    - Check local directory for csv file
        - return if exists
    - If csv doesn't exists:
        - create a df of the SQL_query
        - write df to csv
    - Output titanic df
    """
    if os.path.exists(filename):
        df = pd.read_csv(filename, index_col=0) 
        print('Found CSV')
        return df
    
    else:
        df = new_telco_data()
        
        #want to save to csv
        df.to_csv(filename)
        print('Creating CSV')
        return df