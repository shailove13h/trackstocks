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
from apps.home.models import High_OI_both_Side
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
excel_file = os.path.join(PROJECT_ROOT, 'home/option_chain_analysis_paral.xlsx')
df_list = []
# oi_filename = os.path.join("Files","Nifty_50_oi_data_records_{0}.json".format(datetime.now().strftime("%d%m%y")))

wb = xw.Book(excel_file)

sheet_oi_single = wb.sheets("OIData")
hi_oi_sheet= wb.sheets("High_OI_both_Side")
same_Strike_but_CE_OI_High_side = wb.sheets("CE_OI_High_Same_Stike_hi")
same_Strike_but_PE_OI_High_side = wb.sheets("PE_OI_High_Same_Stike_hi")
update_strike_oi = wb.sheets("OI_strike")
update_movingaverage = wb.sheets("movingaverage")
update_ce_oi =wb.sheets("CE_Data")
update_pe_oi =wb.sheets("PE_Data") 
update_ce_volume =wb.sheets("CE_Volume") 
update_ce_imp_valatlty =wb.sheets("CE_Implied_volatality") 
update_ce_last_price =wb.sheets("CE_Last_Price") 
update_pe_volume =wb.sheets("PE_Volume") 
update_pe_imp_valatlty =wb.sheets("PE_Implied_volatality") 
update_pe_last_price =wb.sheets("PE_Last_Price") 



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
    sheet_oi_single.range("A2").options(index=False, header=False).value = ce_data_S.drop([
    'underlying', 'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange','strikePrice']]
    sheet_oi_single.range("J2").options(index=False, header=False).value = pe_data_S.drop([
        'underlying', 'identifier','totalBuyQuantity', 'totalSellQuantity','strikePrice','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange',]]

    ce_data = ce_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
    
    pe_data = pe_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
    
 
   
    ce_data['type'] = "CE"
    pe_data['type'] = "PE"

      
    
    return ce_data,pe_data

def extractCEnPE(response,indx):
    global hi_oi_CE_chain
    global hi_oi_PE_chain
    global ce_data
    global pe_data
 

    ce_values = [data["CE"] for data in response['filtered']['data'] if "CE" in data ]
    pe_values = [data["PE"] for data in response['filtered']['data'] if "PE" in data ]

    ce_data = pd.DataFrame(ce_values)
    pe_data = pd.DataFrame(pe_values)
    ce_data_S = ce_data.sort_values('strikePrice')
    pe_data_S = pe_data.sort_values('strikePrice')
        
    # write data to sheet single
    sheet_oi_single.range("A2").options(index=False, header=False).value = ce_data_S.drop([
    'underlying', 'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange','strikePrice']]
    sheet_oi_single.range("J2").options(index=False, header=False).value = pe_data_S.drop([
        'underlying', 'identifier','totalBuyQuantity', 'totalSellQuantity','strikePrice','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice', 'underlyingValue'], axis=1)[['openInterest','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','lastPrice','change','pChange',]]

    ce_data = ce_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
    
    pe_data = pe_data.sort_values('openInterest', ascending=False,ignore_index=True).reset_index()
    
 
   
    ce_data['type'] = "CE"
    pe_data['type'] = "PE"

      
    
    return ce_data,pe_data


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
    oi_chain = os.path.join(PROJECT_ROOT,"home/openInterestData/open_interest_{0}.json".format(stk))
    
    with open(oi_chain, "w") as outpufile :
        outpufile.write(json.dumps(stoOPchain, indent=4, sort_keys= True ))
    if len(stoOPchain)>0:

        ce_data,pe_data = extractCEnPE(stoOPchain,1)

         # print("OI data writen to sheets")

        return ce_data,pe_data
    else : 
        return "OI Chain has no data"



