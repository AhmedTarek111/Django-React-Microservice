from django.db import models
from django.utils import timezone

class Post(models.Model):
    author = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=5000)
    puplish_date = models.DateTimeField(default=timezone.now )
    
    def total_likes(self):
        total_likes = Postlikes.objects.filter(post = self).count()
        return total_likes
    
    def total_comments(self):
        total_comments = Comments.objects.filter(post = self).count()
        return total_comments
    def __str__(self):
        return self.title
    
class Postlikes(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    user_id = models.IntegerField()
    
    def __str__(self):
        return self.post
    
class Comments(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    content = models.TextField(max_length=2000)
    user_id = models.IntegerField()
    puplish_date = models.DateTimeField(default=timezone.now )
    
    def __str__(self):
        return self.post
    