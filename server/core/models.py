from django.db import models


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    nick_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'user'


class Memo(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    posted_date = models.DateTimeField()

    class Meta:
        db_table = 'memo'


class Bucket(models.Model):
    id = models.BigAutoField(primary_key=True)
    user_id = models.ForeignKey('user', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    score = models.CharField(max_length=10)
    type = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    posted_date = models.DateTimeField()

    class Meta:
        db_table = 'bucket'
