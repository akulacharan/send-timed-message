# Generated by Django 3.0.6 on 2020-07-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='search',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search', models.CharField(max_length=200)),
                ('created', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'searches',
            },
        ),
    ]
