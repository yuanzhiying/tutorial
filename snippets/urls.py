#!/usr/bin/env python3
# -*- coding: utf-8 -*-


__author__ = 'yuanzhiying'


from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from snippets import views
from rest_framework.schemas import get_schema_view


schema_view = get_schema_view(title='Pastebin API')

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^schema/$', schema_view),
]
