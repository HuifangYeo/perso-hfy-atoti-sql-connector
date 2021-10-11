import random
import pandas as pd
from datetime import date, datetime, timedelta

def predict_prod_sales(hist_data, duration):
    predicted_sales = pd.DataFrame()
    sales_total = hist_data.groupby(["HOSPITAL_ID", "EQUIPMENT_ID", "DEPARTMENT", "Unit Cost"])["QTY.SUM"].sum().reset_index()
    hospitals = hist_data['HOSPITAL_ID'].unique()
    
    for hosp in hospitals:
        for day in range (1, duration+1):
            
            sales_fluctuation = random.uniform(-0.05, 0.15)
        #     print("sales_fluctuation", sales_fluctuation)
            sales = sales_total.loc[sales_total["HOSPITAL_ID"]==hosp].copy()
            sales["QTY.SUM"] = sales["QTY.SUM"] * sales_fluctuation
            sales["QTY.SUM"] = sales["QTY.SUM"].round() 
        #     print(sales)
            sales = sales[sales["QTY.SUM"] > 0]
            
            curr_date = (datetime.now() + timedelta(day)).strftime("%Y%m%d") 
            sales["SALE_ID"] = 'Forecast_' + sales['HOSPITAL_ID'].astype(str) + "_" + curr_date
#             sales["SALE_DATE"] =  pd.to_datetime((datetime.now() + timedelta(day)).strftime("%Y-%m-%d %H:%M:%S"))
            sales["SALE_DATE"] =  pd.to_datetime((datetime.now() + timedelta(day)).strftime("%Y-%m-%d"))
            
            predicted_sales = predicted_sales.append(sales)
        
    predicted_sales.rename(columns={"QTY.SUM":"QTY", "Unit Cost": "UNIT_COST"}, inplace=True)
    predicted_sales["LAST_UPDATE_DATE"] = pd.to_datetime(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#     predicted_sales["SALE_DATE"] = predicted_sales["SALE_DATE"].apply(lambda ts: ts.replace(hour=0, minute=0, second=1))

    return predicted_sales