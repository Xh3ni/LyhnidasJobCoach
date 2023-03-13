from . import views
from django.urls import path

urlpatterns = [
    path("", views.home, name="home"),
    path('job/', views.job_search_list, name='job-search-list'),
    path('job/<slug>', views.job_detail, name='job-detail'),
    path('profile/', views.my_profile, name='my-profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),
    path('profile/<slug>', views.profile_view, name='profile-view'),
    path('introduction/', views.candidate_details, name='detail-candidates'),
    path('delete_skills/', views.delete_skill, name='skill-delete'),
    path('job/<slug>/apply/', views.apply_job, name='apply-job'),
    path('job/<slug>/save/', views.save_job, name='save-job'),
    path('saved_job_list/', views.saved_jobs, name='saved-jobs'),
    path('applied_job_list/', views.applied_jobs, name='applied-jobs'),
    path('job/<slug>/remove/', views.remove_job, name='remove-job'),

    # recruiters

    path('hiring/', views.rec_details, name='detail-recruiters'),
    path('job/add/', views.add_job, name='add-job'),
    path('job/<slug>/edit/', views.edit_job, name='edit-job-post'),
    path('job/<slug>', views.job_detail, name='add-job-detail'),
    path('jobs/', views.all_jobs, name='job-list'),
    path('candidate/search/', views.search_candidates,  name='search-candidates'),
    path('job/<slug>/applicants', views.applicant_list, name='applicant-list'),
    path('job/<slug>/selected', views.selected_list, name='selected-list'),
    path('job/<job_id>/select-applicant/<can_id>/',
         views.select_applicant, name='select-applicant'),
    path('job/<job_id>>/remove-applicant/<can_id>/',
         views.remove_applicant, name='remove-applicant'),
]
