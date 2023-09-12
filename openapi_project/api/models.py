# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cinemas(models.Model):
    cinema_name = models.TextField()
    address = models.TextField()
    description = models.TextField(blank=True, null=True)
    legal_entity = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    inn = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cinemas'
