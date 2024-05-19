from django.contrib.auth.models import AbstractUser
from django.db import models

class Profile(AbstractUser):
    phone_number = models.CharField(max_length=10)

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='profile_set',  # Changed related name
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='profile_set',  # Changed related name
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

    def __str__(self):
        return self.username

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

class Own(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} owns this {self.item.name} item"
