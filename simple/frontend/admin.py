from django.contrib import admin

# Register your models here.
from .models import Category
from .models import Image
from .models import Video

# Define the admin class
class CategoryAdmin( admin.ModelAdmin ):
    list_display = ( 'id', 'title' )

class ImageAdmin( admin.ModelAdmin ):
    list_display = ( 'category', 'image' )

class VideoAdmin( admin.ModelAdmin ):
    list_display = ( 'category', 'video' )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Video, VideoAdmin)