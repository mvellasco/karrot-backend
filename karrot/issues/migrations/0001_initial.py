# Generated by Django 2.1.5 on 2019-01-21 12:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import karrot.conversations.models
import karrot.issues.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('groups', '0036_group_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.TextField(choices=[('ongoing', 'ongoing'), ('decided', 'decided'), ('cancelled', 'cancelled')], default='ongoing')),
                ('type', models.TextField(choices=[('conflict_resolution', 'conflict_resolution')], default='conflict_resolution')),
                ('topic', models.TextField()),
                ('affected_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='affected_by_issue', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues_created', to=settings.AUTH_USER_MODEL)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='issues', to='groups.Group')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, karrot.conversations.models.ConversationMixin),
        ),
        migrations.CreateModel(
            name='IssueParticipant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='issues.Issue')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('type', models.TextField(choices=[('further_discussion', 'further_discussion'), ('no_change', 'no_change'), ('remove_user', 'remove_user')])),
                ('message', models.TextField(null=True)),
                ('sum_score', models.FloatField(null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('score', models.IntegerField()),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes', to='issues.Option')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votes_given', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Voting',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('expires_at', models.DateTimeField(default=karrot.issues.models.voting_expiration_time)),
                ('accepted_option', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='accepted_for_voting', to='issues.Option')),
                ('issue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='votings', to='issues.Issue')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='option',
            name='voting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='options', to='issues.Voting'),
        ),
        migrations.AddField(
            model_name='issue',
            name='participants',
            field=models.ManyToManyField(related_name='issues', through='issues.IssueParticipant', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='issueparticipant',
            unique_together={('issue', 'user')},
        ),
    ]
