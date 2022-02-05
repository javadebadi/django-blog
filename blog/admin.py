from django.contrib import admin
from blog.models import (
    Post,
    ContactMessage,
    )

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publish_date')
    list_filter = ('author', 'publish_date')

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'insert_time')
    list_filter = ('email',)