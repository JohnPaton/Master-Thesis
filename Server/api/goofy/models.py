from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False, unique=True)
    password = models.CharField(max_length=1000, null=False, blank=False)
    salt = models.CharField(max_length=1000, null=False, blank=False)
    gender = models.CharField(max_length=5, null=False, blank=False)
    nationality = models.CharField(max_length=50, null=False, blank=False)
    occupation = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.username


class UserHistory(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    sentence = models.CharField(max_length=100, null=False, blank=False)
    chart_id = models.CharField(max_length=50, null=False, blank=False)
    date = models.DateField()
    vowels = models.BinaryField(null=False, blank=False)

    def __str__(self):
        return self.sentence


class UserSentenceVowelsTrend(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    sentence = models.CharField(max_length=100, null=False, blank=False)
    vowel = models.CharField(max_length=5, null=False, blank=False)
    trend_values = models.TextField(null=False, blank=False)
    trend = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return self.sentence


class UserReport(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    report_values = models.TextField(null=False, blank=False)

    def __str__(self):
        return self.username
