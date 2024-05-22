from django.shortcuts import render
from .models import *
from datetime import datetime


def home(request):

    rooms = Room.objects.all()
    today = datetime.now()

    context = {
        'rooms' : rooms,
    }
    return render(request, 'allocator/index.html', context)



def rooms(request):
    all_rooms = Room.objects.all()
    context = {
        'rooms' : all_rooms,
        'title' : 'Lecture Rooms'
    }
    return render(request, 'allocator/rooms.html', context)


def room(request, room_id):
    cur_room = Room.objects.get(id=room_id)

    context = {
        'title' : cur_room.room_name,
        'room' : cur_room,
    }
    return render(request, 'allocator/room.html', context)


def allocations(request):
    rooms = Room.objects.all()
    context = {
        'allocations' :rooms,
        'title' : 'Lecture allocations'
    }
    return render(request, 'allocator/allocations.html', context)


def timetable(request):
    cur_timetable = Time_Table.objects.all().last()
    days = Time_Table_Day.objects.filter(timetable=cur_timetable)

    durations= Timetable_Lecture_Timing.objects.filter(timetable=cur_timetable)

    timings = []
    monday_lectures_8_9 = []
    
    for dur in durations:
        timings.append(f'{dur.start_time} - {dur.end_time}')


    # for day in days:
    #     if day.day == 'Monday':
    #         for lecture in day.lectures.all():
    #             if lecture.start_time == '8:00am' and lecture.end_time == '9:00am':
    #                 monday_lectures_8_9.append(lecture)
    #     else:
    #         pass

    context = {
        'timetable' : cur_timetable,
        'durations' : durations,
        'monday_lectures' : monday_lectures_8_9,
        'title' : f'Lecture timetable for {cur_timetable.semester_name}'
    }
    return render(request, 'allocator/timetable.html', context)



def allocate_rooms(active_lectures, rooms):
    assigned_rooms = []
    # Sort rooms by capacity in descending order
    rooms.sort(key=lambda x: x.room_capacity, reverse=True)

    for lect in active_lectures:
        # Filter rooms based on specification
        if lect.course.course.uses_computer_lab:
            available_rooms = [room for room in rooms if room.room_specification == "Computer Lab"]
        else:
            available_rooms = rooms

        if not available_rooms:
            if lect.course.course.course_type == "Arts Course":
                available_rooms = [room for room in rooms if room.room_specification != "Science Lab"]
            else:
                available_rooms = [room for room in rooms if room.room_specification == "Science Lab"]

        available_rooms.sort(key=lambda x: x.room_capacity, reverse=True) #sort by capacity
        # Allocate the rooms
        room_assigned = False
        for room in available_rooms:
            if room.room_capacity >= lect.course.no_of_students and room not in assigned_rooms:
                print(f"Assigning room {room.room_name} to {lect.course.course.course_name}\'s Lecture")
                assigned_rooms.append(room)
                room_assigned = True
                room.allocated_to = F'Lecture for {lect.course.course} ({lect.study_topic}) by {lect.lecturer}'
                room.state = 'In Use'
                room.save(update_fields=['allocated_to', 'state'])

                new_report = Report()
                new_report.room = room
                new_report.allocated_to = F'Lecture for {lect.course.course} ({lect.study_topic}) by {lect.lecturer}'
                new_report.from_time = lect.duration.start_time
                new_report.to_time = lect.duration.end_time
                new_report.save()
                break
            else:
                new_report = Report()
                new_report.room = room
                new_report.allocated_to = 'None'
                new_report.from_time = lect.duration.start_time
                new_report.to_time = lect.duration.end_time
                new_report.save()

        if not room_assigned:
            print(f"No suitable room found for {lect.course.course.course_name}\'s lecture")
        else:
            continue
    # check for any free rooms
    remaining_rooms = [room for room in rooms if room not in assigned_rooms]
    if remaining_rooms:
        for room in remaining_rooms:
            room.allocated_to = 'None'
            room.state = 'Free'
            room.save(update_fields=['allocated_to', 'state'])

    return remaining_rooms


def today_report(request, room_id):
    cur_room = Room.objects.get(id=room_id)
    all_reports = Report.objects.filter(room=cur_room)
    reports = []
    for report in all_reports:
        if report.date_generated.date() == datetime.now().date():
            reports.append(report)

    context = {
        'title' : f'Today Report for {cur_room.room_name}',
        'reports' : reports
    }
    return render(request, 'allocator/report.html', context)


def yesterday_report(request, room_id):
    cur_room = Room.objects.get(id=room_id)
    all_reports = Report.objects.filter(room=cur_room)
    yesterday_date = datetime.now().date() - timedelta(days=1)
    print(yesterday_date)


    reports = []
    for report in all_reports:
        if report.date_generated.date() == yesterday_date:
            reports.append(report)

    context = {
        'title' : f'Yesterday Report for {cur_room.room_name}',
        'reports' : reports
    }
    return render(request, 'allocator/report.html', context)


def week_report(request, room_id):
    cur_room = Room.objects.get(id=room_id)
    all_reports = Report.objects.filter(room=cur_room)
    last_week_start = datetime.now().date() - timedelta(days=7)
    print(last_week_start)


    reports = []
    for report in all_reports:
        if report.date_generated.date() >= last_week_start:
            reports.append(report)

    context = {
        'title' : f'This week\'s Report for {cur_room.room_name}',
        'reports' : reports
    }
    return render(request, 'allocator/report.html', context)


def month_report(request, room_id):
    cur_room = Room.objects.get(id=room_id)
    all_reports = Report.objects.filter(room=cur_room)
    last_month_start = datetime.now().date() - timedelta(days=30)
    print(last_month_start)


    reports = []
    for report in all_reports:
        if report.date_generated.date() >= last_month_start:
            reports.append(report)

    context = {
        'title' : f'This month\'s Report for {cur_room.room_name}',
        'reports' : reports
    }
    return render(request, 'allocator/report.html', context)

def year_report(request, room_id):
    cur_room = Room.objects.get(id=room_id)
    all_reports = Report.objects.filter(room=cur_room)
    last_year_start = datetime.now().date() - timedelta(days=365)
    print(last_year_start)


    reports = []
    for report in all_reports:
        if report.date_generated.date() >= last_year_start:
            reports.append(report)

    context = {
        'title' : f'This year\'s Report for {cur_room.room_name}',
        'reports' : reports
    }
    return render(request, 'allocator/report.html', context)