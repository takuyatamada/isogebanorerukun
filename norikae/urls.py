from django.urls import path

from . import views
from .models import User,Route
app_name = 'norikae'
urlpatterns = [
    path('', views.index, name='index'),
    path('input_user_name/',views.input_user_name,name='input_user_name'),
    path('record_user',views.record_user,name='record_user'),
    path('show_users',views.show_users,name='show_users'),
    path('<int:user_id>/',views.detail,name='detail'),
]