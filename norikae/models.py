from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)

class Route(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    route_name = models.CharField(max_length=50)
    departure_name = models.CharField(max_length=50)
    destination_name = models.CharField(max_length=50)


class Timetable(models.Model):
    route = models.ForeignKey(Route,on_delete=models.CASCADE)
    departure_time = models.DateTimeField()
    is_holiday = models.IntegerField(default=0)
    train_type = models.CharField(max_length=10,blank=True)

