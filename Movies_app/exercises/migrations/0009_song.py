# Generated by Django 2.0.5 on 2018-05-27 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0008_album_band'),
    ]

    operations = [
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('duration', models.TimeField(null=True)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exercises.Album')),
            ],
        ),
    ]
