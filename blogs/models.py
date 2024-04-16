from django.db import models
from django.contrib.auth import get_user_model
import uuid
from django.utils import timezone

# Create your models here.

User = get_user_model()

class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True,default=uuid.uuid4)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.TextField(blank=True)
    like_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return self.user.username

class Like(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.user.username
