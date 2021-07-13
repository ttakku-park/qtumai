# Generated by Django 3.2.4 on 2021-07-13 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountShopkeeper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopkeeper_name', models.CharField(blank=True, max_length=20)),
                ('phone_number', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(blank=True, max_length=30)),
                ('marker_path', models.CharField(blank=True, max_length=200)),
                ('like_count', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_content', models.TextField(blank=True)),
                ('begin_date', models.DateTimeField(null=True)),
                ('expire_date', models.DateTimeField(null=True)),
                ('coupon_count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score_taste', models.PositiveIntegerField(default=0)),
                ('score_service', models.PositiveIntegerField(default=0)),
                ('score_cleanliness', models.PositiveIntegerField(default=0)),
                ('score_vibe', models.PositiveIntegerField(default=0)),
                ('score_price', models.PositiveIntegerField(default=0)),
                ('content', models.TextField(blank=True)),
                ('img_path', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('guest', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='guestReview', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(blank=True, max_length=20)),
                ('shop_address', models.CharField(blank=True, max_length=50)),
                ('shop_description', models.TextField(blank=True)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('like_count', models.PositiveIntegerField(default=0)),
                ('shop_info_url', models.TextField(blank=True)),
                ('score_taste', models.FloatField(default=0)),
                ('score_service', models.FloatField(default=0)),
                ('score_cleanliness', models.FloatField(default=0)),
                ('score_vibe', models.FloatField(default=0)),
                ('score_price', models.FloatField(default=0)),
                ('review_count', models.IntegerField()),
                ('kakao_score', models.FloatField(default=0)),
                ('kakao_score_count', models.IntegerField(default=0)),
                ('kakao_review_count', models.IntegerField(default=0)),
                ('price_range', models.CharField(blank=True, max_length=15)),
                ('latitude', models.FloatField(null=True)),
                ('longitude', models.FloatField(null=True)),
                ('is_subscribe', models.BooleanField(default=False)),
                ('subscribe_time', models.DateField(blank=True, null=True)),
                ('is_new_opend', models.BooleanField(default=False)),
                ('business_reg_img', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ShopArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area_name', models.CharField(blank=True, max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='ThemeKeyword',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('theme_keyword', models.TextField(blank=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
        migrations.CreateModel(
            name='ShopImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.TextField(blank=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
        migrations.AddField(
            model_name='shop',
            name='area',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shoparea'),
        ),
        migrations.AddField(
            model_name='shop',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.category'),
        ),
        migrations.AddField(
            model_name='shop',
            name='coupon',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.coupon'),
        ),
        migrations.AddField(
            model_name='shop',
            name='shopkeeper',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.accountshopkeeper'),
        ),
        migrations.CreateModel(
            name='ReviewImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.TextField(blank=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.review')),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='shop',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop'),
        ),
        migrations.CreateModel(
            name='ReportShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_closed', models.BooleanField(default=False)),
                ('time_different', models.BooleanField(default=False)),
                ('address_different', models.BooleanField(default=False)),
                ('no_coupon', models.BooleanField(default=False)),
                ('others', models.TextField(blank=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reportShop', to='shops.shop')),
            ],
        ),
        migrations.CreateModel(
            name='OpenTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('open_time', models.TextField(blank=True)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu_name', models.CharField(blank=True, max_length=20)),
                ('price', models.PositiveIntegerField(null=True)),
                ('is_representative', models.BooleanField(default=False)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient_name', models.CharField(blank=True, max_length=20)),
                ('menu', models.ManyToManyField(blank=True, related_name='ingredients', to='shops.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='DataLab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age_10s', models.FloatField(default=0)),
                ('age_20s', models.FloatField(default=0)),
                ('age_30s', models.FloatField(default=0)),
                ('age_40s', models.FloatField(default=0)),
                ('age_50s', models.FloatField(default=0)),
                ('age_60s', models.FloatField(default=0)),
                ('male', models.FloatField(default=0)),
                ('female', models.FloatField(default=0)),
                ('shop', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='shops.shop')),
            ],
        ),
    ]
