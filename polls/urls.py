# -*- coding: utf-8 -*-
"""
Created on Wed Jun  3 12:00:49 2020

@author: GVN
"""

from django.urls import path
from . import views

urlpatterns = [
        path('',views.home, name = "home"),
        path('home/',views.home,name = 'home'),
        path('house/',views.house,name = 'house'),
        path('add',views.add,name = 'add'),
        path('product_detail_view',views.product_detail_view, name ='product_detail_view' )
        ] 
