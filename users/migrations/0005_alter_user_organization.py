# Generated by Django 3.2 on 2021-06-09 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_users_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='organization',
            field=models.IntegerField(choices=[(0, 'NONE'), (1, 'HUMANSCAPE'), (2, 'MOMMYTALK')], default=0),
        ),
    ]