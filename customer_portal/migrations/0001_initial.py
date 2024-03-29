

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('car_dealer_portal', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile', models.CharField(max_length=13, validators=[django.core.validators.MinLengthValidator(10), django.core.validators.MaxLengthValidator(13)])),
                ('area', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.Area')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rent', models.CharField(max_length=8)),
                ('days', models.CharField(max_length=3)),
                ('car_dealer', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.CarDealer')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='car_dealer_portal.Vehicles')),
            ],
        ),
    ]
