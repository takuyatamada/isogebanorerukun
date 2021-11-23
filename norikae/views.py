from django.http import HttpResponse
from django.shortcuts import render

from .models import User,Route
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, user_id):
    return HttpResponse("You're looking at question %s." % user_id)

def input_user_name(request):
    return render(request,'norikae/input_user_name.html')

def record_user(request):
    user_name = request.POST['user_name']
    User.objects.create(user_name=user_name)
    return render(request,'norikae/input_user_name.html')

def show_users(request):
    users = User.objects.all()
    content = {
        'users':users,
    }
    # pmf_engine.make_prediction_data()
    # pmf_engine.build_model()
    return render(request,'norikae/show_users.html',content)