# Generated by Django 2.1 on 2018-10-28 04:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('subtitle', models.CharField(blank=True, max_length=128, null=True)),
                ('location', models.CharField(blank=True, max_length=128, null=True)),
                ('slug', models.SlugField(max_length=32, unique=True)),
                ('booking_url', models.URLField(blank=True, help_text='ex. TryBooking URL', null=True)),
                ('open_date', models.DateTimeField(help_text='The date/time which the event will become visible.')),
                ('end_action', models.CharField(choices=[('R', 'Archive'), ('H', 'Hide')], default='R', help_text="The action to take after the final event date has passed. Archived events will display under 'Past Events'. Hidden events will not be shown.", max_length=1)),
            ],
            options={
                'ordering': ('open_date',),
            },
        ),
        migrations.CreateModel(
            name='EventDateTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Event')),
            ],
            options={
                'ordering': ('datetime',),
            },
        ),
        migrations.CreateModel(
            name='EventPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('background', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('mobile', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('tablet', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('desktop', models.ImageField(blank=True, null=True, upload_to='images/%Y/%m/%d/')),
                ('css', models.TextField(blank=True, null=True)),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.Event')),
            ],
        ),
    ]
