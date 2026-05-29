from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from .models import Resume, WorkExperience, Education, Course, Language, ComputerSkill
from .forms import ResumeForm, WorkExperienceForm, EducationForm, CourseForm, LanguageForm, ComputerSkillForm
from django.db.models import Q
import requests
from django.http import HttpResponse

def resume_list(request):
    query = request.GET.get('q', '')
    if query:
        resumes = Resume.objects.filter(
            Q(firstname__icontains=query) | 
            Q(secondname__icontains=query) | 
            Q(position__icontains=query),
            status=True
        )
    else:
        resumes = Resume.objects.filter(status=True)
    
    return render(request, 'resume_admin/resume_list.html', {'resumes': resumes, 'query': query})

@login_required
def resume_create(request):
    WorkExperienceFormSet = inlineformset_factory(
        Resume, WorkExperience, form=WorkExperienceForm, extra=1, can_delete=True
    )
    EducationFormSet = inlineformset_factory(
        Resume, Education, form=EducationForm, extra=1, can_delete=True
    )
    CourseFormSet = inlineformset_factory(
        Resume, Course, form=CourseForm, extra=1, can_delete=True
    )
    LanguageFormSet = inlineformset_factory(
        Resume, Language, form=LanguageForm, extra=1, can_delete=True
    )
    ComputerSkillFormSet = inlineformset_factory(
        Resume, ComputerSkill, form=ComputerSkillForm, extra=1, can_delete=True
    )
    
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        work_formset = WorkExperienceFormSet(request.POST)
        edu_formset = EducationFormSet(request.POST)
        course_formset = CourseFormSet(request.POST)
        lang_formset = LanguageFormSet(request.POST)
        skill_formset = ComputerSkillFormSet(request.POST)
        
                # Сначала проверяем, что абсолютно все формы заполнены без ошибок
        if (form.is_valid() and 
            work_formset.is_valid() and 
            edu_formset.is_valid() and 
            course_formset.is_valid() and 
            lang_formset.is_valid() and 
            skill_formset.is_valid()):
            
            # Сохраняем основное резюме
            resume = form.save(commit=False)
            resume.save()
            
            # Привязываем резюме к каждому блоку и сохраняем их
            work_formset.instance = resume
            work_formset.save()
            
            edu_formset.instance = resume
            edu_formset.save()
            
            course_formset.instance = resume
            course_formset.save()
            
            lang_formset.instance = resume
            lang_formset.save()
            
            skill_formset.instance = resume
            skill_formset.save()
            
            return redirect('resume_detail', resume_id=resume.id)

    else:
        form = ResumeForm()
        work_formset = WorkExperienceFormSet()
        edu_formset = EducationFormSet()
        course_formset = CourseFormSet()
        lang_formset = LanguageFormSet()
        skill_formset = ComputerSkillFormSet()
    
    return render(request, 'resume_admin/resume_form.html', {
        'form': form,
        'work_formset': work_formset,
        'edu_formset': edu_formset,
        'course_formset': course_formset,
        'lang_formset': lang_formset,
        'skill_formset': skill_formset,
        'title': 'Создание резюме'
    })

@login_required
def resume_edit(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    
    WorkExperienceFormSet = inlineformset_factory(
        Resume, WorkExperience, form=WorkExperienceForm, extra=1, can_delete=True
    )
    EducationFormSet = inlineformset_factory(
        Resume, Education, form=EducationForm, extra=1, can_delete=True
    )
    CourseFormSet = inlineformset_factory(
        Resume, Course, form=CourseForm, extra=1, can_delete=True
    )
    LanguageFormSet = inlineformset_factory(
        Resume, Language, form=LanguageForm, extra=1, can_delete=True
    )
    ComputerSkillFormSet = inlineformset_factory(
        Resume, ComputerSkill, form=ComputerSkillForm, extra=1, can_delete=True
    )
    
    if request.method == 'POST':
        form = ResumeForm(request.POST, instance=resume)
        work_formset = WorkExperienceFormSet(request.POST, request.FILES, instance=resume)
        edu_formset = EducationFormSet(request.POST, request.FILES, instance=resume)
        course_formset = CourseFormSet(request.POST, request.FILES, instance=resume)
        lang_formset = LanguageFormSet(request.POST, request.FILES, instance=resume)
        skill_formset = ComputerSkillFormSet(request.POST, request.FILES, instance=resume)
        
        # Проверяем основную форму и все формсеты на валидность
        if (form.is_valid() and 
            work_formset.is_valid() and 
            edu_formset.is_valid() and 
            course_formset.is_valid() and 
            lang_formset.is_valid() and 
            skill_formset.is_valid()):
            
            # Сохраняем данные только если все формы валидны
            resume = form.save()
            work_formset.save()
            edu_formset.save()
            course_formset.save()
            lang_formset.save()
            skill_formset.save()
            
            return redirect('resume_detail', resume_id=resume.id)
    else:
        form = ResumeForm(instance=resume)
        work_formset = WorkExperienceFormSet(instance=resume)
        edu_formset = EducationFormSet(instance=resume)
        course_formset = CourseFormSet(instance=resume)
        lang_formset = LanguageFormSet(instance=resume)
        skill_formset = ComputerSkillFormSet(instance=resume)
    
    return render(request, 'resume_admin/resume_form.html', {
        'form': form,
        'work_formset': work_formset,
        'edu_formset': edu_formset,
        'course_formset': course_formset,
        'lang_formset': lang_formset,
        'skill_formset': skill_formset,
        'resume': resume,
        'title': 'Редактирование резюме'
    })


def resume_detail(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    return render(request, 'resume_admin/resume_detail.html', {'resume': resume})

@login_required
def resume_delete(request, resume_id):
    resume = get_object_or_404(Resume, id=resume_id)
    if request.method == 'POST':
        resume.delete()
        return redirect('resume_list')
    
    return render(request, 'resume_admin/resume_confirm_delete.html', {'resume': resume})

def export_resume(request, resume_id, format):
    api_url = "http://localhost:8000/api/v1/export/"
    
    payload = {
        "resume_ids": [resume_id],
        "format": format.upper()
    }
    
    try:
        response = requests.post(api_url, json=payload)
        
        if response.status_code == 200:
            file_data = response.json()
            download_url = f"http://localhost:8000{file_data['download_url']}"
            file_response = requests.get(download_url)
            
            http_response = HttpResponse(file_response.content, content_type='application/octet-stream')
            http_response['Content-Disposition'] = f'attachment; filename="{file_data["filename"]}"'
            return http_response
        else:
            return HttpResponse(f"Ошибка экспорта: {response.status_code}", status=400)
    except Exception as e:
        return HttpResponse(f"Ошибка подключения к API: {str(e)}", status=500)