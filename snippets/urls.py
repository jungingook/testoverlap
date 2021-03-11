from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('screen_list/<str:user_id>', list_screen),
    path('test/<str:userid>', views.test)
]