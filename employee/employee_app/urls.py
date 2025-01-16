from django.urls import path
from . import views

urlpatterns =[
    path('',views.create,name="add_data"),
    path('index/',views.index,name="main_file"),
    path('edit/<sid>',views.edit,name="edit_data"),
    path('delete/<did>',views.delete)
    
]