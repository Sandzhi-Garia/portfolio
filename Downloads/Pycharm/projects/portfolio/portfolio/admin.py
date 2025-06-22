from django.contrib import admin
from django.utils.html import format_html
from .models import Projects, AboutMe, WorkExperience, Education, ContactMe, Blog, BlogImage, ProjectImage

admin.site.register(AboutMe)

# Admin for Work Experience
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date')

admin.site.register(WorkExperience, WorkExperienceAdmin)

# Admin for Education
class EducationAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'degree', 'start_date', 'end_date')

admin.site.register(Education, EducationAdmin)

admin.site.register(ContactMe)

# Inline admin for BlogImage
class BlogImageInline(admin.TabularInline):
    model = BlogImage
    extra = 10
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""

# Admin for Blog
class BlogAdmin(admin.ModelAdmin):
    inlines = [BlogImageInline]
    list_display = ('title', 'date')
    ordering = ['-date']

admin.site.register(Blog, BlogAdmin)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 10
    readonly_fields = ['preview']

    def preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" />', obj.image.url)
        return ""
class ProjectsAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline]
    list_display = ('title',)
admin.site.register(Projects, ProjectsAdmin)
