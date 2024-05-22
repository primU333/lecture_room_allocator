from django.db import models


# Create your models here.
class Room(models.Model):
    states = (
        ('In Use', 'In Use'),
        ('Free', 'Free'),
        ('Closed', 'Closed'),
    )

    specifications = (
        ('Computer Lab', 'Computer Lab'),
        ('Science Lab', 'Science Lab'),
        ('Library', 'Library'),
        ('Lecture Room', 'Lecture Room'),
        ('Comfrence Hall', 'Comfrence Hall'),
    )

    room_name = models.CharField(max_length=200)
    room_specification = models.CharField(max_length=100, choices=specifications)
    room_size_in_metres = models.FloatField()
    room_capacity = models.IntegerField(null=True)
    room_description = models.TextField()
    room_image = models.ImageField(upload_to='rooms')
    state = models.CharField(max_length=100, choices=states, default='Free')
    allocated_to = models.CharField(max_length=200, default='None')

    def __str__(self):
        return self.room_name



class Course(models.Model):
    types = (
        ('Science Course', 'Science Course'),
        ('Arts Course', 'Arts Course'),
    )
    uses_computer_lab = models.BooleanField(default=False)
    uses_science_lab = models.BooleanField(default=False)
    course_name = models.CharField(max_length=200)
    course_type = models.CharField(max_length=200, null=True, choices=types)

    def __str__(self):
        return self.course_name
    
class Year_Course(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    year = models.CharField(max_length=100)
    no_of_students = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.course.course_name} Year: {self.year}"


class Report(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='reports')
    allocated_to = models.TextField(null=True)
    from_time = models.CharField(max_length=100, null=True)
    to_time = models.CharField(max_length=100, null=True)
    date_generated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room.room_name
    


class Time_Table(models.Model):
    semester_name = models.CharField(max_length=100, default="Sem One")

    def __str__(self) -> str:
        return self.semester_name


class Time_Table_Day(models.Model):
    days = (
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),

    )
    timetable = models.ForeignKey(Time_Table, on_delete=models.CASCADE, related_name='days')
    day = models.CharField(max_length=100, choices=days)

    def __str__(self) -> str:
        return self.day


class Timetable_Lecture_Timing(models.Model):
    times = (
        ('8:00am', '8:00am'),
        ('9:00am', '9:00am'),
        ('10:00am', '10:00am'),
        ('11:00am', '11:00am'),
        ('12:00pm', '12:00pm'),
        ('1:00pm', '1:00pm'),
        ('2:00pm', '2:00pm'),
        ('3:00pm', '3:00pm'),
        ('4:00pm', '4:00pm'),
        ('5:00pm', '5:00pm'),
        ('6:00pm', '6:00pm'),
    )
    timetable = models.ForeignKey(Time_Table, on_delete=models.CASCADE, related_name="timings")
    start_time = models.CharField(max_length=100, choices=times)
    end_time = models.CharField(max_length=100, choices=times)

    def __str__(self) -> str:
        return f'{self.timetable.semester_name} Lecture starting at:{self.start_time} Ending at: {self.end_time}'



class Lecture(models.Model):
    day = models.ForeignKey(Time_Table_Day, on_delete=models.CASCADE, related_name="lectures")
    course = models.ForeignKey(Year_Course, on_delete=models.CASCADE, related_name='timetables')
    lecturer = models.CharField(max_length=100, null=True)
    study_topic = models.CharField(max_length=300, null=True)
    duration = models.ForeignKey(Timetable_Lecture_Timing, on_delete=models.CASCADE, related_name="lectures", null=True)
    
    
    def __str__(self) -> str:
        return self.course.course.course_name


