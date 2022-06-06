# Generated by Django 4.0.4 on 2022-06-05 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_stat'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('price', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.category')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.player')),
            ],
        ),
        migrations.RenameModel(
            old_name='Stat',
            new_name='ItemStat',
        ),
        migrations.CreateModel(
            name='PlayerItemStat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('value', models.IntegerField()),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.playeritem')),
            ],
        ),
    ]
