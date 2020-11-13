from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=600)
    category = models.CharField(max_length=700)
    slug = models.CharField(max_length=900)
    image = models.FileField(blank=True, null=True, upload_to='post_images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    dt = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title+ ' by ' + self.author.username

class BlogComments(models.Model):
    sno = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.comment[0:15] + '... ' + self.user.username    