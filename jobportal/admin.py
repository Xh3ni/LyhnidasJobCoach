from django.contrib import admin
from .models import Job, Applicants, Selected, Profile, Skill, SavedJobs, AppliedJobs
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Job)
class JobAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'date_posted')
    search_fields = ['title', 'description']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('title', 'date_posted')
    summernote_fields = ('description')


@admin.register(Applicants)
class ApplicantsAdmin(admin.ModelAdmin):

    list_display = ('job', 'applicant', 'date_posted')
    list_filter = ('job', 'date_posted')
    search_fields = ['job', 'applicant']


@admin.register(Selected)
class SelectedAdmin(admin.ModelAdmin):

    list_display = ('job', 'applicant', 'date_posted')
    list_filter = ('job', 'date_posted')
    search_fields = ['job', 'applicant']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'slug', 'full_name')
    search_fields = ['full_name', 'user']
    prepopulated_fields = {'slug': ('user',)}
    list_filter = ('full_name', 'looking_for')


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):

    list_display = ('skill', 'user')
    list_filter = ('skill', 'user')
    search_fields = ['skill', 'user']


@admin.register(AppliedJobs)
class AppliedJobsAdmin(admin.ModelAdmin):

    list_display = ('job', 'date_posted')
    list_filter = ('job', 'date_posted')
    search_fields = ['job']


@admin.register(SavedJobs)
class SavedJobsAdmin(admin.ModelAdmin):

    list_display = ('job', 'date_posted')
    list_filter = ('job', 'date_posted')
    search_fields = ['job']
