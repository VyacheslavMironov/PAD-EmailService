import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class ResetToPasswordService:
    def __init__(self, request) -> None:
        self.login = 'vuacheslavmironov@yandex.ru'
        self.password = 'dscfdnwffnguymrn'
        self.server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        self.msg = MIMEMultipart()
        self.message = """
        <h3>
        Здравствуйте, недавно вы подали заявку на смену пароля, заявка была принята и ваш пароль изменён.
        </h3>
        <p>Ваш новый пароль:</p>
        <p>[[password]]</p>
        <br/>
        <p>Ели вы не подавали заявку на смену пароля, обратитесь в техническую поддержку.</p>
        <br/>
        <br/>
        <p>Со всем уважением!<br/>Вячеслав</p>
        """
        self.request = request
        

    def msg_construct(self):
        print(self.request.form.get('data_password'))
        if self.request.form.get('data_password'):
            self.message = self.message.replace('[[password]]', self.request.form.get('data_password'))

        return self.message


    def msg_context(self):
        self.msg['From'] = self.login
        self.msg['To'] = self.request.form.get('email')
        self.msg['Subject'] = "Смена пароля в PAD"
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

