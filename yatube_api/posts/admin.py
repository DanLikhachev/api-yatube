from django.contrib import admin

from .models import Comment, Group, Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("pk", "text", "pub_date", "author")
    search_fields = (
        "text",
        "author__username",
    )
    list_filter = (
        "pub_date",
        "author__username",
    )
    empty_value_display = "-пусто-"


@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = (
        "pk",
        "title",
        "slug",
        "description",
    )
    search_fields = (
        "title",
        "slug",
        "description",
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("pk", "post", "author", "text", "created")
    search_fields = ("post", "author", "text", "created")
    list_filter = ("created", "author")
    empty_value_display = "-пусто-"
