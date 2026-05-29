from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor
from datetime import datetime
import os
from app.models.resume import Resume

class PDFService:
    
    @staticmethod
    def register_fonts():
        """Регистрация шрифтов с поддержкой кириллицы"""
        try:
            # Попытка загрузить DejaVu шрифт
            pdfmetrics.registerFont(TTFont('DejaVuSans', 'fonts/DejaVuSans.ttf'))
            pdfmetrics.registerFont(TTFont('DejaVuSans-Bold', 'fonts/DejaVuSans-Bold.ttf'))
            return True
        except:
            # Если шрифт не найден, используем стандартный (без кириллицы)
            return False
    
    @staticmethod
    def create_resume_pdf(resume: Resume, filename: str = None) -> str:
        """Создание красивого PDF резюме"""
        if not filename:
            filename = f"exports/pdf/resume_{resume.id}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        
        c = canvas.Canvas(filename, pagesize=A4)
        width, height = A4
        
        # Регистрация шрифтов
        has_cyrillic = PDFService.register_fonts()
        font_regular = 'DejaVuSans' if has_cyrillic else 'Helvetica'
        font_bold = 'DejaVuSans-Bold' if has_cyrillic else 'Helvetica-Bold'
        
        # Цвета
        primary_color = HexColor('#2C3E50')
        secondary_color = HexColor('#34495E')
        accent_color = HexColor('#3498DB')
        
        y = height - 3*cm
        
        # === ЗАГОЛОВОК ===
        c.setFont(font_bold, 24)
        c.setFillColor(primary_color)
        fio = f"{resume.secondname} {resume.firstname} {resume.patronymic or ''}"
        c.drawString(2*cm, y, fio)
        
        y -= 0.8*cm
        c.setFont(font_bold, 16)
        c.setFillColor(accent_color)
        c.drawString(2*cm, y, resume.position)
        
        # Линия разделителя
        y -= 0.5*cm
        c.setStrokeColor(accent_color)
        c.setLineWidth(2)
        c.line(2*cm, y, width - 2*cm, y)
        
        y -= 1*cm
        
        # === КОНТАКТНАЯ ИНФОРМАЦИЯ ===
        c.setFont(font_bold, 12)
        c.setFillColor(primary_color)
        c.drawString(2*cm, y, "КОНТАКТНАЯ ИНФОРМАЦИЯ")
        
        y -= 0.6*cm
        c.setFont(font_regular, 10)
        c.setFillColor(secondary_color)
        
        contacts = [
            f"Email: {resume.email}",
            f"Телефон: {resume.phone}",
            f"Город: {resume.city}",
            f"Дата рождения: {resume.birth_date}",
            f"Пол: {resume.gender}"
        ]
        
        for contact in contacts:
            c.drawString(2.5*cm, y, contact)
            y -= 0.5*cm
        
        y -= 0.5*cm
        
        # === ОБРАЗОВАНИЕ ===
        c.setFont(font_bold, 12)
        c.setFillColor(primary_color)
        c.drawString(2*cm, y, "ОБРАЗОВАНИЕ")
        
        y -= 0.6*cm
        c.setFont(font_regular, 10)
        c.setFillColor(secondary_color)
        c.drawString(2.5*cm, y, f"Уровень: {resume.education_level}")
        y -= 0.5*cm
        
        if resume.educations:
            for edu in resume.educations:
                c.setFont(font_bold, 10)
                c.drawString(2.5*cm, y, edu.institution)
                y -= 0.4*cm
                c.setFont(font_regular, 9)
                c.drawString(2.5*cm, y, f"{edu.degree} ({edu.start_date} - {edu.end_date or 'настоящее время'})")
                y -= 0.6*cm
        
        y -= 0.3*cm
        
        # === ОПЫТ РАБОТЫ ===
        if resume.work_experiences:
            c.setFont(font_bold, 12)
            c.setFillColor(primary_color)
            c.drawString(2*cm, y, "ОПЫТ РАБОТЫ")
            
            y -= 0.6*cm
            
            for exp in resume.work_experiences:
                # Проверка на новую страницу
                if y < 4*cm:
                    c.showPage()
                    y = height - 3*cm
                
                c.setFont(font_bold, 10)
                c.setFillColor(accent_color)
                c.drawString(2.5*cm, y, exp.company)
                y -= 0.4*cm
                
                c.setFont(font_regular, 10)
                c.setFillColor(secondary_color)
                c.drawString(2.5*cm, y, f"{exp.position}")
                y -= 0.4*cm
                
                c.setFont(font_regular, 9)
                period = f"{exp.start_date} - {exp.end_date or 'настоящее время'}"
                c.drawString(2.5*cm, y, period)
                y -= 0.5*cm
                
                if exp.responsibilities:
                    c.drawString(2.5*cm, y, f"Обязанности: {exp.responsibilities[:80]}...")
                    y -= 0.6*cm
            
            y -= 0.3*cm
        
        # === КОМПЬЮТЕРНЫЕ НАВЫКИ ===
        if resume.computer_skills:
            if y < 5*cm:
                c.showPage()
                y = height - 3*cm
            
            c.setFont(font_bold, 12)
            c.setFillColor(primary_color)
            c.drawString(2*cm, y, "КОМПЬЮТЕРНЫЕ НАВЫКИ")
            
            y -= 0.6*cm
            c.setFont(font_regular, 10)
            c.setFillColor(secondary_color)
            
            for skill in resume.computer_skills:
                c.drawString(2.5*cm, y, f"• {skill.skill} - {skill.level}")
                y -= 0.5*cm
            
            y -= 0.3*cm
        
        # === ИНОСТРАННЫЕ ЯЗЫКИ ===
        if resume.languages:
            if y < 4*cm:
                c.showPage()
                y = height - 3*cm
            
            c.setFont(font_bold, 12)
            c.setFillColor(primary_color)
            c.drawString(2*cm, y, "ИНОСТРАННЫЕ ЯЗЫКИ")
            
            y -= 0.6*cm
            c.setFont(font_regular, 10)
            c.setFillColor(secondary_color)
            
            for lang in resume.languages:
                c.drawString(2.5*cm, y, f"• {lang.language} - {lang.level}")
                y -= 0.5*cm
            
            y -= 0.3*cm
        
        # === КУРСЫ ===
        if resume.courses:
            if y < 4*cm:
                c.showPage()
                y = height - 3*cm
            
            c.setFont(font_bold, 12)
            c.setFillColor(primary_color)
            c.drawString(2*cm, y, "КУРСЫ И ТРЕНИНГИ")
            
            y -= 0.6*cm
            c.setFont(font_regular, 10)
            c.setFillColor(secondary_color)
            
            for course in resume.courses:
                c.drawString(2.5*cm, y, f"• {course.name} ({course.organization}, {course.year})")
                y -= 0.5*cm
        
        # === ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ ===
        if y < 5*cm:
            c.showPage()
            y = height - 3*cm
        
        y -= 0.5*cm
        c.setFont(font_bold, 12)
        c.setFillColor(primary_color)
        c.drawString(2*cm, y, "ДОПОЛНИТЕЛЬНАЯ ИНФОРМАЦИЯ")
        
        y -= 0.6*cm
        c.setFont(font_regular, 10)
        c.setFillColor(secondary_color)
        
        additional = [
            f"Семейное положение: {resume.marital_status}",
            f"Дети: {'Да' if resume.has_children else 'Нет'}",
            f"Военная служба: {'Да' if resume.military_service else 'Нет'}"
        ]
        
        if resume.driver_license:
            additional.append(f"Водительские права: {resume.driver_license}")
        
        if resume.personal_qualities:
            additional.append(f"Личные качества: {resume.personal_qualities}")
        
        for info in additional:
            c.drawString(2.5*cm, y, info)
            y -= 0.5*cm
        
        # Футер
        c.setFont(font_regular, 8)
        c.setFillColor(HexColor('#95A5A6'))
        c.drawString(2*cm, 1.5*cm, f"Резюме создано: {datetime.now().strftime('%d.%m.%Y %H:%M')}")
        c.drawRightString(width - 2*cm, 1.5*cm, f"ID: {resume.id}")
        
        c.save()
        return filename
