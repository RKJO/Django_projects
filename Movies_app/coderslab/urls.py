"""coderslab URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path
from exercises.views import *
from homework.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    re_path(r'^articles', articles),
    re_path(r'^show_band/(?P<id>\d+)', show_band),
    re_path(r'^movies/', movies),
    re_path(r'^movie_details/(?P<id>\d+)', movie_details),
    re_path(r'^persons', persons),
    re_path(r'^edit_person/(?P<id>\d+)', edit_person),
    re_path(r'^add_person', add_person),
    re_path(r'^edit_movie/(?P<id>\d+)', edit_movie),
    re_path(r'^add_movie', add_movie),

    re_path(r'^show_range/(?P<start>\d+)/(?P<end>\d+)$', show_range),
    re_path(r'^show_multiplication/(?P<height>(\d)+)/(?P<width>(\d)+)$', show_multiplication),
    # re_path(r'^hello', hello),
    re_path(r'^temp_convert', temp_convert),
    re_path(r'^setSession', setSession),
    re_path(r'^showSession', showSession),
    re_path(r'^deleteSession', deleteSession),
    re_path(r'^login', login),
    re_path(r'^addToSession', addToSession),
    re_path(r'^show_all_session_values', show_all_session_values),
    re_path(r'^set_cookie', set_cookie),
    re_path(r'^show_cookie', show_cookie),
    re_path(r'^logout', logout),
    # re_path(r'^addToCookie', addToCookie),
    re_path(r'^AddToCookie', AddToCookie.as_view()),
    re_path(r'^showAllCookies', showAllCookies),
    re_path(r'^random/(?P<min_number>(\d){2})/(?P<max_number>(\d){2,4})$', show_number3),
    re_path(r'^hello/(?P<name>([A-Z]{1})([a-z])+)$', hello_name),
    # re_path(r'^hello/(?P<name>)', hello_name),
]




