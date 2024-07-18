from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insertData, name='insert_data'),
    path('update/<int:id>/', views.updateData, name='update_data'),
    path('delete/<int:id>/', views.deleteData, name='delete_data'),
]