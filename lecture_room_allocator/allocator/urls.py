from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'allocator'

urlpatterns = [
    path('', views.home, name='home'),
    path('rooms', views.rooms, name='rooms'),
    path('allocations', views.allocations, name='allocations'),
    path('timetable', views.timetable, name='timetable'),
    path('room/<int:room_id>', views.room, name='room_details'),
    path('today-report-?/<int:room_id>', views.today_report, name='today_report'),
    path('yesterday-report-?/<int:room_id>', views.yesterday_report, name='yesterday_report'),
    path('this-week-report-?/<int:room_id>', views.week_report, name='week_report'),
    path('this-month-report-?/<int:room_id>', views.month_report, name='month_report'),
    path('this-year-report-?/<int:room_id>', views.year_report, name='year_report'),

]