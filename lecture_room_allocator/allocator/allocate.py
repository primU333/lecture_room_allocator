from datetime import datetime, timedelta
from django_q.tasks import schedule
from django_q.models import Schedule
from .models import *
from .views import allocate_rooms


def alloctate():
    rooms = Room.objects.all()
    today = datetime.now()

    formatted_time = today.strftime("%l:%M%P")
    day_name = today.strftime("%A")

    if today.minute == 0 and today.second == 0:
        formatted_time = today.strftime("%l:%M%P")
        current_ass_time = formatted_time
        day_name = today.strftime("%A")
        today_day = day_name

    lecs = Lecture.objects.all()
    active_lectures = []
    for lec in lecs:
        if lec.duration.start_time == current_ass_time and lec.day.day == today_day:
            active_lectures.append(lec)
        else:
            pass

    print('Lectures', active_lectures)
    
    allocate_rooms(active_lectures, list(rooms))


schedule(
    name='Allocate Lecture Rooms',
    func='allocator.allocate.alloctate',
    schedule_type=Schedule.HOURLY,
    next_run=datetime.now() + timedelta(hours=1)
)
