#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import server_information as si
import functions as f
import pandas as pd



# NCR = Fejlrapporter | SupplierEvaluation = Leverandørevaluering
# SupplierComplaint = Leverandørreklmationer | CustomerComplaint = Kundereklamationer
data_to_export = ["NCR","CustomerComplaint","SupplierComplaint","SupplierEvaluation"]

for requested_data in data_to_export:
    wb_name = f"Sherlock data {requested_data}.xlsx"
    path_file_wb = si.filepath + r"\\" + wb_name
    excel_writer = pd.ExcelWriter(path_file_wb, engine="xlsxwriter")    
    try:
        # Get data and insert into workbook
        f.insert_dataframe_into_excel(
            excel_writer
            ,f.get_sherlock_data(requested_data)
            ,requested_data)
        # Save and close workbook
        excel_writer.save()
        excel_writer.close()
        # Write into log
        f.log_insert("Sherlock data - flow_management.py"
                     ,f"Script for list: {requested_data} completed.")        
    except Exception as e:
        f.log_insert("Sherlock data - flow_management.py"
                     ,f"Script has failed for list: {requested_data} with error message: {e}")
        # Save and close workbook
        excel_writer.save()
        excel_writer.close()        