def run(stk,return_dict):
    ce_chain_all_high_C = pd.DataFrame()
    pe_chain_all_high_C = pd.DataFrame()
    # CE oi high but same strike pe
    ce_chain_Same_Strike_high_OI_CE_C = pd.DataFrame()
    pe_chain__Same_Strike_high_OI_CE_C = pd.DataFrame()
    # PE oi high but same CE strike
    ce_chain_Same_Strike_high_OI_PE_C = pd.DataFrame()
    pe_chain__Same_Strike_high_OI_PE_C = pd.DataFrame()
    # print(self.id)
    ce_data, pe_data =fetch_by_stock(stk)

    for n in range(0,3):

        # below is comparision of high open interest
        hi_oi_CE_chain  = pd.DataFrame(ce_data).loc[ pd.DataFrame(ce_data)['index'] == n ]
        
        hi_oi_PE_chain  = pd.DataFrame(pe_data).loc[ pd.DataFrame(pe_data)['index'] == n ]

        ce_chain_all_high_C = pd.concat([ce_chain_all_high_C, hi_oi_CE_chain])
        pe_chain_all_high_C = pd.concat([pe_chain_all_high_C, hi_oi_PE_chain])
        # below if comparison of ce high open interest but with same strike pe oi
        ce_high_oi_same_strike = hi_oi_CE_chain['strikePrice'][n]
        # print(ce_high_oi_same_strike)
        hi_ce_oi_ce_chain_Same_Strike  = pd.DataFrame(ce_data).loc[ pd.DataFrame(ce_data)['index'] == n ]
        
        hi_ce_oi_PE_chain_Same_Strike  = pd.DataFrame(pe_data).loc[ pd.DataFrame(pe_data)['strikePrice'] == ce_high_oi_same_strike ]
        ce_chain_Same_Strike_high_OI_CE_C = pd.concat([ce_chain_Same_Strike_high_OI_CE_C, hi_ce_oi_ce_chain_Same_Strike])
        pe_chain__Same_Strike_high_OI_CE_C = pd.concat([pe_chain__Same_Strike_high_OI_CE_C, hi_ce_oi_PE_chain_Same_Strike])
        # below if comparison of PE high open interest but with same strike CE oi
        pe_high_oi_same_strike = hi_oi_PE_chain['strikePrice'][n]
        # print(pe_high_oi_same_strike)
        hi_pe_oi_ce_chain_Same_Strike  = pd.DataFrame(ce_data).loc[ pd.DataFrame(ce_data)['strikePrice'] == pe_high_oi_same_strike ]
        
        hi_pe_oi_PE_chain_Same_Strike  = pd.DataFrame(pe_data).loc[ pd.DataFrame(pe_data)['index'] == n ]
                
        ce_chain_Same_Strike_high_OI_PE_C = pd.concat([ce_chain_Same_Strike_high_OI_PE_C, hi_pe_oi_ce_chain_Same_Strike])
        pe_chain__Same_Strike_high_OI_PE_C = pd.concat([pe_chain__Same_Strike_high_OI_PE_C, hi_pe_oi_PE_chain_Same_Strike])
    
    
    
    return_dict[stk] = {"ce_chain_all_high_C" : ce_chain_all_high_C,"pe_chain_all_high_C":pe_chain_all_high_C,"ce_chain_Same_Strike_high_OI_CE_C":ce_chain_Same_Strike_high_OI_CE_C,"pe_chain__Same_Strike_high_OI_CE_C" :pe_chain__Same_Strike_high_OI_CE_C,"pe_chain__Same_Strike_high_OI_CE_C":pe_chain__Same_Strike_high_OI_CE_C,"ce_chain_Same_Strike_high_OI_PE_C":ce_chain_Same_Strike_high_OI_PE_C, "pe_chain__Same_Strike_high_OI_PE_C":pe_chain__Same_Strike_high_OI_PE_C  }
    
    return 0

    # print("I'm the process with id: {}".format(self.id))
