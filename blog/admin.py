from blog.models import Entries
from blog.models import Categories
from blog.models import TagModel
from django.contrib import admin

class EntriesAdmin(admin.ModelAdmin):
	list_display = ['id','created','Title']	

class CategoriesAdmin(admin.ModelAdmin):
	pass

class TagModelAdmin(admin.ModelAdmin):
	pass

admin.site.register(Entries, EntriesAdmin)
admin.site.register(Categories, CategoriesAdmin)
admin.site.register(TagModel, TagModelAdmin)
