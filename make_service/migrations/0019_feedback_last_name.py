# Generated by Django 4.2.4 on 2024-02-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('make_service', '0018_remove_feedback_comment_date_remove_feedback_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='last_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
