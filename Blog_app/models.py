import cloudinary.models
from django.db import models
from django.contrib.auth.models import User
import cloudinary


# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # photo = models.ImageField(upload_to="blog_images", blank=True, null=True)
    photo = cloudinary.models.CloudinaryField("image", blank=True, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author} created {self.title}"


# class Comments(models.Model):
#     name = User
#     post_name = models.ForeignKey(Posts, on_delete=models.CASCADE)
#     comment_body = models.TextField()
#     date_added = models.DateTimeField(auto_now=True)


# def __str__(self):
#     return f"{self.post_name} created {self.comment_body}"
class Comments(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, null=True)  # Fix this
    post_name = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment_body = models.TextField()
    date_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post_name}"
