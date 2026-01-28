
from django.core.management.base import BaseCommand
from octofit_tracker.models import Team, UserProfile, Activity, Workout, Leaderboard
from django.utils import timezone
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'


    def handle(self, *args, **kwargs):
        # Drop collections directly for a clean slate
        db = connection.cursor().db_conn.client['octofit_db']
        for col in ['activity', 'leaderboard', 'workout', 'userprofile', 'team']:
            db[col].drop()



        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Team Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='Team DC Superheroes')

        # Create users
        users = [
            UserProfile.objects.create(email='ironman@marvel.com', name='Iron Man', team=marvel),
            UserProfile.objects.create(email='captainamerica@marvel.com', name='Captain America', team=marvel),
            UserProfile.objects.create(email='spiderman@marvel.com', name='Spider-Man', team=marvel),
            UserProfile.objects.create(email='batman@dc.com', name='Batman', team=dc),
            UserProfile.objects.create(email='superman@dc.com', name='Superman', team=dc),
            UserProfile.objects.create(email='wonderwoman@dc.com', name='Wonder Woman', team=dc),
        ]

        # Create activities
        for user in users:
            Activity.objects.create(user=user, activity_type='Running', duration_minutes=30, date=timezone.now().date())
            Activity.objects.create(user=user, activity_type='Cycling', duration_minutes=45, date=timezone.now().date())

        # Create workouts
        w1 = Workout.objects.create(name='Hero HIIT', description='High intensity interval training for heroes')
        w2 = Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility')
        w1.suggested_for.set([marvel, dc])
        w2.suggested_for.set([dc])

        # Create leaderboards
        Leaderboard.objects.create(team=marvel, total_points=150)
        Leaderboard.objects.create(team=dc, total_points=180)

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data!'))
