# Generated by Django 2.0.4 on 2018-04-21 13:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Main_Meme', '0002_comentari'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Meme_vote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Main_Meme.Meme')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
