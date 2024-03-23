from django.db import models
from django.contrib.auth.models import User

from djrichtextfield.models import RichTextField
from django_resized import ResizedImageField


ANIMALS = (
    ("Dog", "Dog"),
    ("Cat", "Cat"),
    ("Lion", "Lion"),
    ("Platypus", "Platypus")
)

GENDER = (
    ("Male", "Male"),
    ("Female", "Female")
)

class Adoption(models.Model):
    """
    Class for the adoption model schema
    """
    user = models.ForeignKey(
        User,
        related_name="adoption_admin",
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=50, null=False, blank=False)
    animal_type = models.CharField(max_length=10, choices=ANIMALS)
    age = models.IntegerField()
    color = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=GENDER)
    image = ResizedImageField(
        size=[400, None],
        quality=75,
        upload_to="animals/",
        force_format="WEBP",
        blank=False,
        null=False
    )
    description = RichTextField(max_length=10000, null=False, blank=False)
