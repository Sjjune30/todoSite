from django.urls import path,include
from todoApp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('delete/<int:task_id>/',views.delete ,name = 'delete'),
    path('update/<int:id>',views.update,name='update'),
    path('cbvhome/',views.homeview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.detailview.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.updateview.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.deleteview.as_view(), name='cbvdelete'),

]