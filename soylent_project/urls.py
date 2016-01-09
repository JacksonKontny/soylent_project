"""soylent_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import patterns, include, url
from django.contrib import admin
from soylent_project.apps import soylent_app
from soylent_project.apps.soylent_app import urls as soylent_urls

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include(soylent_urls)),
    url(r'^api/get_foods/',
        soylent_app.views.FoodsAPI.as_view(),
        name='FoodsAPI'),
    url(r'^api/get_nutrients/',
        soylent_app.views.NutrientsAPI.as_view(),
        name='NutrientsAPI'),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
]
