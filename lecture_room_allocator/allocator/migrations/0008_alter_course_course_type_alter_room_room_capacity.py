# Generated by Django 4.2.11 on 2024-05-02 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('allocator', '0007_course_course_type_course_uses_computer_lab_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('Science Course', 'Science Course'), ('Arts Course', 'Arts Course')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='room',
            name='room_capacity',
            field=models.IntegerField(null=True),
        ),
    ]