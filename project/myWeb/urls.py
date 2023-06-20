from django.urls import path
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns



app_name='myWeb'
urlpatterns=[
    path('',views.homepage,name='homepage'),
    path('Customer view',views.Customer_view,name='Customer view'),
    path('Customer list',views.Customer_list,name='Customer list'),
    path('Phone view',views.Phone_view,name='Phone view'),
      #path('index2 ,views.Phone_view,name=Phone view')

]
urlpatterns += staticfiles_urlpatterns()

