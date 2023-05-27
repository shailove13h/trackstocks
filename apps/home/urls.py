# -*- encoding: utf-8 -*-
"""
Copyright (c) 2023 - present Shailesh Vasava
"""

from django.urls import path, re_path
from apps.home import views
from apps.home.views import PersonListView,TableView

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('onetimeDatafetchSortcovering', views.onetimeDatafetchSortcovering, name='onetimeDatafetchSortcovering'),
    
    path('multiDatafetch', views.multiDatafetch, name='multiDatafetch'),
    # path('tableView', views.TableView, name='tableView'),

    path('comparisionTable', views.comparisionTable, name='comparisionTable'),
    path('peoiHiSameStrike', views.peoiHiSameStrike_data, name='peoiHiSameStrike'),
    path('onetimeDatafetchLongunwinding', views.onetimeDatafetchLongunwinding, name='onetimeDatafetchLongunwinding'),
    
    # path("people/", TableView.get_table_data(self)),
    path('people', views.Table, name ="table"),
    # path('runfunction',views.runfunction, name='runfunction'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),
    # re_path(r'^runfunction', views.runfuntion, name='runfunction')
    

]
