# Generated by Django 3.0.5 on 2020-05-03 07:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Your Name', max_length=100)),
                ('birthday', models.DateTimeField(help_text='Birth of Date')),
            ],
        ),
    ]