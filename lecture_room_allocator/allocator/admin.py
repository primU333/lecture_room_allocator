from django.contrib import admin
from .models import *


class Room_Admin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Room, Room_Admin)

class Course_Admin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Course, Course_Admin)

class Year_Course_Admin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Year_Course, Year_Course_Admin)

class Report_Admin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Report, Report_Admin)

class TimeTableAdmin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Time_Table, TimeTableAdmin)

class Lecture_Admin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Lecture, Lecture_Admin)

class Time_Table_Day_Admin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Time_Table_Day, Time_Table_Day_Admin)

class Time_Table_Duratin_Admin(admin.ModelAdmin):
    search_fields = ['id']
admin.site.register(Timetable_Lecture_Timing, Time_Table_Duratin_Admin)