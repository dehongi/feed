from django.db import models
from django.conf import settings
from django.urls import reverse

User = settings.AUTH_USER_MODEL

# Create your models here.


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.user}: {self.text}"

    def get_absolute_url(self):
        return reverse("feed:post_detail", kwargs={"pk": self.pk})
