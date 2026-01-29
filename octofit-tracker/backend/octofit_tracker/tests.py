from django.test import TestCase
from rest_framework.test import APIClient
from .models import Team, UserProfile, Activity, Workout, Leaderboard
from django.urls import reverse

class APITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.team = Team.objects.create(name='Test Team', description='A test team')
        self.user = UserProfile.objects.create(email='test@example.com', name='Test User', team=self.team)
        self.workout = Workout.objects.create(name='Test Workout', description='A test workout')
        self.workout.suggested_for.set([self.team])
        self.activity = Activity.objects.create(user=self.user, activity_type='Test', duration_minutes=10, date='2026-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, total_points=100)

    def test_api_root(self):
        response = self.client.get(reverse('api-root'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('users', response.data)
        self.assertIn('teams', response.data)
        self.assertIn('activities', response.data)
        self.assertIn('workouts', response.data)
        self.assertIn('leaderboards', response.data)

    def test_user_list(self):
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, 200)

    def test_team_list(self):
        response = self.client.get('/api/teams/')
        self.assertEqual(response.status_code, 200)

    def test_activity_list(self):
        response = self.client.get('/api/activities/')
        self.assertEqual(response.status_code, 200)

    def test_workout_list(self):
        response = self.client.get('/api/workouts/')
        self.assertEqual(response.status_code, 200)

    def test_leaderboard_list(self):
        response = self.client.get('/api/leaderboards/')
        self.assertEqual(response.status_code, 200)
