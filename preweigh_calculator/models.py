from django.db import models


class Configs(models.Model):
    variable = models.CharField(max_length=32)
    int_val = models.IntegerField(null=True, blank=True)
    float_val = models.FloatField(null=True, blank=True)
    str_val = models.CharField(blank=True, max_length=255)
    bool_val = models.NullBooleanField()

    class Meta:
        verbose_name_plural = "configs"

    def __str__(self):
        return self.variable


class Work(models.Model):
    task = models.CharField(max_length=127)
    minutes = models.FloatField()
    people = models.IntegerField()

    class Meta:
        verbose_name_plural = "Work"

    def __str__(self):
        return self.task


class Composition(models.Model):
    composition = models.CharField(max_length=10)
    major_components = models.IntegerField()
    minor_components = models.IntegerField()

    def __str__(self):
        return self.composition
