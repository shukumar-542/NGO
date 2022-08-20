# Generated by Django 3.1.3 on 2022-08-20 03:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clientSite', '0004_newsandevents'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsEventImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='newsEvent/')),
                ('news_event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='clientSite.newsandevents')),
            ],
        ),
    ]
