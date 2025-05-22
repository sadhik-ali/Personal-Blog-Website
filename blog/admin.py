from django.contrib import admin
from .models import Post, Category, Tag, Comment

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'slug']

class CommentInline(admin.TabularInline):
    model = Comment
    extra = 1
    readonly_fields = ['name', 'email', 'body', 'created_at']
    can_delete = True

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ['title', 'author', 'category', 'created_at', 'is_published']
    list_filter = ['is_published', 'category', 'created_at']
    search_fields = ['title', 'content']
    inlines = [CommentInline]

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'post', 'created_at', 'approved']
    list_filter = ['approved', 'created_at']
    search_fields = ['name', 'email', 'body']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
