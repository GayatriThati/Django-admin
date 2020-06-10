# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 11:03:36 2020

@author: GVN
"""
from django.urls import path
from . import views

urlpatterns = {
        path('',views.index,name='index')
        }