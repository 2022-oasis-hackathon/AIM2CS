# Generated by Django 4.0.6 on 2022-07-20 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('userpasswd', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='honam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
                ('uploadedFile', models.FileField(upload_to='')),
                ('dir_name', models.CharField(max_length=200)),
                ('season', models.CharField(max_length=10, null=True)),
                ('weather', models.CharField(max_length=20, null=True)),
                ('nature', models.CharField(max_length=20, null=True)),
                ('place', models.CharField(max_length=20, null=True)),
                ('big_area', models.CharField(max_length=20, null=True)),
                ('small_area', models.CharField(max_length=20, null=True)),
                ('detail_area', models.TextField()),
                ('explanation', models.TextField()),
                ('likenum', models.IntegerField(default=0)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Aim2cs_app.users')),
            ],
        ),
    ]
