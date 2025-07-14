from django.contrib import admin
from .models import Course, Registration
from .models import Post

admin.site.register(Post)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'duration_weeks', 'price')
    search_fields = ('title',)


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'telegram_id', 'course')
    search_fields = ('full_name', 'telegram_id')
    list_filter = ('course',)
