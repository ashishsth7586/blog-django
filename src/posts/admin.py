from django.contrib import admin
from .models import Author, Category, Post, Comment, PostView
from import_export.admin import ImportExportModelAdmin
# Register your models here.
admin.site.register(Author)
admin.site.register(Category)
# admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(PostView)

@admin.register(Post)
class PostAdmin(ImportExportModelAdmin):
    pass