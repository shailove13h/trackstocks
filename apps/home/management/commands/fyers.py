# INSTALLATION:
# pip install fyers-apiv2
from django.core.management.base import BaseCommand
from django.conf import settings
from sqlalchemy import create_engine
# AUTHORIZATION:
from fyers_api import fyersModel
from fyers_api import accessToken
import os

import datetime
import calendar
class Command(BaseCommand):
    help = "A command to add dta from data frame to dabase"

    def handle(self, *args, **options) :

        print("fyers mangement commands")
        client_id = "VXH2Y42J29-100"
        secret_key="072Y0CJEMR"
        def get_access_token() : 
            if not os.path.exists("access_token.txt"):

               
                redirect_uri="https://www.google.com/"      
                session=accessToken.SessionModel(client_id=client_id,secret_key=secret_key,redirect_uri=redirect_uri, 
                response_type="code", grant_type="authorization_code")

                response = session.generate_authcode()  
                print("Creating New Token File")
                # scope=”The value in scope must be openid if being passed.
                # Though this is an optional field”

                # Nonce = “The value in nonce can be any random string value.
                # This is also an optional field”

            
                print("Login Url : ",response)


                # auth_code = "This will be the response of the session.generate_authcode() method once you click on the redirect_url you will be provided with the auth_code"
                auth_code = input("Enter Auth Code : s")
                session.set_token(auth_code)
                response = session.generate_token()
                print(response)
                access_token = response["access_token"]
                with open("access_token.txt","w") as f:
                    f.write(access_token)
                return access_token
                    


                # "You will be provided with the access_token which will have the below shown response" 
                # ----------------------------------------------------------------------------------------------------------------------------------------
                # Sample Success Response 
                # ---------------------------------------------------------------------------------------------------------------------------------------
                # {
                #     "s": "ok",
                #     "code": 200,
                #     "message": "",
                #     "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE2MDM4ODA4NTIsImV4cCI6MTYwMzkzMTQzMiwibmJmIjoxNjAzODgwODUyLCJhdWQiOlsieDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCZm1VZVVlSTJnYTVQR2pnNktPSXRoU1JxUklDOVlxeTdxYm1SLVEyR1NLY29OSjgxWEdXLVl1U1BjbzY1T2hESVprT1U1X2RRRUJwUE15M24zS1dQYjUyVkFnUW1BQ2JUZGNZRVRfbjJudEQ2QmYxND0iLCJkaXNwbGF5X25hbWUiOiJQSVlVU0ggUkFKRU5EUkEgS0FQU0UiLCJmeV9pZCI6IkRQMDA0MDQiLCJhcHBUeXBlIjoxMDB9.EquxH8D98KSoRzMcicIkGLszGubh_cCwwQXALP-OLOk"
                # }


                
                #(By default the async will be False, Change to True for async API calls.)
                # is_async = True
                # log_path = "This will create logs in the local system and that will be stored in the particular local address you have defined"

            else :
                with open("access_token.txt","r") as f:
                    access_token = f.read()
                return access_token

        # print(get_access_token())

        fyers = fyersModel.FyersModel(client_id=client_id, token=get_access_token(),log_path="")

        # print(fyers.get_profile())  
        # 
        startepoch = datetime.datetime(2023, 3, 11, 1, 2, 1).strftime('%s')  
        endtepoch =datetime.datetime(2023, 3, 14, 15, 15, 1).strftime('%s') 
        data = {"symbol":"NSE:FINNIFTY2331415850CE" ,"resolution":"1","date_format":"0","range_from":startepoch,"range_to":endtepoch,"cont_flag":"1"}
        print(fyers.get_profile())
        print(fyers.history(data))
