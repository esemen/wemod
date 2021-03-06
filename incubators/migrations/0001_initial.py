# Generated by Django 4.0.2 on 2022-02-25 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='campaign name')),
                ('slug', models.SlugField(max_length=80, unique=True, verbose_name='slug')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this campaign should be treated as active. Unselect this instead of deleting campaigns.', verbose_name='active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date Updated')),
            ],
            options={
                'verbose_name': 'Campaign',
                'verbose_name_plural': 'Campaigns',
            },
        ),
    ]
