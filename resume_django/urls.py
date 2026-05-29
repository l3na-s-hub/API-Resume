from django.contrib import admin
from django.urls import path
from resume_admin import views as resume_views
from accounts import views as accounts_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', resume_views.resume_list, name='resume_list'),
    path('resume/<int:resume_id>/', resume_views.resume_detail, name='resume_detail'),
    path('register/', accounts_views.register, name='register'),
    path('login/', accounts_views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('create/', resume_views.resume_create, name='resume_create'),
    path('edit/<int:resume_id>/', resume_views.resume_edit, name='resume_edit'),
    path('delete/<int:resume_id>/', resume_views.resume_delete, name='resume_delete'),
    path('export/<int:resume_id>/<str:format>/', resume_views.export_resume, name='export_resume'),
]