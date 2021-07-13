# Generated by Django 3.2.4 on 2021-07-13 11:45

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountGuest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone_number', models.CharField(blank=True, max_length=20)),
                ('kakao_number', models.CharField(blank=True, max_length=50)),
                ('google_number', models.EmailField(blank=True, max_length=50)),
                ('google_mail', models.EmailField(blank=True, max_length=128)),
                ('naver_id', models.CharField(blank=True, max_length=50)),
                ('gender', models.CharField(blank=True, max_length=2)),
                ('birthday', models.DateField(null=True)),
                ('is_subscribe', models.BooleanField(default=False, null=True)),
                ('subscribe_time', models.DateTimeField(null=True)),
                ('written_review_count', models.PositiveIntegerField(default=0)),
                ('review_like_count', models.PositiveIntegerField(default=0)),
                ('fun_data_count', models.PositiveIntegerField(default=0)),
                ('agreed_marketing_receive', models.BooleanField(default=False)),
                ('shopkeeper_tel', models.CharField(blank=True, max_length=20)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='AccountJob',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='ClickData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clicked_time', models.TimeField(auto_now_add=True)),
                ('stayed_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='FunData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_name', models.CharField(blank=True, max_length=20)),
                ('score', models.SmallIntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LivingArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('living_area', models.TextField()),
                ('people_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='MyLikeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='MyLikeListShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Preference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference_name', models.CharField(blank=True, max_length=20)),
                ('score', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SearchedLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_word', models.CharField(blank=True, max_length=20)),
                ('searched_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SearchedMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_word', models.CharField(blank=True, max_length=20)),
                ('searched_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='SearchedStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_word', models.CharField(blank=True, max_length=20)),
                ('searched_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='VisitedShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('visited_time', models.DateTimeField(auto_now_add=True)),
                ('account_guest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
