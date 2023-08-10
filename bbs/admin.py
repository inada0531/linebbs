from django.contrib import admin
from bbs.models import Post

class PostAdmin(admin.ModelAdmin):
    pass

#実際に管理サイトに登録している
admin.site.register(Post, PostAdmin)

# Register your models here.
