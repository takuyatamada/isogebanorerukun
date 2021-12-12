# Generated by Django 3.2.9 on 2021-12-12 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('route_name', models.CharField(max_length=50)),
                ('departure_name', models.CharField(max_length=50)),
                ('destination_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Timetable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure_time', models.DateTimeField()),
                ('is_holiday', models.IntegerField(default=0)),
                ('train_type', models.CharField(blank=True, max_length=10)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='norikae.route')),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='norikae.user'),
        ),
    ]