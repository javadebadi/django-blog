from django.db import models

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