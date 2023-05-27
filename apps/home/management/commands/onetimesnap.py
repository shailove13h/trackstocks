# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Shailesh Vasava
"""

from .startMulti import *
import multiprocessing
import time
# from startMulti import *
# from nseMultiple import *
import numpy as np
import xlwings as xw
from xlwings.main import Sheet
from xlwings.utils import exception
from pandas.core.indexes.datetimes import date_range
from datetime import date, datetime
from openpyxl import Workbook
from django.http import HttpResponse
import os
# from apps.home.models import High_OI_both_Side
from django.core.management.base import BaseCommand
from django.conf import settings
from sqlalchemy import create_engine

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir))
XMLFILES_FOLDER = os.path.join(PROJECT_ROOT, 'xml_files/')
# start = time.time()
global df_list
expiry = "12-Jan-2023"
lowerStrike = 800
# excel_file = os.path.join(PROJECT_ROOT, 'option_chain_analysis_paral.xlsx')
df_list = []
# oi_filename = os.path.join("Files","Nifty_50_oi_data_records_{0}.json".format(datetime.now().strftime("%d%m%y")))

# wb = xw.Book(excel_file)

# sheet_oi_single = wb.sheets("OIData")
# hi_oi_sheet= wb.sheets("High_OI_both_Side")
# same_Strike_but_CE_OI_High_side = wb.sheets("CE_OI_High_Same_Stike_hi")
# same_Strike_but_PE_OI_High_side = wb.sheets("PE_OI_High_Same_Stike_hi")
# update_strike_oi = wb.sheets("OI_strike")
# update_movingaverage = wb.sheets("movingaverage")
# update_ce_oi =wb.sheets("CE_Data")
# update_pe_oi =wb.sheets("PE_Data") 
# update_ce_volume =wb.sheets("CE_Volume") 
# update_ce_imp_valatlty =wb.sheets("CE_Implied_volatality") 
# update_ce_last_price =wb.sheets("CE_Last_Price") 
# update_pe_volume =wb.sheets("PE_Volume") 
# update_pe_imp_valatlty =wb.sheets("PE_Implied_volatality") 
# update_pe_last_price =wb.sheets("PE_Last_Price") 



# execute tasks sequentially in a for loop
from time import sleep



start = time.time()

# fisrt we need to increase ulimit as below
# try:
#     import resource as res
# except ImportError: #Windows
#     res = None

# def raise_nofile(nofile_atleast=4096):
#     """
#     sets nofile soft limit to at least 4096, useful for running matlplotlib/seaborn on
#     parallel executing plot generators vs. Ubuntu default ulimit -n 1024 or OS X El Captian 256
#     temporary setting extinguishing with Python session.
#     """
#     if res is None:
#         return (None,)*2
# # %% (0) what is current ulimit -n setting?
#     soft,ohard = res.getrlimit(res.RLIMIT_NOFILE)
#     hard = ohard
# # %% (1) increase limit (soft and even hard) if needed
#     if soft<nofile_atleast:
#         soft = nofile_atleast

#         if hard<soft:
#             hard = soft

#         print('setting soft & hard ulimit -n {} {}'.format(soft,hard))
#         try:
#             res.setrlimit(res.RLIMIT_NOFILE,(soft,hard))
#         except (ValueError,res.error):
#             try:
#                hard = soft
#                print('trouble with max limit, retrying with soft,hard {},{}'.format(soft,hard))
#                res.setrlimit(res.RLIMIT_NOFILE,(soft,hard))
#             except Exception:
#                print('failed to set ulimit, giving up')
#                soft,hard = res.getrlimit(res.RLIMIT_NOFILE)

#     return soft,hard
# # limit seting done go to main function




print(datetime.now().strftime("%H:%M"))
def extractCEnPE(response,indx):
    # global hi_oi_CE_chain
    # global hi_oi_PE_chain
    # global ce_data
    # global pe_data
 

    ce_values = [data["CE"] for data in response['filtered']['data'] if "CE" in data ]
    pe_values = [data["PE"] for data in response['filtered']['data'] if "PE" in data ]

    ce_data = pd.DataFrame(ce_values)
    pe_data = pd.DataFrame(pe_values)
    ce_data_S = ce_data.sort_values('strikePrice')
    pe_data_S = pe_data.sort_values('strikePrice')
        
    # write data to sheet single
    # sheet_oi_single.range("A2").options(index=False, header=False).value = ce_data_S.drop([
    # 'underlying', 'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange','strikePrice']]
    # sheet_oi_single.range("J2").options(index=False, header=False).value = pe_data_S.drop([
    #     'underlying', 'identifier','totalBuyQuantity', 'totalSellQuantity','strikePrice','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange',]]

    # ce_data = ce_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
    
    pe_data = pe_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
    
 
   
    ce_data['type'] = "CE"
    pe_data['type'] = "PE"

      
    
    return ce_data,pe_data

