# Generated by Django 2.2.12 on 2020-08-31 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0002_auto_20200831_1521'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=None)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=300)),
            ],
        ),
        migrations.DeleteModel(
            name='New',
        ),
    ]