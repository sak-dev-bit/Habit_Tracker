from django.db import models
from django.utils import timezone

class Habit(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    streak = models.IntegerField(default=0)
    last_completed = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

    def update_streak(self):
        today = timezone.now().date()
        if self.last_completed == today:
            return  # already done today

        if self.last_completed == today - timezone.timedelta(days=1):
            self.streak += 1
        else:
            self.streak = 1

        self.last_completed = today
        self.save()


class HabitRecord(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.habit.name} on {self.date}"
