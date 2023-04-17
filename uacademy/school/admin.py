from django.contrib import admin
from .models import *
from django.core.exceptions import ValidationError
from django.db import IntegrityError


class GradeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug')
    list_display_links = ('id', 'name')
    list_editable = ('is_active',)
    prepopulated_fields={"slug":("name",)}


class SubjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active', 'slug')
    list_display_links = ('id', 'name')
    list_editable = ('is_active',)
    search_fields = ["id", "name",]
    prepopulated_fields={"slug":("name",)}


class GradeSubjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active','slug_grade','slug_subject', 'additional_id')
    list_editable = ('is_active',)
    search_fields = ["id","additional_id"]
    #prepopulated_fields={"slug":("grade","subject",)}


admin.site.register(Grade, GradeAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(GradeSubject, GradeSubjectAdmin),
