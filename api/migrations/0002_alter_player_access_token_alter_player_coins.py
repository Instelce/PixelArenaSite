# Generated by Django 4.0.4 on 2022-05-18 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='access_token',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='coins',
            field=models.IntegerField(default=100),
        ),
    ]
