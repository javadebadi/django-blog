from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):

    title = models.CharField(
        max_length=256,
    )

    subheading = models.CharField(
        max_length=256,
        null=True,
        blank=True,
    )

    text = models.TextField()

    publish_date = models.DateField(
        auto_now=True,
    )

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column='author_id',
        related_name='posts',
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        db_table = 'post'