# def extractCEnPE(response):
    # global hi_oi_CE_chain
    # global hi_oi_PE_chain
    # global ce_data
    # global pe_data
 

    # ce_values = [data["CE"] for data in response['filtered']['data'] if "CE" in data ]
    # pe_values = [data["PE"] for data in response['filtered']['data'] if "PE" in data ]

    # ce_data = pd.DataFrame(ce_values)
    # pe_data = pd.DataFrame(pe_values)
    # ce_data_S = ce_data.sort_values('strikePrice')
    # pe_data_S = pe_data.sort_values('strikePrice')
        
    # # write data to sheet single
    # # sheet_oi_single.range("A2").options(index=False, header=False).value = ce_data_S.drop([
    # # 'underlying', 'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange','strikePrice']]
    # # sheet_oi_single.range("J2").options(index=False, header=False).value = pe_data_S.drop([
    # #     'underlying', 'identifier','totalBuyQuantity', 'totalSellQuantity','strikePrice','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange',]]

    # ce_data = ce_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
    
    # pe_data = pe_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
    
 
   
    # ce_data['type'] = "CE"
    # pe_data['type'] = "PE"

      
    
    # return ce_data,pe_data


def fetch_by_stock(df):


    #all oi high 
    ce_chain_all_high = pd.DataFrame()
    pe_chain_all_high = pd.DataFrame()
    # CE oi high but same strike pe
    ce_chain_Same_Strike_high_OI_CE = pd.DataFrame()
    pe_chain__Same_Strike_high_OI_CE = pd.DataFrame()
    # PE oi high but same CE strike
    ce_chain_Same_Strike_high_OI_PE = pd.DataFrame()
    pe_chain__Same_Strike_high_OI_PE = pd.DataFrame()
        # return df_list
   
    stk = df
    stkname = stk + ".json"
    
    stoOPchain = nse_optionchain_scrapper(stk)
    # print(stoOPchain)
    oi_chain = os.path.join(PROJECT_ROOT,"openInterestData/open_interest_{0}.json".format(stk))
    
    with open(oi_chain, "w") as outpufile :
        outpufile.write(json.dumps(stoOPchain, indent=4, sort_keys= True ))
    if len(stoOPchain)>0:

        # ce_data,pe_data = extractCEnPE(stoOPchain)

        ce_values = [data["CE"] for data in stoOPchain['filtered']['data'] if "CE" in data ]
        pe_values = [data["PE"] for data in stoOPchain['filtered']['data'] if "PE" in data ]

        ce_data = pd.DataFrame(ce_values)
        pe_data = pd.DataFrame(pe_values)
        # ce_data_S = ce_data.sort_values('strikePrice')
        # pe_data_S = pe_data.sort_values('strikePrice')
            
        # write data to sheet single
        # sheet_oi_single.range("A2").options(index=False, header=False).value = ce_data_S.drop([
        # 'underlying', 'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange','strikePrice']]
        # sheet_oi_single.range("J2").options(index=False, header=False).value = pe_data_S.drop([
        #     'underlying', 'identifier','totalBuyQuantity', 'totalSellQuantity','strikePrice','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange',]]

        ce_data = ce_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
        
        pe_data = pe_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
        
    
    
        ce_data['type'] = "CE"
        pe_data['type'] = "PE"





        pcrvalue=pcr(stoOPchain,0)

        print("PCR for " + stkname + "is : " + str(pcrvalue))


         # print("OI data writen to sheets")

        return ce_data,pe_data,pcrvalue
    else : 
        return "OI Chain has no data"



