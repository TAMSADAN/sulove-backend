# Generated by Django 4.0.2 on 2022-02-23 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nick_name', models.CharField(max_length=30)),
            ],
        ),
    ]