def combineStockOI(fnolists,return_dict,lststk):
    ce_chain_all_high = pd.DataFrame()
    pe_chain_all_high = pd.DataFrame()
    # CE oi high but same strike pe
    ce_chain_Same_Strike_high_OI_CE = pd.DataFrame()
    pe_chain__Same_Strike_high_OI_CE = pd.DataFrame()
    # PE oi high but same CE strike
    ce_chain_Same_Strike_high_OI_PE = pd.DataFrame()
    pe_chain__Same_Strike_high_OI_PE = pd.DataFrame()
    # print(self.id)
    # ce_data, pe_data =fetch_by_stock(stk)
    # lststk = len(fnolists)
    for  key in return_dict:
    
        stk = key
        stkname = stk + ".json"
        print( "This is stock : " + str(stk))
        try:
            
            # lststk = len(fnolists)
            
            ce_chain_all_high_C = return_dict[stk]["ce_chain_all_high_C"]             
            pe_chain_all_high_C = return_dict[stk]["pe_chain_all_high_C"]
            # print("Printing CE Chain List")
            # print(ce_chain_all_high_C)

            ce_chain_Same_Strike_high_OI_CE_C = return_dict[stk]["ce_chain_Same_Strike_high_OI_CE_C"]
            pe_chain__Same_Strike_high_OI_CE_C = return_dict[stk]["pe_chain__Same_Strike_high_OI_CE_C"]
            
            ce_chain_Same_Strike_high_OI_PE_C = return_dict[stk]["ce_chain_Same_Strike_high_OI_PE_C"]
            pe_chain__Same_Strike_high_OI_PE_C = return_dict[stk]["pe_chain__Same_Strike_high_OI_PE_C"]

            
            # Concate or combibe all stock in diction of levled oi

            ce_chain_all_high = pd.concat([ce_chain_all_high, ce_chain_all_high_C])
            pe_chain_all_high = pd.concat([pe_chain_all_high, pe_chain_all_high_C])

              # Concate or combibe CE oi High  stock in diction of levled oi
            ce_chain_Same_Strike_high_OI_CE = pd.concat([ce_chain_Same_Strike_high_OI_CE, ce_chain_Same_Strike_high_OI_CE_C])
            pe_chain__Same_Strike_high_OI_CE = pd.concat([pe_chain__Same_Strike_high_OI_CE, pe_chain__Same_Strike_high_OI_CE_C])
       

            ce_chain_Same_Strike_high_OI_PE = pd.concat([ce_chain_Same_Strike_high_OI_PE, ce_chain_Same_Strike_high_OI_PE_C])
            pe_chain__Same_Strike_high_OI_PE = pd.concat([pe_chain__Same_Strike_high_OI_PE, pe_chain__Same_Strike_high_OI_PE_C])

            # print(ce_chain_all_high)

        except Exception as err:
            print("opps error")
            print("This is error" + str(err)) 
                
    print("OI data writen to sheets")
    ce_chain_all_high_r = ce_chain_all_high.drop([
        'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty','bidprice', 'askQty', 'askPrice'], axis=1)[['changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','lastPrice','openInterest','strikePrice','underlyingValue','underlying']]
    df = pd.DataFrame(ce_chain_all_high_r)

    # Save the DataFrame to an Excel file
    df.to_excel("data.xlsx", index=False)
    
    # write data to datbase table High_OI_both_Side
    df = pd.DataFrame(df)

    # Write the DataFrame to the database

    user = settings.Databse['deafualt'] ['USER']
    password = settings.Databse['deafualt'] ['PASSWORD']
    database_name  = settings.Databse['deafualt'] ['NAME']
    database_url = 'postgresql://{user}:{password}@localhost:5432/{databse_name}'.format(
        user = user,
        password = password,
        database_name = database_name ,

    )
    engine = create_engine(database_url, echo = False)

    df.to_sql(High_OI_both_Side._meta.db_table, if_exists="append",con=engine, index=False)
    print(ce_chain_all_high)
    return HttpResponse("DataFrame exported to database successfully!")


   
   
    

    # try:
    #      # below is comparision of high open interest
    #     hi_oi_sheet.range("A2").options(index=False, header=False).value = ce_chain_all_high.drop([
    #     'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty','bidprice', 'askQty', 'askPrice'], axis=1)[['changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','lastPrice','openInterest','strikePrice','underlyingValue','underlying']]
    #     hi_oi_sheet.range("N2").options(index=False, header=False).value = pe_chain_all_high.drop([
    #     'identifier','totalBuyQuantity', 'totalSellQuantity','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice','underlyingValue',], axis=1)[['strikePrice','openInterest','lastPrice','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange',]]

    #     # below if comparison of ce high open interest but with same strike pe oi
    #     same_Strike_but_CE_OI_High_side.range("A2").options(index=False, header=False).value = ce_chain_Same_Strike_high_OI_CE.drop([
    #         'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty','bidprice', 'askQty', 'askPrice'], axis=1)[['changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','lastPrice','openInterest','strikePrice','underlyingValue','underlying']]
    #     same_Strike_but_CE_OI_High_side.range("N2").options(index=False, header=False).value = pe_chain__Same_Strike_high_OI_CE.drop([
    #         'identifier','totalBuyQuantity', 'totalSellQuantity','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice','underlyingValue',], axis=1)[['strikePrice','openInterest','lastPrice','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange',]]
        
    #     # below if comparison of PE high open interest but with same strike CE oi
    #     same_Strike_but_PE_OI_High_side.range("A2").options(index=False, header=False).value = ce_chain_Same_Strike_high_OI_PE.drop([
    #         'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty','bidprice', 'askQty', 'askPrice'], axis=1)[['changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','lastPrice','openInterest','strikePrice','underlyingValue','underlying']]
    #     same_Strike_but_PE_OI_High_side.range("N2").options(index=False, header=False).value = pe_chain__Same_Strike_high_OI_PE.drop([
    #         'identifier','totalBuyQuantity', 'totalSellQuantity','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice','underlyingValue',], axis=1)[['strikePrice','openInterest','lastPrice','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange',]]
    #     print("writing to excel is completed")
        
    # except Exception as err:
    #     print("writing excel data  error")
    #     print(err)  
    
