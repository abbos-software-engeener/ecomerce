from django.db import models

from config.helpers import UploadTo


class Post_Comment(models.Model):
    parent = models.ForeignKey('main.Post_Comment', null=True, default=None, on_delete=models.CASCADE)
    post = models.ForeignKey('api.Product', null=True, default=None, on_delete=models.CASCADE)
    user = models.ForeignKey('user.User', default=None, on_delete=models.CASCADE)
    comment = models.TextField(verbose_name="izoh")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Contact(models.Model):
    first_name = models.CharField(max_length=100, default='ismingizni kiriting')
    last_name = models.CharField(max_length=100, default='familiyangizni kiriting kiriting')
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        fullname = f"{self.first_name}  {self.last_name}"
        return fullname

