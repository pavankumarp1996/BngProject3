# Generated by Django 3.2.1 on 2021-05-05 05:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one_to_many_Relation', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='Student1',
            new_name='Student',
        ),
    ]
