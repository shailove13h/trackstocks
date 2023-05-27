# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Shailesh Vasava
"""


from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
# from .onetimesnap import onetimefuction
from django.shortcuts import render

from django.core.management.base import BaseCommand
from django.conf import settings
from sqlalchemy import create_engine
from django.db import connections
from datetime import datetime,date,timezone
from django.utils import timezone

from django.apps import apps
from apps.home.models import SimpleTable,selecttime,CEPE_all_oi_high,CE_oi_high_same_CEstrike,PE_oi_high_same_PEstrike, Multi_CEPE_all_oi_high, Multi_CE_oi_high_same_CEstrike, Multi_PE_oi_high_same_PEstrike, cepeBothhigh_OnetimeDatafetchSortcovering, ceoiHigh_OnetimeDatafetchSortcovering, peoiHigh_OnetimeDatafetchSortcovering, cepeBothhigh_onetimeDatafetchLongunwinding,ceoiHigh_onetimeDatafetchLongunwinding,peoiHigh_onetimeDatafetchLongunwinding,Comparision_CEPE_all_oi_high
import django_tables2 as tables
from django.views.generic import ListView
from django.shortcuts import redirect
from django.core.management import call_command


@login_required(login_url="/login/")
def run_command_onetime(request):
    print("command is calling now")
    if request.method == 'POST':
       
        print(call_command('add_data_onetime'))
        return HttpResponse('Command executed successfully.')
    
    else:
        print("invalid request")
        
        return HttpResponse('Invalid request method.')
    
@login_required(login_url="/login/")
def run_command_multitime(request):
    print("command is calling now")
    if request.method == 'POST':
       
        print(call_command('add_data_multitime'))
        return HttpResponse('Command executed successfully.')
      
    else:
        print("invalid request")
     
        return HttpResponse('Invalid request method.')
    

@login_required(login_url="/login/")
def run_command_comparision(request):
    print("command is calling now")
    if request.method == 'POST':
       
        print(call_command('add_data_comparision'))
        return HttpResponse('Command executed successfully.')
      
    else:
        print("invalid request")
     
        return HttpResponse('Invalid request method.')

@login_required(login_url="/login/")
def index(request):
    # context = {'segment': 'index'}

    # html_template = loader.get_template('home/profile.html')
    # return HttpResponse(html_template.render(context, request))


    if request.user.is_authenticated:
        if request.user.is_staff:
            # Redirect staff users to a specific page
            return redirect('home/adminuser.html')  # Replace 'staff_dashboard' with the appropriate URL or view name for the staff dashboard
        else:
            # Regular authenticated users can continue to the profile page
            context = {'segment': 'index'}
            html_template = loader.get_template('home/profile.html')
            return HttpResponse(html_template.render(context, request))
    else:
        # Redirect anonymous users to the login page
        return redirect('login')  # Replace 'login' with the appropriate URL or view name for the login page

@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template


        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



@login_required(login_url="/login/")
def onetimeDatafetchSortcovering(request):

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        
        dates = request.POST['date']

        print("This is date : ", dates)
        # print(dates.strftime("%m/%d/%y"))
        cepehioiObject= cepeBothhigh_OnetimeDatafetchSortcovering.objects.filter(created_date = dates).order_by('-created_at')
        ceoihiObject   = ceoiHigh_OnetimeDatafetchSortcovering.objects.filter(created_date = dates).order_by('-created_at')
        peoihiObject   = peoiHigh_OnetimeDatafetchSortcovering.objects.filter(created_date = dates).order_by('-created_at')
    else :
        cepehioiObject= cepeBothhigh_OnetimeDatafetchSortcovering.objects.filter(created_date = date.today()).order_by('-created_at')
        ceoihiObject   = ceoiHigh_OnetimeDatafetchSortcovering.objects.filter(created_date = date.today()).order_by('-created_at')
        peoihiObject   = peoiHigh_OnetimeDatafetchSortcovering.objects.filter(created_date = date.today()).order_by('-created_at')
    selecttimes = selecttime.objects.all().order_by('-created_at')

    # created_date = date.today()
    html_template = loader.get_template('home/onetimeDatafetchSortcovering.html')
    return HttpResponse(html_template.render({"cepehioi" : cepehioiObject, "ceoihi" : ceoihiObject, "peoihi" : peoihiObject , "selecttime" : selecttimes }, request))
   

@login_required(login_url="/login/")
def onetimeDatafetchLongunwinding(request) :

    print(timezone.now())
    print(date.today())
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        
        dates = request.POST['date']

        print("This is date : ", dates)
        cepehioiObject=cepeBothhigh_onetimeDatafetchLongunwinding.objects.filter(created_date  = dates).order_by('-created_at')
        ceoihiObject= ceoiHigh_onetimeDatafetchLongunwinding.objects.filter(created_date  = dates).order_by('-created_at')
        peoihiObject= peoiHigh_onetimeDatafetchLongunwinding.objects.filter(created_date  = dates).order_by('-created_at')
    
    else :
        cepehioiObject=cepeBothhigh_onetimeDatafetchLongunwinding.objects.filter(created_date = date.today()).order_by('-created_at')
        ceoihiObject= ceoiHigh_onetimeDatafetchLongunwinding.objects.filter(created_date = date.today()).order_by('-created_at')
        peoihiObject= peoiHigh_onetimeDatafetchLongunwinding.objects.filter(created_date = date.today()).order_by('-created_at')
        
    selecttimes = selecttime.objects.all().order_by('-created_at')
    html_template = loader.get_template('home/onetimeDatafetchLongunwinding.html')

    return HttpResponse(html_template.render({"cepehioi" : cepehioiObject, "ceoihi" : ceoihiObject, "peoihi" : peoihiObject,"selecttime" : selecttimes }, request))



@login_required(login_url="/login/")
def multiDatafetch(request):
    
    # hioiObject= CEPE_all_oi_high.objects.raw('SELECT * FROM public.home_ce_oi_high_same_cestrike  ')
    # html_template = loader.get_template('home/ceoiHiSameStrike.html')
    print(timezone.now())
    print(date.today())
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        
        dates = request.POST['date']

        print("This is date : ", dates)
        cepehioiObject= Multi_CEPE_all_oi_high.objects.filter(changeinOpenInterest__lt =0, change__gt = 0, PE_changeinOpenInterest__gt = 0, PE_change__lt =0 , created_date = dates).order_by('-created_at')
        ceoihiObject= Multi_CE_oi_high_same_CEstrike.objects.filter(changeinOpenInterest__lt =0, change__gt = 0, PE_changeinOpenInterest__gt = 0, PE_change__lt =0, created_date = dates).order_by('-created_at')
        peoihiObject= Multi_PE_oi_high_same_PEstrike.objects.filter(changeinOpenInterest__lt =0, change__gt = 0, PE_changeinOpenInterest__gt = 0, PE_change__lt =0,  created_date = dates).order_by('-created_at')
    

    else : 
        cepehioiObject= Multi_CEPE_all_oi_high.objects.filter(changeinOpenInterest__lt =0, change__gt = 0, PE_changeinOpenInterest__gt = 0, PE_change__lt =0 , created_date = date.today()).order_by('-created_at')
        ceoihiObject= Multi_CE_oi_high_same_CEstrike.objects.filter(changeinOpenInterest__lt =0, change__gt = 0, PE_changeinOpenInterest__gt = 0, PE_change__lt =0, created_date = date.today()).order_by('-created_at')
        peoihiObject= Multi_PE_oi_high_same_PEstrike.objects.filter(changeinOpenInterest__lt =0, change__gt = 0, PE_changeinOpenInterest__gt = 0, PE_change__lt =0,  created_date = date.today()).order_by('-created_at')
        
    html_template = loader.get_template('home/multitimeData.html')

    selecttimes = selecttime.objects.all().order_by('-created_at')
    return HttpResponse(html_template.render({"cepehioi" : cepehioiObject, "ceoihi" : ceoihiObject, "peoihi" : peoihiObject,"selecttime" : selecttimes }, request))


    
    # return HttpResponse(html_template.render({"ceoihi" : hioiObject}, request))
@login_required(login_url="/login/")    
def comparisionTable(request):
    
    # hioiObject= CEPE_all_oi_high.objects.raw('SELECT * FROM public.home_ce_oi_high_same_cestrike  ')
    # html_template = loader.get_template('home/ceoiHiSameStrike.html')
    print(timezone.now())
    print(date.today())
    html_template = loader.get_template('home/comparision_multitimeData.html')

    # cepehioiObject= Multi_CEPE_all_oi_high.objects.filter(changeinOpenInterest__lt =0, change__gt = 0, PE_changeinOpenInterest__gt = 0, PE_change__lt =0 , created_date = date.today()).order_by('-created_at')
    

    ceoihiObject= Comparision_CEPE_all_oi_high.objects.all()
    # html_template = loader.get_template('home/ceoiHiSameStrike.html')
    
    # peoihiObject= Multi_PE_oi_high_same_PEstrike.objects.filter(changeinOpenInterest__lt =0, change__gt = 0, PE_changeinOpenInterest__gt = 0, PE_change__lt =0,  created_date = date.today()).order_by('-created_at')
    # html_template = loader.get_template('home/peoiHiSameStrike.html')

    # return HttpResponse(html_template.render({"cepehioi" : cepehioiObject, "ceoihi" : ceoihiObject, "peoihi" : peoihiObject }, request))


    return HttpResponse(html_template.render({"ceoihi" : ceoihiObject}, request))




@login_required(login_url="/login/")
def peoiHiSameStrike_data(request):
    
    hioiObject= CEPE_all_oi_high.objects.raw('SELECT * FROM public.home_pe_oi_high_same_pestrike  ')
    html_template = loader.get_template('home/peoiHiSameStrike.html')
    
    return HttpResponse(html_template.render({"peoihi" : hioiObject}, request))

class TableView(tables.SingleTableView):
    table_class = SimpleTable
    queryset = cepeBothhigh_OnetimeDatafetchSortcovering.objects.all()
    template_name = "home/simple_list.html"


def Table(request):
    # df = pd.read_csv("tableview/static/csv/20_Startups.csv")
    #'tableview/static/csv/20_Startups.csv' is the django 
    # directory where csv file exist.
    # Manipulate DataFrame using to_html() function
    cepeBothhigh= cepeBothhigh_OnetimeDatafetchSortcovering.objects.all()
    # geeks_object = cepeBothhigh.to_html()
    print(cepeBothhigh)
    return HttpResponse(cepeBothhigh)


class PersonListView(ListView):
    model = cepeBothhigh_OnetimeDatafetchSortcovering
    template_name = 'home/simple_list.html'


    