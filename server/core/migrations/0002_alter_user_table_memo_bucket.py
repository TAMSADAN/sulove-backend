# Generated by Django 4.0.2 on 2022-02-23 14:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
        migrations.CreateModel(
            name='Memo',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('context', models.CharField(max_length=255)),
                ('posted_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
            options={
                'db_table': 'memo',
            },
        ),
        migrations.CreateModel(
            name='Bucket',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=255)),
                ('context', models.CharField(max_length=255)),
                ('score', models.CharField(max_length=10)),
                ('type', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=10)),
                ('posted_date', models.DateTimeField()),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
            options={
                'db_table': 'bucket',
            },
        ),
    ]
