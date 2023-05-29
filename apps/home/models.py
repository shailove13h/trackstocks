# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Shailesh Vasava
"""
from django.contrib.auth.models import User
from django.db import models
import django_tables2 as tables

# Create your models here.


class selecttime(models.Model) : 
    # for call side
    
    id = models.AutoField(primary_key=True)
    
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)


# <-- one time data models start
class CEPE_all_oi_high(models.Model) : 
    # for call side
    
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)
    

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

class CE_oi_high_same_CEstrike(models.Model) : 
    # CE oi highest cepestrike same 
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)
    

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

class PE_oi_high_same_PEstrike(models.Model) : 
    # PE oi highest cepestrike same 
    
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)
    

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

# <-- one time data models Ends here



# <-- Multi time data models start

class Multi_CEPE_all_oi_high(models.Model) : 
    # for call side
    
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

class Multi_CE_oi_high_same_CEstrike(models.Model) : 
    # CE oi highest cepestrike same 
    
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

class Multi_PE_oi_high_same_PEstrike(models.Model) : 

    # PE oi highest cepestrike same 
    
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)
    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

#    Multi time data models End ---->


# <-- Multi but at time one snap FOr Comparision time  models start
# CPT means Comparision Table

class Multi_CEPE_all_oi_high_CPT(models.Model) : 
    # for call side
    
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

class Multi_CE_oi_high_same_CEstrike_CPT(models.Model) : 
    # CE oi highest cepestrike same 
    
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

class Multi_PE_oi_high_same_PEstrike_CPT(models.Model) : 

    # PE oi highest cepestrike same 
    
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)
    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

#    Multi but at time one snap time data models End ---->


# sortcovering data Tables

class OnetimeDatafetchSortcovering(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)



#long unwinding Data Tables

class onetimeDatafetchLongunwinding(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)



class cepeBothhigh_OnetimeDatafetchSortcovering(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

class ceoiHigh_OnetimeDatafetchSortcovering(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)

class peoiHigh_OnetimeDatafetchSortcovering(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    
    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)


#long unwinding Data Tables

class cepeBothhigh_onetimeDatafetchLongunwinding(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)


class ceoiHigh_onetimeDatafetchLongunwinding(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)


class peoiHigh_onetimeDatafetchLongunwinding(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)


# Comparision Dashord from Comparision_CEPE_all_oi_high

class Comparision_CEPE_all_oi_high(models.Model) :
    id = models.AutoField(primary_key=True)
    changeinOpenInterest = models.FloatField(max_length=25, null=True)
    pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    totalTradedVolume	= models.IntegerField(null=True)
    impliedVolatility	= models.FloatField(max_length=25, null=True)
    change	=models.FloatField(max_length=25, null=True)
    pChange	= models.FloatField(max_length=25, null=True)
    lastPrice = models.FloatField(max_length=25, null=True)
    openInterest = models.FloatField(max_length=25, null=True)
    strikePrice	 = models.IntegerField(null=True)
    underlyingValue = models.FloatField(max_length=25, null=True)
    underlying = models.CharField (max_length=25, null=True)
    underlyingValue_diff = models.FloatField(max_length=25, null=True)
    pcr = models.FloatField(max_length=25, null=True)
    created_at = models.DateTimeField( null=True, blank=True)
    created_date = models.DateField(null=True)

    #  for puteside
    PE_changeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_pchangeinOpenInterest = models.FloatField(max_length=25, null=True)
    PE_totalTradedVolume	= models.IntegerField(null=True)
    PE_impliedVolatility	= models.FloatField(max_length=25, null=True)
    PE_change	=models.FloatField(max_length=25, null=True)
    PE_pChange	= models.FloatField(max_length=25, null=True)
    PE_lastPrice = models.FloatField(max_length=25, null=True)
    PE_openInterest = models.FloatField(max_length=25, null=True)
    PE_strikePrice	 = models.IntegerField(null=True)
    PE_underlyingValue = models.FloatField(max_length=25, null=True)
    PE_underlying = models.CharField (max_length=25, null=True)




class SimpleTable(tables.Table):
    class Meta:
        model = cepeBothhigh_OnetimeDatafetchSortcovering



