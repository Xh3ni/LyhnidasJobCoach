from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator

# candidates view


def home(request):
    context = {
        'home_page': "active",
    }
    return render(request, 'index.html', context)


def job_search_list(request):
    query = request.GET.get('p')
    loc = request.GET.get('q')
    object_list = []
    if (query == None):
        object_list = Job.objects.all()
    else:
        title_list = Job.objects.filter(
            title__icontains=query).order_by('-date_posted')
        skill_list = Job.objects.filter(
            skills_req__icontains=query).order_by('-date_posted')
        company_list = Job.objects.filter(
            company__icontains=query).order_by('-date_posted')
        job_type_list = Job.objects.filter(
            job_type__icontains=query).order_by('-date_posted')
        for i in title_list:
            object_list.append(i)
        for i in skill_list:
            if i not in object_list:
                object_list.append(i)
        for i in company_list:
            if i not in object_list:
                object_list.append(i)
        for i in job_type_list:
            if i not in object_list:
                object_list.append(i)
    if (loc == None):
        locat = Job.objects.all()
    else:
        locat = Job.objects.filter(
            location__icontains=loc).order_by('-date_posted')
    final_list = []
    for i in object_list:
        if i in locat:
            final_list.append(i)
    paginator = Paginator(final_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'jobs': page_obj,
        'query': query,
    }
    return render(request, 'job_search_list.html', context)


def job_detail(request, slug):
    job = get_object_or_404(Job, slug=slug)
    apply_button = 0
    save_button = 0
    profile = Profile.objects.filter(user=request.user).first()
    if AppliedJobs.objects.filter(user=request.user).filter(job=job).exists():
        apply_button = 1
    if SavedJobs.objects.filter(user=request.user).filter(job=job).exists():
        save_button = 1
    relevant_jobs = []
    jobs1 = Job.objects.filter(
        company__icontains=job.company).order_by('-date_posted')
    jobs2 = Job.objects.filter(
        job_type__icontains=job.job_type).order_by('-date_posted')
    jobs3 = Job.objects.filter(
        title__icontains=job.title).order_by('-date_posted')
    for i in jobs1:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)
    for i in jobs2:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)
    for i in jobs3:
        if len(relevant_jobs) > 5:
            break
        if i not in relevant_jobs and i != job:
            relevant_jobs.append(i)

    return render(request, 'job_detail.html', {'job': job, 'profile': profile, 'apply_button': apply_button, 'save_button': save_button, 'relevant_jobs': relevant_jobs, 'candidate_navbar': 1})


def saved_jobs(request):
    jobs = SavedJobs.objects.filter(
        user=request.user).order_by('-date_posted')
    return render(request, 'saved_jobs.html', {'jobs': jobs, 'candidate_navbar': 1})


def applied_jobs(request):
    jobs = AppliedJobs.objects.filter(
        user=request.user).order_by('-date_posted')
    statuses = []
    for job in jobs:
        if Selected.objects.filter(job=job.job).filter(applicant=request.user).exists():
            statuses.append(0)
        elif Applicants.objects.filter(job=job.job).filter(applicant=request.user).exists():
            statuses.append(1)
        else:
            statuses.append(2)
    zipped = zip(jobs, statuses)
    return render(request, 'applied_jobs.html', {'zipped': zipped, 'candidate_navbar': 1})


def apply_job(request, slug):
    user = request.user
    job = get_object_or_404(Job, slug=slug)
    applied, created = AppliedJobs.objects.get_or_create(job=job, user=user)
    applicant, creation = Applicants.objects.get_or_create(
        job=job, applicant=user)
    return HttpResponseRedirect('/job/{}'.format(job.slug))


def save_job(request, slug):
    user = request.user
    job = get_object_or_404(Job, slug=slug)
    saved, created = SavedJobs.objects.get_or_create(job=job, user=user)
    return HttpResponseRedirect('/job/{}'.format(job.slug))


def remove_job(request, slug):
    user = request.user
    job = get_object_or_404(Job, slug=slug)
    saved_job = SavedJobs.objects.filter(job=job, user=user).first()
    saved_job.delete()
    return HttpResponseRedirect('/job/{}'.format(job.slug))
