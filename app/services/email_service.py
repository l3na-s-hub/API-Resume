import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from typing import List
import os

class EmailService:
    
    @staticmethod
    def send_email(
        to_emails: List[str],
        subject: str,
        body: str,
        attachments: List[str] = None
    ):
        """Отправка email с вложениями"""
        # Настройки SMTP (заполнить реальные данные)
        smtp_server = os.getenv("SMTP_SERVER", "smtp.gmail.com")
        smtp_port = int(os.getenv("SMTP_PORT", "587"))
        smtp_username = os.getenv("SMTP_USERNAME", "")
        smtp_password = os.getenv("SMTP_PASSWORD", "")
        
        msg = MIMEMultipart()
        msg['From'] = smtp_username
        msg['To'] = ", ".join(to_emails)
        msg['Subject'] = subject
        
        msg.attach(MIMEText(body, 'html'))
        
        # Вложения
        if attachments:
            for file_path in attachments:
                with open(file_path, "rb") as attachment:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(attachment.read())
                    encoders.encode_base64(part)
                    part.add_header(
                        "Content-Disposition",
                        f"attachment; filename= {os.path.basename(file_path)}",
                    )
                    msg.attach(part)
        
        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
            server.quit()
            return True
        except Exception as e:
            print(f"Ошибка отправки email: {e}")
            return False
    
    @staticmethod
    def send_resume_notification(resume_id: int, to_email: str):
        """Уведомление о создании резюме"""
        subject = "Резюме успешно создано"
        body = f"""
        <html>
            <body>
                <h2>Ваше резюме успешно создано!</h2>
                <p>ID резюме: {resume_id}</p>
                <p>Вы можете отредактировать его в личном кабинете.</p>
            </body>
        </html>
        """
        return EmailService.send_email([to_email], subject, body)
