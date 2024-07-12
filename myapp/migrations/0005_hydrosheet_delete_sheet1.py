# Generated by Django 5.0.7 on 2024-07-11 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_rename_hydroproject_sheet1'),
    ]

    operations = [
        migrations.CreateModel(
            name='hydrosheet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('capacity', models.FloatField()),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Sheet1',
        ),
    ]