# Generated by Django 5.2 on 2025-04-29 07:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
        ('dresses', '0001_initial'),
        ('shipping', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shipment',
            old_name='Expected_delivery_date',
            new_name='expected_delivery_date',
        ),
        migrations.AddField(
            model_name='shipment',
            name='adress',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='customer.adress'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='shipment',
            name='status',
            field=models.CharField(choices=[('Shipment Created', 'Shipment Created'), ('Picked Up from Sender', 'Picked Up from Sender'), ('In Transit', 'In Transit'), ('Out for Delivery', 'Out for Delivery'), ('Delivered', 'Delivered'), ('Delivery Failed', 'Delivery Failed'), ('On Hold', 'On Hold'), ('Returned to Sender', 'Returned to Sender'), ('Shipment Canceled', 'Shipment Canceled')], max_length=100),
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('refID', models.IntegerField()),
                ('card_number', models.IntegerField()),
                ('card_holder_name', models.CharField(max_length=100)),
                ('expiry_date', models.DateField()),
                ('cvv', models.IntegerField()),
                ('status', models.CharField(choices=[('Paid', 'Paid'), ('Processing', 'Processing'), ('Refunded', 'Refunded')], max_length=100)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dresses.rental')),
            ],
        ),
    ]
