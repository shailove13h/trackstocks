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
        
        m=0
        
        # while (datetime.now().strftime("%H:%M")) != ("15:31") :
        while m<1:
        
          
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
                
                

                # Compare Dashboard fro ce pe all oi high comprision with snap data from current cpt table
                 
                CEPE_all_oi_high_DF = pd.DataFrame.from_records((CEPE_all_oi_high.objects.all()).values())
                Multi_CEPE_all_oi_high_DF = pd.DataFrame.from_records((Multi_CEPE_all_oi_high_CPT.objects.all().order_by('-created_at')).values())
                print(Multi_CEPE_all_oi_high_DF)
                CEPE_all_oi_high_DF_len = len(CEPE_all_oi_high_DF)
                comparision_table = pd.DataFrame()

                for n in range(CEPE_all_oi_high_DF_len):
                    row_values = CEPE_all_oi_high_DF.iloc[n, :]
                    
                    underlying = row_values['underlying']
                    print(underlying)
                    strikePrice = row_values['strikePrice']
                    print("checking underlying")
                    # print(Multi_CEPE_all_oi_high_DF['underlying'])
                    
                    if underlying in Multi_CEPE_all_oi_high_DF['underlying'].values:
                        print("underlying found")
                        
                            
                        multi_DF_asPer_single = Multi_CEPE_all_oi_high_DF.loc[(Multi_CEPE_all_oi_high_DF['underlying'] == underlying) & (Multi_CEPE_all_oi_high_DF['strikePrice'] == strikePrice )]
                        
                        # print(multi_DF_asPer_single)
                        # Call Side Data Comparision
                        changeinOpenInterest_val = multi_DF_asPer_single['changeinOpenInterest']
                        changeinOpenInterest = row_values['changeinOpenInterest']
                        changeinOpenInterest_diff = changeinOpenInterest - changeinOpenInterest_val
                        
                        pchangeinOpenInterest_val = multi_DF_asPer_single['pchangeinOpenInterest']
                        pchangeinOpenInterest = row_values['pchangeinOpenInterest']
                        pchangeinOpenInterest_diff = pchangeinOpenInterest - pchangeinOpenInterest_val
                    
                        totalTradedVolume_val = multi_DF_asPer_single['totalTradedVolume']
                        totalTradedVolume = row_values['totalTradedVolume']
                        totalTradedVolume_diff = totalTradedVolume - totalTradedVolume_val
                    

                        impliedVolatility_val = multi_DF_asPer_single['impliedVolatility']
                        impliedVolatility = row_values['impliedVolatility']
                        impliedVolatility_diff = impliedVolatility - impliedVolatility_val
                    
                        change_val = multi_DF_asPer_single['change']
                        change = row_values['change']
                        change_diff = change - change_val
                    
                        pChange_val = multi_DF_asPer_single['pChange']
                        pChange = row_values['pChange']
                        pChange_diff = pChange - pChange_val
                    

                        lastPrice_val = multi_DF_asPer_single['lastPrice']
                        lastPrice = row_values['lastPrice']
                        lastPrice_diff = lastPrice - lastPrice_val
                    
                        openInterest_val = multi_DF_asPer_single['openInterest']
                        openInterest = row_values['openInterest']
                        openInterest_diff = openInterest - openInterest_val

                        openInterest_val = multi_DF_asPer_single['underlyingValue']
                        openInterest = row_values['underlyingValue']
                        underlyingValue_diff = openInterest - openInterest_val

                        # underlying_val = multi_DF_asPer_single['underlying']
                        # underlying = row_values['underlying']
                        # underlying_diff = underlying - underlying_val

                        pcr_val = multi_DF_asPer_single['pcr']
                        print("printing pcr")
                        print(pcr_val)
                        pcr = row_values['pcr']
                        pcr_diff = pcr - pcr_val
                        
                        # Put Side Data Comparision
                        
                        PE_changeinOpenInterest_val = multi_DF_asPer_single['PE_changeinOpenInterest']
                        PE_changeinOpenInterest = row_values['PE_changeinOpenInterest']
                        PE_changeinOpenInterest_diff = PE_changeinOpenInterest - PE_changeinOpenInterest_val
                        
                        PE_pchangeinOpenInterest_val = multi_DF_asPer_single['PE_pchangeinOpenInterest']
                        PE_pchangeinOpenInterest = row_values['PE_pchangeinOpenInterest']
                        PE_pchangeinOpenInterest_diff = PE_pchangeinOpenInterest - PE_pchangeinOpenInterest_val
                    
                        PE_totalTradedVolume_val = multi_DF_asPer_single['PE_totalTradedVolume']
                        PE_totalTradedVolume = row_values['PE_totalTradedVolume']
                        PE_totalTradedVolume_diff = PE_totalTradedVolume - PE_totalTradedVolume_val
                    

                        PE_impliedVolatility_val = multi_DF_asPer_single['PE_impliedVolatility']
                        PE_impliedVolatility = row_values['PE_impliedVolatility']
                        PE_impliedVolatility_diff = PE_impliedVolatility - PE_impliedVolatility_val
                    
                        PE_change_val = multi_DF_asPer_single['PE_change']
                        PE_change = row_values['PE_change']
                        PE_change_diff = PE_change - PE_change_val
                    
                        PE_pChange_val = multi_DF_asPer_single['PE_pChange']
                        PE_pChange = row_values['PE_pChange']
                        PE_pChange_diff = PE_pChange - PE_pChange_val
                    

                        PE_lastPrice_val = multi_DF_asPer_single['PE_lastPrice']
                        PE_lastPrice = row_values['PE_lastPrice']
                        PE_lastPrice_diff = PE_lastPrice - PE_lastPrice_val
                    
                        PE_openInterest_val = multi_DF_asPer_single['PE_openInterest']
                        PE_openInterest = row_values['PE_openInterest']
                        PE_openInterest_diff = PE_openInterest - PE_openInterest_val
 
                        
                    
                        compare_diff = pd.concat([changeinOpenInterest_diff,pchangeinOpenInterest_diff,totalTradedVolume_diff,impliedVolatility_diff,change_diff,pChange_diff,lastPrice_diff,openInterest_diff,pcr_diff,PE_changeinOpenInterest_diff,PE_pchangeinOpenInterest_diff,PE_totalTradedVolume_diff,PE_impliedVolatility_diff,PE_change_diff,PE_pChange_diff,PE_lastPrice_diff,PE_openInterest_diff],axis=1)
                        # print(comparision_table)

                        compare_diff['underlying'] = underlying
                        compare_diff['strikePrice'] = strikePrice
                        compare_diff['underlyingValue_diff'] = underlyingValue_diff


                        
                        compare_diff['underlyingValue'] = multi_DF_asPer_single['underlyingValue']
                        compare_diff['created_at'] = multi_DF_asPer_single['created_at']
                        compare_diff['PE_strikePrice'] = multi_DF_asPer_single['PE_strikePrice']
                        compare_diff['PE_strikePrice'] = multi_DF_asPer_single['PE_strikePrice']
                        compare_diff['PE_underlyingValue'] = multi_DF_asPer_single['PE_underlyingValue']
                        compare_diff['PE_underlying'] = multi_DF_asPer_single['PE_underlying']

                        
                        comparision_table = pd.concat([comparision_table,compare_diff])  
                        print("stike Found")
                        
                    else :
                        print(" Stock not found in table")     
                print(comparision_table)
                Comparision_CEPE_all_oi_high.objects.all().delete()
                comparision_table.to_sql(Comparision_CEPE_all_oi_high._meta.db_table, if_exists="append",con=engine, index=False)
            
                print("Comparision Table writen to database")
                
        
        
        
                # cepehioiObject= CEPE_all_oi_high.objects.filter(created_date = date.today())


            except Exception as err:
                    print("opps error")  
                    print("we have error in Comparision")
                    print(err)
        
            print(" Continue for next fectch")
            m=m+1
            # now calculate sortcoveing and long unwinding
   
            continue 
    
