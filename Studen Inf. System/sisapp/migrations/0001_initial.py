# Generated by Django 2.2 on 2019-05-02 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SIS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enqno', models.IntegerField()),
                ('firstName', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('Intrest', models.CharField(max_length=20)),
                ('source', models.CharField(max_length=20)),
                ('phoneNumber', models.IntegerField()),
                ('refrence', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'SIS',
            },
        ),
    ]