# if __name__ == '__main__':
    
#     # p = Process(banknifty)
#     # p.start()
#     # p.join()
#     # initiate ulimit function 
#     from argparse import ArgumentParser
#     u = ArgumentParser()
#     u.add_argument('-n','--nofile',help='max number of open files',type=int,default=4096)
#     u = u.parse_args()

#     soft,hard = raise_nofile(u.nofile)
#     print('ulimit -n soft,hard: {},{}'.format(soft,hard))
#     # limit seting done
#     manager = multiprocessing.Manager()
#     return_dict = manager.dict()
#     jobs = []
#     try:
#         # fnolist = nifty50List()
#         fnolists = fnolist()
#         print("get request called")
#         # print(fnolist)
#         if len(fnolists) == 0:
#             print("Resposnse is Empty")
              
#         lststk = len(fnolists)
#     except Exception as err:

#         print("opps error in getting fnolist")
#         print(err)   
    
#     # lststk = 150
    
    

#     part = lststk
#     if len(fnolists) > 0:
#         global m
#         global s
#         global brk
#         m = 0
#         brk = 60
#         s= 0
#         while s < part-1 :
#             print("Snap part is running")
#             if brk >part-1 :
#                 brk = part
#             # print("lets Sleep for 10 second")
#             # time.sleep(10)   
#             # print("oh lets awake do some work") 
#             for n in range(m,brk):
#                 print(" running Process no :" + str(n))
#                 s=s+1
#                 try:
#                     stk = fnolists[n]
#                     if (stk):
#                         stkname = stk + ".json"
#                         # p = Process(target=worker, args=(stk, return_dict))
#                         p = multiprocessing.Process(target=run, args=(stk, return_dict))
                        
#                         p.start()
#                         jobs.append(p)
#                     # lststk = len(fnolists)
#                 except Exception as err:
#                     print("process creation  error")
#                     print(err)
#             try:
#                 for proc in jobs:
#                     proc.join()
                
#             except Exception as err:
#                 print("joing  error")
#                 print(err)  
#             m = brk
#             brk = brk + 60
        




    




            
#     if s > lststk-1:
#         for proc in jobs:
#                     proc.join()

        

#         combineStockOI(fnolists,return_dict,lststk)

#     print('ulimit -n soft,hard: {},{}'.format(soft,hard))
#     print(f'Duration: {time.time() - start} seconds')

def onetimefuction():
    
    # # p = Process(banknifty)
    # # p.start()
    # # p.join()
    # # initiate ulimit function 
    # from argparse import ArgumentParser
    # u = ArgumentParser()
    # u.add_argument('-n','--nofile',help='max number of open files',type=int,default=4096)
    # u = u.parse_args()

    # soft,hard = raise_nofile(u.nofile)
    # print('ulimit -n soft,hard: {},{}'.format(soft,hard))
    # # limit seting done
    manager = multiprocessing.Manager()
    return_dict = manager.dict()
    jobs = []
    try:
        # fnolist = nifty50List()
        fnolists = fnolist()
        print("get request called")
        # print(fnolist)
        if len(fnolists) == 0:
            print("Resposnse is Empty")
              
        lststk = len(fnolists)
    except Exception as err:

        print("opps error in getting fnolist")
        print(err)   
    
    lststk = 6
    
    

    part = lststk
    if len(fnolists) > 0:
        global m
        global s
        global brk
        m = 0
        brk = 3
        s= 0
        while s < part-1 :
            print("Snap part is running")
            if brk >part-1 :
                brk = part
            # print("lets Sleep for 10 second")
            # time.sleep(10)   
            # print("oh lets awake do some work") 
            for n in range(m,brk):
                print(" running Process no :" + str(n))
                s=s+1
                try:
                    stk = fnolists[n]
                    if (stk):
                        stkname = stk + ".json"
                        # p = Process(target=worker, args=(stk, return_dict))
                        p = multiprocessing.Process(target=run, args=(stk, return_dict))
                        
                        p.start()
                        jobs.append(p)
                    # lststk = len(fnolists)
                except Exception as err:
                    print("process creation  error")
                    print(err)
            try:
                for proc in jobs:
                    proc.join()
                
            except Exception as err:
                print("joing  error")
                print(err)  
            m = brk
            brk = brk + 3
        

            
    if s > lststk-1:
        for proc in jobs:
                    proc.join()

        

        combineStockOI(fnolists,return_dict,lststk)
    print("data fetched successfully")
    return "data fetch successfully"
    # print('ulimit -n soft,hard: {},{}'.format(soft,hard))
    # print(f'Duration: {time.time() - start} seconds')
         


