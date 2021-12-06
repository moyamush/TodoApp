from django.contrib import admin
from django.contrib.auth.admin import UserAdmin, GroupAdmin
from todo.models import CustomUser, CustomGroup, Task

# Djangoがデフォルトで用意しているUserを使用しない
class CustomUserAdmin(UserAdmin):
    #add_form = 
    #form =

    model = CustomUser
    list_display = ["username", "email", "is_staff"]

class CustomGroupAdmin(GroupAdmin):
    model = CustomGroup
    # list_display = ["groupname"]

# admin/でmodel.pyの内容を追加したい時に必要
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(CustomGroup, CustomGroupAdmin)
admin.site.register(Task)

#admin.site.register(User)