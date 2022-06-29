#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import server_information as si
import requests
import pandas as pd


# Write into dbo.log
def log_insert(event: str, note: str):
    """Inserts a record into BKI_Datastore dbo.log with event and note."""
    dict_log = {"Note": note
                ,"Event": event}
    pd.DataFrame(data=dict_log, index=[0]).to_sql("Log", con=si.engine_ds, schema="dbo", if_exists="append", index=False)

# Write dataframe into Excel sheet
def insert_dataframe_into_excel (engine, dataframe, sheetname: str, include_index: bool = False):
    """
    Inserts a dataframe into an Excel sheet
    \n Parameters
    ----------
    engine : Excel engine
    dataframe : Pandas dataframe
        Dataframe containing data supposed to be inserted into the Excel workbook.
    sheetname : str (max length 31 characters)
        Name of sheet created where dataframe will be inserted into.
    include_index : bool
        True if index is supposed to be included in insert into Excel, False if not.
    """
    dataframe.to_excel(engine, sheet_name=sheetname, index=include_index)

# Get data from Sherlock Postman API
def get_sherlock_data(list_name:str, rename_headers:bool=True) -> pd.DataFrame():
    """
    Returns a pandas Dataframe with data from Sherlock from the requested list.
    \n Parameters
    ----------
    list_name : str
        The name of the list with data which is to be exported.
    rename_headers: boolean. Default value is True
        Define whether or not to translate headers of the returned dataframe from english to danish.
    """
    
    # Define base url for api
    base_url = "https://qa.bki.dk/api/stats/"   #CustomerComplaint #/NCR
    # Add requested list to url to create the required format for data fetching
    request_url = base_url + list_name
    
    # Get the data
    payload={}
    headers = {
      'Authorization': 'Basic bm1vOkxhZ2thZ2VwbGFnZTEyMw==',
      'Cookie': 'LtpaToken=AAECAzYyNzhDMTdBNjI3OTMxRkFDTj1OaWNob2xhaiBNhm5zc29uIE9sc2VuL09VPUJydWdlcmUvT1U9SG9qYmplcmcvREM9YmtpL0RDPWRrJWJFFxF7CQtHYevRAfStIiKZQHc=; SessionID=6757E9F11F001C6E9AB9C32545944DAAF94F5146'
    }
    response = requests.request("GET", request_url, headers=headers, data=payload).json()[0]

    # Add data into a dataframe    
    df = pd.DataFrame(response['data'])
    # Translate headers from english to danish if requested
    if rename_headers:
        df.rename(columns = response['fields'], inplace = True)
  
    return df

