from tabnanny import verbose
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

    image = models.ImageField(
        '/blog/images/',
        null=True,
        blank=True,
        )

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
        ordering = (
            '-publish_date',  # Descending -> New publish posts first
            '-id',
        )


# create model for contact message
class ContactMessage(models.Model):

    phone_number = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        )
    
    email = models.EmailField()

    name = models.CharField(max_length=128)

    message = models.CharField(max_length=1500)

    insert_time = models.DateTimeField(
        auto_now_add=True,
        )


    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'contact_message'
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
        ordering = (
            '-insert_time',
        )