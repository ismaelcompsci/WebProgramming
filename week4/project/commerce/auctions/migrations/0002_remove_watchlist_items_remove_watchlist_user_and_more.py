# Generated by Django 4.1.3 on 2022-12-11 04:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("auctions", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="watchlist",
            name="items",
        ),
        migrations.RemoveField(
            model_name="watchlist",
            name="user",
        ),
        migrations.AddField(
            model_name="watchlist",
            name="item_id",
            field=models.ManyToManyField(
                related_name="auction_item", to="auctions.auction_item"
            ),
        ),
        migrations.AddField(
            model_name="watchlist",
            name="user_id",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]