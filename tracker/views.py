from django.shortcuts import render, redirect, get_object_or_404
from .models import Habit
from .forms import HabitForm

def home(request):
    habits = Habit.objects.all().order_by('-streak')
    for habit in habits:
        habit.progress_percent = min(100, (habit.streak / 30) * 100)
    form = HabitForm()
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'tracker/home.html', {'habits': habits, 'form': form})


def complete_habit(request, habit_id):
    habit = get_object_or_404(Habit, id=habit_id)
    habit.update_streak()
    return redirect('home')


def leaderboard(request):
    habits = Habit.objects.all().order_by('-streak')
    return render(request, 'tracker/leaderboard.html', {'habits': habits})
