from django.contrib import admin

# Register your models here.
from blog.models import Tag, Post
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ("published_at", "slug")

admin.site.register(Post, PostAdmin)