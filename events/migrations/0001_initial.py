# Generated by Django 2.2.4 on 2019-08-26 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('comments', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Unregistered_user',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.EmailField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=45)),
                ('content', models.TextField()),
                ('date', models.DateTimeField()),
                ('published', models.IntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Event_subscriptions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Listing')),
                ('unregistered_user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Unregistered_user')),
                ('user_comments', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Comments')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='event_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Listing'),
        ),
        migrations.AddField(
            model_name='comments',
            name='unregistered_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Unregistered_user'),
        ),
    ]
