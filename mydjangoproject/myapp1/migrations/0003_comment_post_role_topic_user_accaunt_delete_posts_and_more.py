# Generated by Django 5.0.4 on 2024-04-17 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0002_posts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('post_id', models.IntegerField()),
                ('user_id', models.IntegerField()),
                ('content', models.CharField(max_length=250)),
                ('publish_datetime', models.DateTimeField()),
            ],
            options={
                'db_table': 'comment',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('head', models.CharField(max_length=100)),
                ('content', models.CharField(max_length=10000)),
                ('publish_datetime', models.DateTimeField()),
                ('topic_id', models.IntegerField()),
                ('image', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'post',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'db_table': 'role',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'topic',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User_Accaunt',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=25)),
                ('login', models.CharField(max_length=25)),
                ('password', models.CharField(max_length=30)),
                ('role_id', models.IntegerField()),
            ],
            options={
                'db_table': 'user_account',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='Posts',
        ),
        migrations.DeleteModel(
            name='Worker',
        ),
    ]
