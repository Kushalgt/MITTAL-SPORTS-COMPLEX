# Generated by Django 4.1 on 2022-09-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=122)),
                ('password', models.CharField(max_length=122)),
                ('username', models.CharField(max_length=122)),
            ],
        ),
    ]
