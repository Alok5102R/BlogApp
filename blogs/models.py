from django.db import models
from django.contrib.auth import get_user_model
import uuid


# Create your models here.

User = get_user_model()

class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.TextField(blank=True)
    like_count = models.IntegerField()

    def __str__(self) -> str:
        return self.user.username