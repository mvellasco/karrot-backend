# Generated by Django 2.2.6 on 2019-10-15 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0016_activity_feedback_as_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='feedback_as_sum',
            field=models.BooleanField(default=True),
        ),
    ]
