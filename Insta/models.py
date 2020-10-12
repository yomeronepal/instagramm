from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=500,null=True)
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,default=1, on_delete=models.CASCADE)

    post_image = models.ImageField(upload_to='posts_images',null=True)


    def __str__(self):
        return self.text

    def get_total_like(self):
        return self.likes_set.all().count()





class Likes(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete =models.CASCADE)
    image = models.ImageField(default ='default.jpg', upload_to = 'profile_pics',null=True)
    name = models.CharField(max_length=200,null=True)


    def __str__(self):
        return f'{self.user.username} Profile'

