from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('write', views.write),
    path('view/<int:boardidx>', views.view),
    path('modify/<int:boardidx>', views.modify),
    path('delete/<int:boardidx>', views.delete),
]