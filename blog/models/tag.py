from django.db import models

# create tag model
class Tag(models.Model):

    name = models.CharField(max_length=32)

    def __str__(self) -> str:
        return self.name

    class Meta:
        db_table = 'tag'
        ordering = (
            'name',
        )
