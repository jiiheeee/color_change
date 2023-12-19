from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    mail = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    mixed_color_number = models.IntegerField(default='0')
    is_active = models.BooleanField(default=True, null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now_add=True)