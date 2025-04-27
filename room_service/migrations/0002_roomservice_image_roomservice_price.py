

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomservice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='room_service_images/'),
        ),
        migrations.AddField(
            model_name='roomservice',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room_service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomservice',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='room_service_images/'),
        ),
        migrations.AddField(
            model_name='roomservice',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]

