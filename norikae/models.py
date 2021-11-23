from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)

class Route(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=50)

class Timetable(models.Model):
    route_id = models.ForeignKey(Route,on_delete=models.CASCADE)
    time = models.IntegerField(default=0)

