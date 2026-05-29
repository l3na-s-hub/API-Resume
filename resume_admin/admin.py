from django.contrib import admin
from .models import Category, Resume, WorkExperience, Education, Course, Language, ComputerSkill

class WorkExperienceInline(admin.TabularInline):
    model = WorkExperience
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class CourseInline(admin.TabularInline):
    model = Course
    extra = 1

class LanguageInline(admin.TabularInline):
    model = Language
    extra = 1

class ComputerSkillInline(admin.TabularInline):
    model = ComputerSkill
    extra = 1

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('id', 'secondname', 'firstname', 'position', 'status', 'city')
    list_filter = ('status', 'category', 'city')
    search_fields = ('secondname', 'firstname', 'email', 'phone')
    inlines = [WorkExperienceInline, EducationInline, CourseInline, LanguageInline, ComputerSkillInline]
    fieldsets = (
        ('Личная информация', {
            'fields': ('secondname', 'firstname', 'patronymic', 'photo', 'birth_date', 'gender')
        }),
        ('Контакты', {
            'fields': ('email', 'phone', 'city', 'address')
        }),
        ('Профессиональная информация', {
            'fields': ('position', 'category', 'status')
        }),
        ('Дополнительно', {
            'fields': ('education_level', 'marital_status', 'has_children', 'military_service', 'driver_license', 'personal_qualities')
        }),
    )
    
    actions = ['make_active', 'make_inactive']
    
    def make_active(self, request, queryset):
        updated = queryset.update(status=True)
        self.message_user(request, f'{updated} резюме активировано.')
    make_active.short_description = "Сделать активными"
    
    def make_inactive(self, request, queryset):
        updated = queryset.update(status=False)
        self.message_user(request, f'{updated} резюме деактивировано.')
    make_inactive.short_description = "Сделать неактивными"

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)