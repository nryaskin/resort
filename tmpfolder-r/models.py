# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Dishes(models.Model):
    dish_name = models.CharField(max_length=50)
    for_breakfast = models.IntegerField()
    for_lunch = models.IntegerField()
    for_dinner = models.IntegerField()
    link_to_picture = models.CharField(max_length=60)
    description = models.TextField(primary_key=True)
    type_of_dish = models.CharField(max_length=60)

    class Meta:
        managed = False
        db_table = 'dishes'


class OrdersForToday(models.Model):
    breakfast_main = models.CharField(max_length=50)
    breakfast_beverage = models.CharField(max_length=50)
    breakfast_desert = models.CharField(max_length=50)
    lunch_first_course = models.CharField(max_length=50)
    lunch_second_course = models.CharField(max_length=50)
    lunch_beverage = models.CharField(max_length=50)
    lunch_desert = models.CharField(max_length=50)
    dinner_snack = models.CharField(max_length=50)
    dinner_main = models.CharField(max_length=50)
    dinner_beverage = models.CharField(max_length=50)
    dinner_desert = models.CharField(max_length=50)
    order_number = models.IntegerField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'orders_for_today'


class Procedures(models.Model):
    procedurename = models.CharField(db_column='procedureName', max_length=50)  # Field name made lowercase.
    time = models.TimeField()
    date = models.DateField()
    doctor = models.CharField(max_length=50)
    cabinet = models.IntegerField()
    vocationnumber = models.IntegerField(db_column='vocationNumber')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'procedures'
        unique_together = (('procedurename', 'time', 'date', 'vocationnumber'),)


class Rooms(models.Model):
    roomnumber = models.IntegerField(db_column='roomNumber')  # Field name made lowercase.
    housenumber = models.IntegerField(db_column='houseNumber')  # Field name made lowercase.
    roomtype = models.CharField(db_column='roomType', max_length=50)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rooms'
        unique_together = (('roomnumber', 'housenumber'),)


class Visitors(models.Model):
    visitorname = models.TextField(db_column='visitorName')  # Field name made lowercase.
    vocationnumber = models.IntegerField(db_column='vocationNumber', primary_key=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'visitors'


class Vocations(models.Model):
    vocationnumber = models.IntegerField(db_column='vocationNumber', primary_key=True)  # Field name made lowercase.
    tablenumber = models.IntegerField(db_column='tableNumber', blank=True, null=True)  # Field name made lowercase.
    roomnumber = models.IntegerField(db_column='roomNumber', blank=True, null=True)  # Field name made lowercase.
    housenumber = models.IntegerField(db_column='houseNumber', blank=True, null=True)  # Field name made lowercase.
    arrivaldate = models.DateField(db_column='arrivalDate', blank=True, null=True)  # Field name made lowercase.
    departuredate = models.DateField(db_column='departureDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'vocations'
