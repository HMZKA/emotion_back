# Generated by Django 4.2 on 2024-02-05 23:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("company", "0001_initial"),
        ("job", "0002_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="company_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="jobs",
                to="company.company",
            ),
        ),
    ]