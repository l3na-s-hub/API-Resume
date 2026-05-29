from django import forms
from .models import Resume, WorkExperience, Education, Course, Language, ComputerSkill

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
            'has_children': forms.CheckboxInput(),
            'military_service': forms.CheckboxInput(),
            'address': forms.Textarea(attrs={'rows': 2, 'cols': 40}),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        exclude = ['id', 'resume']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        exclude = ['id', 'resume']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ['id', 'resume']
        widgets = {
            'year': forms.NumberInput(attrs={'type': 'number'}),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        exclude = ['id', 'resume']
        widgets = {
            'language': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(choices=[
                ('', '---------'), 
                ('Начальный', 'Начальный'), 
                ('Средний', 'Средний'), 
                ('Продвинутый', 'Продвинутый'), 
                ('Свободный', 'Свободный')
            ]),
        }

class ComputerSkillForm(forms.ModelForm):
    class Meta:
        model = ComputerSkill
        exclude = ['id', 'resume']
        widgets = {
            'skill': forms.TextInput(attrs={'class': 'form-control'}),
            'level': forms.Select(choices=[
                ('', '---------'), 
                ('Начальный', 'Начальный'), 
                ('Средний', 'Средний'), 
                ('Продвинутый', 'Продвинутый'), 
                ('Эксперт', 'Эксперт')
            ]),
        }

