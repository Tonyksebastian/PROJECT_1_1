# Generated by Django 4.2.4 on 2024-02-20 07:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('make_service', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='service_booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(default='', max_length=250)),
                ('model', models.CharField(default='', max_length=250)),
                ('km_done', models.FloatField()),
                ('date', models.DateTimeField()),
                ('slotnumber', models.IntegerField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='make_service.add_service')),
                ('station', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='make_service.service_station')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]