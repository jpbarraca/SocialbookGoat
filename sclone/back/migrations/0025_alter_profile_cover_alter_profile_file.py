# Generated by Django 4.1.5 on 2023-06-26 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("back", "0024_alter_profile_fname_alter_profile_lname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="cover",
            field=models.ImageField(
                default="default/blank.png", upload_to="coverimages"
            ),
        ),
        migrations.AlterField(
            model_name="profile",
            name="file",
            field=models.ImageField(
                default="default/defaultprofile.jpg", upload_to="images"
            ),
        ),
    ]
