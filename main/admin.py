from django.contrib import admin
from .models import Module, Task, Participant


class TaskInline(admin.TabularInline):
    model = Task
    extra = 1


class ModuleAdmin(admin.ModelAdmin):
    inlines = [TaskInline]


class ParticipantAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'task')
    list_filter = ('task',)
    search_fields = ('name', 'email')


admin.site.register(Module, ModuleAdmin)
admin.site.register(Participant, ParticipantAdmin)
