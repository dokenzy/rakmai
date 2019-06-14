# Generated by Django 2.2.2 on 2019-06-14 13:01

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20190607_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailBanned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, verbose_name='email address')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PhoneBanned',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_removed', models.BooleanField(default=False)),
                ('phone', models.CharField(blank=True, max_length=16, null=True, verbose_name='phone number')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
