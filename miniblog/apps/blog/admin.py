from django.contrib import admin

from blog.admin_forms import PostAdminForm, CategoryAdminForm
from blog.models import Post, Category


class PostAdmin(admin.ModelAdmin):
    list_display  = ('title', 'authored_at', 'status')
    list_filter   = ('status', )
    list_editable = ('status', )
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = [
            ("Content", {
                'fields': (
                    'title',
                    'slug',
                    'summary',
                    'body'
                )
            }),
            ("Meta", {
                'fields': ('author',
                    'authored_at',
                    'status',
                    'category',
                    'tags'
                )
            })
        ]

    form = PostAdminForm


class CategoryAdmin(admin.ModelAdmin):
    list_display  = ('name', )
    prepopulated_fields = {'slug': ('name',)}

    form = CategoryAdminForm


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)