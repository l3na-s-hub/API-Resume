from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'categories'
    
    def __str__(self):
        return self.name

class Resume(models.Model):
    id = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    patronymic = models.CharField(max_length=100, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=20)
    birth_date = models.DateField()
    passport = models.CharField(max_length=50)
    education_level = models.CharField(max_length=100)
    marital_status = models.CharField(max_length=50)
    has_children = models.BooleanField(default=False)
    military_service = models.BooleanField(default=False)
    position = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    status = models.BooleanField(default=True)
    driver_license = models.CharField(max_length=50, blank=True, null=True)
    personal_qualities = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'resumes'
    
    def __str__(self):
        return f"{self.secondname} {self.firstname} - {self.position}"

class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='work_experiences')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    responsibilities = models.TextField(blank=True, null=True)
    
    class Meta:
        db_table = 'work_experiences'

class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    institution = models.CharField(max_length=255)
    degree = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    
    class Meta:
        db_table = 'educations'

class Course(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='courses')
    name = models.CharField(max_length=255)
    organization = models.CharField(max_length=255, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    
    class Meta:
        db_table = 'courses'

class Language(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='languages')
    language = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'languages'

class ComputerSkill(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='computer_skills')
    skill = models.CharField(max_length=100)
    level = models.CharField(max_length=50)
    
    class Meta:
        db_table = 'computer_skills'