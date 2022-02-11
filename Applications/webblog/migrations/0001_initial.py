# Generated by Django 4.0.2 on 2022-02-11 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='WebblogFormModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('post_date', models.DateField()),
            ],
            options={
                'verbose_name': 'WebblogFormModel',
                'verbose_name_plural': 'WebblogFormModels',
            },
        ),
    ]