from djongo import models
from bson import ObjectId

class Team(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, related_name='members')
    is_superhero = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Activity(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='activities')
    activity_type = models.CharField(max_length=100)
    duration_minutes = models.PositiveIntegerField()
    date = models.DateField()

    def __str__(self):
        return f"{self.user.name} - {self.activity_type}"

class Workout(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    suggested_for = models.ManyToManyField(Team, related_name='workouts')

    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    id = models.ObjectIdField(primary_key=True, default=ObjectId)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='leaderboards')
    total_points = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.team.name} - {self.total_points} points"
