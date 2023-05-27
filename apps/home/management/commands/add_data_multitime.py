# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Shailesh Vasava
"""

from django.core.management.base import BaseCommand
from django.conf import settings
from sqlalchemy import create_engine
import pandas as pd
from openpyxl import Workbook
from apps.home.models import Multi_CEPE_all_oi_high,Multi_CE_oi_high_same_CEstrike ,Multi_PE_oi_high_same_PEstrike,CEPE_all_oi_high,Multi_CEPE_all_oi_high_CPT,Multi_CE_oi_high_same_CEstrike_CPT ,Multi_PE_oi_high_same_PEstrike_CPT, Comparision_CEPE_all_oi_high
from .startMulti import *
from .onetimesnap import *
from django.http import HttpResponse
from datetime import datetime,date

class Command(BaseCommand):
    help = "A command to add dta from data frame to dabase"

    def handle(self, *args, **options) :

        print("mangement commands")
        
        
        while (datetime.now().strftime("%H:%M")) != ("15:31") :
            cepe_all_hi, ceOiHigh_sameStrike, peOiHigh_sameStrike = onetimefuction()
   
            # write data to datbase table High_OI_both_Side
            
            # print(df)
            # Write the DataFrame to the database
            
            user = settings.DATABASES['default'] ['USER']
            password = settings.DATABASES['default'] ['PASSWORD']
            database_name  = settings.DATABASES['default'] ['NAME']
            database_url = 'postgresql://{user}:{password}@localhost:5432/{database_name}'.format(
                user = user,
                password = password,
                database_name = database_name

            )
            engine = create_engine(database_url, echo = False)
            try :
                # write data to datbase table High_OI_both_Side
                cepe_all_hi.to_sql(Multi_CEPE_all_oi_high._meta.db_table, if_exists="append",con=engine, index=False)
                ceOiHigh_sameStrike.to_sql(Multi_CE_oi_high_same_CEstrike._meta.db_table, if_exists="append",con=engine, index=False)
                peOiHigh_sameStrike.to_sql(Multi_PE_oi_high_same_PEstrike._meta.db_table, if_exists="append",con=engine, index=False)
                
                
                print("Multi time data writen to database")
                # delete record from CPT table and add new record so snap and current can be compared

                Multi_CEPE_all_oi_high_CPT.objects.all().delete()
                Multi_CE_oi_high_same_CEstrike_CPT.objects.all().delete()
                Multi_PE_oi_high_same_PEstrike_CPT.objects.all().delete()

                cepe_all_hi.to_sql(Multi_CEPE_all_oi_high_CPT._meta.db_table, if_exists="append",con=engine, index=False)
                ceOiHigh_sameStrike.to_sql(Multi_CE_oi_high_same_CEstrike_CPT._meta.db_table, if_exists="append",con=engine, index=False)
                peOiHigh_sameStrike.to_sql(Multi_PE_oi_high_same_PEstrike_CPT._meta.db_table, if_exists="append",con=engine, index=False)
                


                # Compare Dashboard fro ce pe all oi high comprision with snap data from current cpt table
            #     # try :
            #     #     num =0
                    
            #     #     CEPE_all_oi_high_DF = pd.DataFrame.from_records((CEPE_all_oi_high.objects.all()).values())
            #     #     Multi_CEPE_all_oi_high_DF = pd.DataFrame.from_records((Multi_CEPE_all_oi_high_CPT.objects.all().order_by('-created_at')).values())
            #     #     print(Multi_CEPE_all_oi_high_DF)
            #     #     CEPE_all_oi_high_DF_len = len(CEPE_all_oi_high_DF)
            #     #     comparision_table = pd.DataFrame()

            #     #     for n in range(CEPE_all_oi_high_DF_len):
            #     #         row_values = CEPE_all_oi_high_DF.iloc[n, :]
                        
            #     #         underlying = row_values['underlying']
            #     #         print(underlying)
            #     #         strikePrice = row_values['strikePrice']
            #     #         print("checking underlying")
            #     #         print(Multi_CEPE_all_oi_high_DF['underlying'])
                        
            #     #         if underlying in Multi_CEPE_all_oi_high_DF['underlying'].values:
            #     #             print("underlying found")
                            
                                
            #     #             multi_DF_asPer_single = Multi_CEPE_all_oi_high_DF.loc[(Multi_CEPE_all_oi_high_DF['underlying'] == underlying) & (Multi_CEPE_all_oi_high_DF['strikePrice'] == strikePrice )]
                            
            #     #             print(multi_DF_asPer_single)
                            
            #     #             changeinOpenInterest_val = multi_DF_asPer_single['changeinOpenInterest']
            #     #             changeinOpenInterest = row_values['changeinOpenInterest']
            #     #             changeinOpenInterest_diff = changeinOpenInterest - changeinOpenInterest_val
                            
            #     #             pchangeinOpenInterest_val = multi_DF_asPer_single['pchangeinOpenInterest']
            #     #             pchangeinOpenInterest = row_values['pchangeinOpenInterest']
            #     #             pchangeinOpenInterest_diff = pchangeinOpenInterest - pchangeinOpenInterest_val
                        
            #     #             totalTradedVolume_val = multi_DF_asPer_single['totalTradedVolume']
            #     #             totalTradedVolume = row_values['totalTradedVolume']
            #     #             totalTradedVolume_diff = totalTradedVolume - totalTradedVolume_val
                        

            #     #             impliedVolatility_val = multi_DF_asPer_single['impliedVolatility']
            #     #             impliedVolatility = row_values['impliedVolatility']
            #     #             impliedVolatility_diff = impliedVolatility - impliedVolatility_val
                        
            #     #             change_val = multi_DF_asPer_single['change']
            #     #             change = row_values['change']
            #     #             change_diff = change - change_val
                        
            #     #             pChange_val = multi_DF_asPer_single['pChange']
            #     #             pChange = row_values['pChange']
            #     #             pChange_diff = pChange - pChange_val
                        

            #     #             lastPrice_val = multi_DF_asPer_single['lastPrice']
            #     #             lastPrice = row_values['lastPrice']
            #     #             lastPrice_diff = lastPrice - lastPrice_val
                        
            #     #             openInterest_val = multi_DF_asPer_single['openInterest']
            #     #             openInterest = row_values['openInterest']
            #     #             openInterest_diff = openInterest - openInterest_val

            #     #             # underlying_val = multi_DF_asPer_single['underlying']
            #     #             # underlying = row_values['underlying']
            #     #             # underlying_diff = underlying - underlying_val

            #     #             pcr_val = multi_DF_asPer_single['pcr']
            #     #             print("printing pcr")
            #     #             print(pcr_val)
            #     #             pcr = row_values['pcr']
            #     #             pcr_diff = pcr - pcr_val

                            
                        
            #     #             compare_diff = pd.concat([changeinOpenInterest_diff,pchangeinOpenInterest_diff,totalTradedVolume_diff,impliedVolatility_diff,change_diff,pChange_diff,lastPrice_diff,openInterest_diff,pcr_diff],axis=1)
            #     #             print(comparision_table)

            #     #             compare_diff['underlying'] = underlying
            #     #             comparision_table = pd.concat([comparision_table,compare_diff])  
            #     #             print("stike Found")
                            
            #     #         else :
            #     #             print(" Stock not found in table")     
            #     #     print(comparision_table)
            #     #     Comparision_CEPE_all_oi_high.objects.all().delete()
            #     #     comparision_table.to_sql(Comparision_CEPE_all_oi_high._meta.db_table, if_exists="append",con=engine, index=False)
               
            #     #     print("Comparision Table writen to database")
                    
            
            
            
            #         # cepehioiObject= CEPE_all_oi_high.objects.filter(created_date = date.today())


            #     except Exception as err:
            #             print("opps error")  
            #             print("we have error in Comparision")
            #             print(err)
            except Exception as err:
                    print("opps error")  
                    print(err)
                # df.to_sql(High_OI_both_Side._meta.db_table, if_exists="append",con=engine, index=False)
            print(" Continue for next fectch")

            # now calculate sortcoveing and long unwinding

            
            continue 
    

def onetimefuction():
    
    
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
    
    # lststk = 2
    part = lststk
    

   
    if len(fnolists) > 0:
        global m
        global s
        global brk
        m = 0
        brk = 50
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
                        stkjobnamename = stk + "job"
                        # p = Process(target=worker, args=(stk, return_dict))
                        stkjobnamename = multiprocessing.Process(target=run, args=(stk, return_dict))
                        
                        stkjobnamename.start()
                        jobs.append(stkjobnamename)
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
            brk = brk + 50
            for proc in jobs:


                cp = proc.close()
                print("closing process : " + str(cp))
            jobs.clear() 


        

            
    if s > lststk-1:
        for proc in jobs:
                    proc.join()

        

        # below is from combine function
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
            'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty','bidprice', 'askQty', 'askPrice'], axis=1)[['changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','lastPrice','openInterest','strikePrice','underlyingValue','underlying','pcr']]
        ce_chain_all_high = pd.DataFrame(ce_chain_all_high_r)
        ce_chain_all_high['created_at'] = datetime.now()
        ce_chain_all_high['created_date'] = date.today()
        
       

        pe_chain_all_high=pe_chain_all_high.drop([
        'identifier','totalBuyQuantity', 'totalSellQuantity','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice',], axis=1)[['strikePrice','openInterest','lastPrice','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','underlyingValue','underlying','pcr']]
        pe_chain_all_high.rename(columns = {'strikePrice': 'PE_strikePrice','openInterest': 'PE_openInterest','lastPrice':'PE_lastPrice','changeinOpenInterest': 'PE_changeinOpenInterest','pchangeinOpenInterest': 'PE_pchangeinOpenInterest','totalTradedVolume':'PE_totalTradedVolume','impliedVolatility': 'PE_impliedVolatility','change' : 'PE_change','pChange': 'PE_pChange','underlyingValue' : 'PE_underlyingValue','underlying' : 'PE_underlying'}, inplace = True)
        
        ce_chain_all_high.reset_index(inplace = True, drop = True)
        pe_chain_all_high.reset_index(inplace = True, drop = True)
        cepe_all_hi = pd.concat([ce_chain_all_high, pe_chain_all_high], axis=1)


        ce_chain_Same_Strike_high_OI_CE = ce_chain_Same_Strike_high_OI_CE.drop([
            'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty','bidprice', 'askQty', 'askPrice'], axis=1)[['changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','lastPrice','openInterest','strikePrice','underlyingValue','underlying','pcr']]
        ce_chain_Same_Strike_high_OI_CE = pd.DataFrame(ce_chain_Same_Strike_high_OI_CE)
        ce_chain_Same_Strike_high_OI_CE['created_at'] = datetime.now()
        ce_chain_Same_Strike_high_OI_CE['created_date'] = date.today()

        pe_chain__Same_Strike_high_OI_CE = pe_chain__Same_Strike_high_OI_CE.drop([
        'identifier','totalBuyQuantity', 'totalSellQuantity','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice',], axis=1)[['strikePrice','openInterest','lastPrice','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','underlyingValue','underlying','pcr']]
        pe_chain__Same_Strike_high_OI_CE.rename(columns = {'strikePrice': 'PE_strikePrice','openInterest': 'PE_openInterest','lastPrice':'PE_lastPrice','changeinOpenInterest': 'PE_changeinOpenInterest','pchangeinOpenInterest': 'PE_pchangeinOpenInterest','totalTradedVolume':'PE_totalTradedVolume','impliedVolatility': 'PE_impliedVolatility','change' : 'PE_change','pChange': 'PE_pChange','underlyingValue' : 'PE_underlyingValue','underlying' : 'PE_underlying'}, inplace = True)

        ce_chain_Same_Strike_high_OI_CE.reset_index(inplace = True, drop = True)
        pe_chain__Same_Strike_high_OI_CE.reset_index(inplace = True, drop = True)
        ceOiHigh_sameStrike = pd.concat([ce_chain_Same_Strike_high_OI_CE, pe_chain__Same_Strike_high_OI_CE], axis=1)
       
    
        ce_chain_Same_Strike_high_OI_PE = ce_chain_Same_Strike_high_OI_PE.drop([
            'identifier','totalBuyQuantity','totalSellQuantity', 'expiryDate','bidQty','bidprice', 'askQty', 'askPrice'], axis=1)[['changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','lastPrice','openInterest','strikePrice','underlyingValue','underlying','pcr']]
        ce_chain_Same_Strike_high_OI_PE = pd.DataFrame(ce_chain_Same_Strike_high_OI_PE)
        ce_chain_Same_Strike_high_OI_PE['created_at'] = datetime.now()
        ce_chain_Same_Strike_high_OI_PE['created_date'] = date.today()

        pe_chain__Same_Strike_high_OI_PE=pe_chain__Same_Strike_high_OI_PE.drop([
        'identifier','totalBuyQuantity', 'totalSellQuantity','expiryDate','bidQty', 'bidprice', 'askQty', 'askPrice',], axis=1)[['strikePrice','openInterest','lastPrice','changeinOpenInterest','pchangeinOpenInterest','totalTradedVolume','impliedVolatility','change','pChange','underlyingValue','underlying','pcr']]
        pe_chain__Same_Strike_high_OI_PE.rename(columns = {'strikePrice': 'PE_strikePrice','openInterest': 'PE_openInterest','lastPrice':'PE_lastPrice','changeinOpenInterest': 'PE_changeinOpenInterest','pchangeinOpenInterest': 'PE_pchangeinOpenInterest','totalTradedVolume':'PE_totalTradedVolume','impliedVolatility': 'PE_impliedVolatility','change' : 'PE_change','pChange': 'PE_pChange','underlyingValue' : 'PE_underlyingValue','underlying' : 'PE_underlying'}, inplace = True)
        
        ce_chain_Same_Strike_high_OI_PE.reset_index(inplace = True, drop = True)
        pe_chain__Same_Strike_high_OI_PE.reset_index(inplace = True, drop = True)

        peOiHigh_sameStrike = pd.concat([ce_chain_Same_Strike_high_OI_PE, pe_chain__Same_Strike_high_OI_PE], axis=1)

        
        # print(cdpe_all_hi)
    for proc in jobs:

        proc.close()
    jobs.clear() 
    
    return cepe_all_hi, ceOiHigh_sameStrike, peOiHigh_sameStrike


        
        

    