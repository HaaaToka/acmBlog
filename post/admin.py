from django.contrib import admin
from .models import Post
# from post.models import Post üsttekiyle aynı

class PostAdmin(admin.ModelAdmin):

	list_display=['title','publishing']
	list_display_links=['title']
	list_filter=['publishing']
	search_fields=['title','content']
	#list_editable=['title']  display linksden title i sil

	class Meta:
		model=Post



admin.site.register(Post,PostAdmin)

