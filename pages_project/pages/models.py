from django.db import models


class Post(models.Model):
    text = models.TextField()

    def str(self):
        return self.text