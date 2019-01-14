from django.db import models

# Create your models here.
from django.db.models import DateTimeField


class Game(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=200, blank=True, default='')
	release_date = models.DateTimeField()
	game_category = models.CharField(max_length=200, blank=True, default='')
	played = models.BooleanField(default=False)

	class Meta:
		ordering = ('name',)


class Player(models.Model):
    name = models.CharField(max_length=50)
    genre = models.CharField(max_length=10)
    date_register = models.DateField()

class Score(models.Model):
    score = models.FloatField()
	score_date = models.DateTimeField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
