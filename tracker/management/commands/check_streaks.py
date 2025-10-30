from django.core.management.base import BaseCommand
from django.utils import timezone
from tracker.models import Habit

class Command(BaseCommand):
    help = 'Check and reset streaks for habits not completed yesterday'

    def handle(self, *args, **options):
        today = timezone.now().date()
        yesterday = today - timezone.timedelta(days=1)
        habits = Habit.objects.all()
        for habit in habits:
            if habit.last_completed and habit.last_completed < yesterday:
                habit.streak = 0
                habit.save()
                self.stdout.write(f'Reset streak for {habit.name}')
        self.stdout.write('Streak check completed')