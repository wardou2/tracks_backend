# Generated by Django 3.0.8 on 2020-07-08 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.IntegerField()),
                ('longitude', models.IntegerField()),
                ('altitude', models.IntegerField()),
                ('accuracy', models.IntegerField()),
                ('heading', models.IntegerField()),
                ('speed', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.User')),
            ],
        ),
        migrations.CreateModel(
            name='Point',
            fields=[
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('coordinate', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='backend.Coordinate')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.Track')),
            ],
        ),
    ]
