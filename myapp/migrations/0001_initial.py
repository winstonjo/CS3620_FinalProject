# Generated by Django 2.2 on 2024-04-19 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('ingredients', models.TextField()),
                ('instructions', models.TextField()),
                ('prep_time', models.IntegerField(default=0)),
                ('cook_time', models.IntegerField(default=0)),
            ],
        ),
    ]
