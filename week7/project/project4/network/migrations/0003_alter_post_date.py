# Generated by Django 4.1.3 on 2022-12-24 02:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("network", "0002_post_comment_user_likes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="date",
            field=models.DateTimeField(
                default=datetime.datetime(2022, 12, 24, 2, 52, 34, 563448)
            ),
        ),
    ]
