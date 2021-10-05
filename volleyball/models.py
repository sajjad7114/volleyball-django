from django.db import models
from django.contrib.auth.models import User
import datetime

# Create your models here.


class Stadium(models.Model):
    name = models.CharField(max_length=50)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Match(models.Model):
    teamA = models.CharField(max_length=20)
    teamB = models.CharField(max_length=20)
    date = models.DateField()
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE)
    available_seats = models.TextField()
    ticket_price = models.PositiveIntegerField()

    def __str__(self):
        return str(self.teamA) + ' vs. ' + str(self.teamB)

    def available_list(self):
        arr = str(self.available_seats).split(',')
        result = []
        for i in arr:
            try:
                result.append(int(i))
            except:
                pass
        return result


class TransAction(models.Model):
    amount = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    success = models.BooleanField()

# {
#     "amount": 4000,
#     "success": "True"
# }


class Seat(models.Model):
    index = models.PositiveIntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    transaction = models.OneToOneField(TransAction, on_delete=models.CASCADE)
