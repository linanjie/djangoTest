from django.contrib import admin
from .models import Article, Person


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # list_display 就是来配置要显示的字段的，当然也可以显示非字段内容，或者字段相关的内容
    list_display = ('title', 'pub_date', 'update_time')


class PersonAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


admin.site.register(Article, ArticleAdmin)
admin.site.register(Person, PersonAdmin)
