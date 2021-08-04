from django.contrib import admin
from register.models import Register, User_Image, Articles
# Register your models here.


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'user_name',)
    list_filter = ('email', )
    prepopulated_fields = {'slug': ('user_name', )}
    search_fields = ('user_name',)


class ImageAdmin(admin.ModelAdmin):
    list_display = ('photo',)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'writer_user_name',)
    prepopulated_fields = {'slug': ('title', )}

    @admin.display(ordering='writer_user_name')
    def writer_user_name(self, obj):
        return obj.writer.user_name


admin.site.register(Register, RegisterAdmin)
admin.site.register(User_Image, ImageAdmin)
admin.site.register(Articles, ArticleAdmin)