def run(stk,return_dict):
    print("run fucntion called")
    ce_chain_all_high_C = pd.DataFrame()
    pe_chain_all_high_C = pd.DataFrame()
    # CE oi high but same strike pe
    ce_chain_Same_Strike_high_OI_CE_C = pd.DataFrame()
    pe_chain__Same_Strike_high_OI_CE_C = pd.DataFrame()
    # PE oi high but same CE strike
    ce_chain_Same_Strike_high_OI_PE_C = pd.DataFrame()
    pe_chain__Same_Strike_high_OI_PE_C = pd.DataFrame()
    # print(self.id)
    ce_data,pe_data,pcrvalue =fetch_by_stock(stk)



    if stk == "BANKNIFTY" :
        rng = 10
    elif stk == "NIFTY" :
        rng = 10
    else :
        rng = 5

    for n in range(0,rng):

        # below is comparision of high open interest
        hi_oi_CE_chain  = pd.DataFrame(ce_data).loc[ pd.DataFrame(ce_data)['index'] == n ]
        
        hi_oi_PE_chain  = pd.DataFrame(pe_data).loc[ pd.DataFrame(pe_data)['index'] == n ]

        ce_chain_all_high_C = pd.concat([ce_chain_all_high_C, hi_oi_CE_chain])
        ce_chain_all_high_C['pcr'] = pcrvalue
        pe_chain_all_high_C = pd.concat([pe_chain_all_high_C, hi_oi_PE_chain])
        pe_chain_all_high_C['pcr'] = pcrvalue

        # below if comparison of ce high open interest but with same strike pe oi
        ce_high_oi_same_strike = hi_oi_CE_chain['strikePrice'][n]
        # print(ce_high_oi_same_strike)
        hi_ce_oi_ce_chain_Same_Strike  = pd.DataFrame(ce_data).loc[ pd.DataFrame(ce_data)['index'] == n ]
        
        # try to find data as oer strike if not found dont take it 
        
        if ce_high_oi_same_strike in pe_data['strikePrice'].values:
    
            
            hi_ce_oi_PE_chain_Same_Strike  = pd.DataFrame(pe_data).loc[ pd.DataFrame(pe_data)['strikePrice'] == ce_high_oi_same_strike ]
            ce_chain_Same_Strike_high_OI_CE_C = pd.concat([ce_chain_Same_Strike_high_OI_CE_C, hi_ce_oi_ce_chain_Same_Strike])
            pe_chain__Same_Strike_high_OI_CE_C = pd.concat([pe_chain__Same_Strike_high_OI_CE_C, hi_ce_oi_PE_chain_Same_Strike])
            ce_chain_Same_Strike_high_OI_CE_C['pcr'] = pcrvalue
            pe_chain__Same_Strike_high_OI_CE_C['pcr'] = pcrvalue
       
        # below if comparison of PE high open interest but with same strike CE oi

        # try to find data as oer strike if not found dont take it 
        pe_high_oi_same_strike = hi_oi_PE_chain['strikePrice'][n]
        # print(pe_high_oi_same_strike)
        if pe_high_oi_same_strike in ce_data['strikePrice'].values:

            hi_pe_oi_ce_chain_Same_Strike  = pd.DataFrame(ce_data).loc[ pd.DataFrame(ce_data)['strikePrice'] == pe_high_oi_same_strike ]
            
            hi_pe_oi_PE_chain_Same_Strike  = pd.DataFrame(pe_data).loc[ pd.DataFrame(pe_data)['index'] == n ]
                    
            ce_chain_Same_Strike_high_OI_PE_C = pd.concat([ce_chain_Same_Strike_high_OI_PE_C, hi_pe_oi_ce_chain_Same_Strike])
            pe_chain__Same_Strike_high_OI_PE_C = pd.concat([pe_chain__Same_Strike_high_OI_PE_C, hi_pe_oi_PE_chain_Same_Strike])
            ce_chain_Same_Strike_high_OI_PE_C['pcr'] = pcrvalue
            pe_chain__Same_Strike_high_OI_PE_C['pcr'] = pcrvalue
        
        # print("printing pe high oi")
        # print(pe_high_oi_same_strike)
    
    return_dict[stk] = {"ce_chain_all_high_C" : ce_chain_all_high_C,
                        "pe_chain_all_high_C":pe_chain_all_high_C,
                        "ce_chain_Same_Strike_high_OI_CE_C":ce_chain_Same_Strike_high_OI_CE_C,
                        "pe_chain__Same_Strike_high_OI_CE_C" :pe_chain__Same_Strike_high_OI_CE_C,
                        
                        "ce_chain_Same_Strike_high_OI_PE_C":ce_chain_Same_Strike_high_OI_PE_C,
                        "pe_chain__Same_Strike_high_OI_PE_C":pe_chain__Same_Strike_high_OI_PE_C  }
    
   

   

   
   