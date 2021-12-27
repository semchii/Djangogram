from django.db import models
from django.utils import timezone


class User(models.Model):
    user_id = models.CharField(max_length=100, unique=True, primary_key=True)
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=100)
    avatar = models.ImageField(blank=True)
    followers = models.ManyToManyField('self', related_name='follower', blank=True)
    following = models.ManyToManyField('self', related_name='following', blank=True)


class Post(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    images = models.ImageField()
    pub_date = models.DateTimeField(
        default=timezone.now)

    total_likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(User)


class Message(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    pub_date = models.DateTimeField(default=timezone.now)
    is_readed = models.BooleanField(default=False)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)

    total_likes = models.IntegerField(default=0)
    likes = models.ManyToManyField(User, on_delete=models.CASCADE)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)


class Images(models.Model):
    products = models.ForeignKey(Post, related_name='img', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='post/img/%Y/%m/%d')
