from django.db import models
from django.contrib.auth.models import User

class Athletes(models.Model):
    code = models.IntegerField(primary_key=True)
    current = models.BooleanField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    name_short = models.CharField(max_length=50, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    function = models.CharField(max_length=50, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    country_long = models.CharField(max_length=50, blank=True, null=True)
    nationality_long = models.CharField(max_length=50, blank=True, null=True)
    nationality_code = models.CharField(max_length=3, blank=True, null=True)
    disciplines = models.TextField(blank=True, null=True)
    events = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    birth_country = models.CharField(max_length=50, blank=True, null=True)
    residence_place = models.CharField(max_length=50, blank=True, null=True)
    residence_country = models.CharField(max_length=50, blank=True, null=True)
    hobbies = models.TextField(blank=True, null=True)
    occupation = models.CharField(max_length=50, blank=True, null=True)
    education = models.TextField(blank=True, null=True)
    lang = models.CharField(max_length=100, blank=True, null=True)
    coach = models.TextField(blank=True, null=True)
    reason = models.TextField(blank=True, null=True)
    influence = models.TextField(blank=True, null=True)
    philosophy = models.TextField(blank=True, null=True)
    event_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'athletes'


class Events(models.Model):
    event_id = models.IntegerField(primary_key=True)
    event = models.CharField(max_length=100, blank=True, null=True)
    tag = models.CharField(max_length=50, blank=True, null=True)
    sport = models.CharField(max_length=50, blank=True, null=True)
    sport_code = models.CharField(max_length=3, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'



class Medals(models.Model):
    medal_id = models.AutoField(primary_key=True)
    medal_type = models.CharField(max_length=20, blank=True, null=True)
    medal_code = models.IntegerField(blank=True, null=True)
    medal_date = models.DateField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    discipline = models.CharField(max_length=50, blank=True, null=True)
    event = models.CharField(max_length=100, blank=True, null=True)
    event_type = models.CharField(max_length=10, blank=True, null=True)
    code = models.CharField(max_length=30, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    country_long = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medals'


class Schedules(models.Model):
    schedule_id = models.CharField(primary_key=True)
    start_date = models.DateTimeField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    day = models.DateField(blank=True, null=True)
    status = models.CharField(max_length=20, blank=True, null=True)
    discipline = models.CharField(max_length=50, blank=True, null=True)
    discipline_code = models.CharField(max_length=3, blank=True, null=True)
    event = models.CharField(max_length=50, blank=True, null=True)
    event_medal = models.IntegerField(blank=True, null=True)
    phase = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=1, blank=True, null=True)
    event_type = models.CharField(max_length=20, blank=True, null=True)
    venue = models.CharField(max_length=100, blank=True, null=True)
    venue_code = models.CharField(max_length=3, blank=True, null=True)
    location_description = models.CharField(max_length=255, blank=True, null=True)
    location_code = models.CharField(max_length=3, blank=True, null=True)
    event_id = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schedules'


class Teams(models.Model):
    code = models.CharField(max_length=20, blank=True, null=True)
    current = models.BooleanField(blank=True, null=True)
    team = models.CharField(max_length=100, blank=True, null=True)
    country_code = models.CharField(max_length=3, blank=True, null=True)
    country_long = models.CharField(max_length=100, blank=True, null=True)
    discipline = models.CharField(max_length=50, blank=True, null=True)
    disciplines_code = models.CharField(max_length=3, blank=True, null=True)
    events = models.CharField(max_length=50, blank=True, null=True)
    athletes = models.TextField(blank=True, null=True)
    athletes_codes = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'teams'
    