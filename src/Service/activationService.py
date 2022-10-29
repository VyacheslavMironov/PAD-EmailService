import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class ActivationService:
    def __init__(self, request) -> None:
        self.login = 'vuacheslavmironov@yandex.ru'
        self.password = 'dscfdnwffnguymrn'
        self.server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        self.msg = MIMEMultipart()
        self.message = """
        <h3>Уважаемый [[first_name]] ваш аккаунт успешно активирован!</h3>
        <p>Теперь вам доступен весь функционал журнала.</p>
        <a href='[[link]]' style='border: solid 2px gray;padding: 10px; width: 80px; display: table; text-align: center; background: blue; color: white; text-decoration: none; font-size: 16px;'>Вход</a>
        <br/>
        <br/>
        <p>Со всем уважением!<br/>Вячеслав</p>
        """
        self.request = request


    def msg_construct(self):
        if self.request.form.get('first_name'):
            self.message = self.message.replace('[[first_name]]', self.request.form.get('first_name'))

        if self.request.form.get('data_link'):
            self.message = self.message.replace('[[link]]', self.request.form.get('data_link'))
        
        return self.message


    def msg_context(self):
        self.msg['From'] = self.login
        self.msg['To'] = self.request.form.get('email')
        self.msg['Subject'] = "Subscription"
        self.msg.attach(MIMEText(self.msg_construct(), 'html'))
        return self.msg


    def service(self):
        self.server.login(self.login, self.password)
        self.server.sendmail(
            from_addr=self.login, 
            to_addrs=self.request.form.get('email'), 
            msg=self.msg_context().as_string()
        )
        return self.request.form.get('email')
