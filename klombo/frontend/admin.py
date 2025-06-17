# frontend/admin.py
from django.contrib import admin

# Register your models here.
from .models import User 
from .models import Group 
from .models import Post 
from .models import Comment 
from .models import Like 

# Define the admin class
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'password', 'time')
class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'time')
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'text', 'image', 'time')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('userid', 'text', 'time')
class LikeAdmin(admin.ModelAdmin):
    list_display = ('userid', 'commentid', 'time')

admin.site.register(User, UserAdmin)
admin.site.register(Group, GroupAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Like, LikeAdmin)