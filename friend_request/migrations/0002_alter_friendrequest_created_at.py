# Generated by Django 4.2.3 on 2023-07-13 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friend_request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friendrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
