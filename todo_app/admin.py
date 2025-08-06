from django.contrib import admin
from .models import task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'completed', 'created_at', 'updated_at')
    search_fields = ('task',)
admin.site.register(task, TaskAdmin)
