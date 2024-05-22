# Generated by Django 4.2.11 on 2024-05-02 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0006_room_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='uses_computer_lab',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='course',
            name='uses_science_lab',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='room',
            name='allocated_to',
            field=models.CharField(default='None', max_length=200),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_specification',
            field=models.CharField(choices=[('Computer Lab', 'Computer Lab'), ('Science Lab', 'Science Lab'), ('Library', 'Library'), ('Lecture Room', 'Lecture Room'), ('Comfrence Hall', 'Comfrence Hall')], max_length=100),
        ),
    ]