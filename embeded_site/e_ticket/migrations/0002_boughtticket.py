# Generated by Django 3.2.4 on 2021-06-06 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_ticket', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BoughtTicket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=100)),
                ('ticket_id', models.IntegerField()),
            ],
        ),
    ]
