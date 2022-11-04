import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class RegistrationService:
    def __init__(self, request) -> None:
        self.login = 'vuacheslavmironov@yandex.ru'
        self.password = 'dscfdnwffnguymrn'
        self.server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        self.msg = MIMEMultipart()
        self.message = """
        <h3>
        Здравствуйте, недавно вы были добавлены в систему электронного журнала PAD
        администрацией организации [[organization]]
        </h3>
        <p>Ваши данные для входа:</p>
        <p>Логин: [[login]]</p>
        <p>Пароль: [[password]]</p>
        <br/>
        <p>Так же рекомендуем сразу активировать аккаунт перейдя по ссылке ниже:</p>
        <a href='[[link]]'>[[link]]</a>
        <br/>
        <br/>
        <p>Со всем уважением!<br/>Вячеслав</p>
        """
        self.request = request
        

    def msg_construct(self):
        if self.request.form.get('data_organization'):
            self.message = self.message.replace('[[organization]]', self.request.form.get('data_organization'))

        if self.request.form.get('data_login'):
            self.message = self.message.replace('[[login]]', self.request.form.get('data_login'))

        if self.request.form.get('data_password'):
            self.message = self.message.replace('[[password]]', self.request.form.get('data_password'))

        if self.request.form.get('data_link'):
            self.message = self.message.replace('[[link]]', self.request.form.get('data_link'))
        
        return self.message


    def msg_context(self):
        self.msg['From'] = self.login
        self.msg['To'] = self.request.form.get('email')
        self.msg['Subject'] = "Регистрация в PAD"
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

