import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

send_email = 'godp23@naver.com'
send_pwd = '127selle!'

recv_email = 'godp4785@gmail.com'

smtp_name = 'smtp.naver.com'
smtp_port = 587

msg = MIMEMultipart()

msg['Subject'] = 'html로 보내는 메일 입니다.'
msg['From'] = send_email
msg['To'] = recv_email

html_body = """
<p>안뇽 html 형식으로 보내는 이메일 테스트야</p>
<p><span style="color: #00ffff;">글자의 색상을 지정하거나</span></p>
<h1>크기를 조정할 수 있지</h1>
<p>표도 만들수 있단다&nbsp;</p>
<p>요렇게</p>
<table class="editorDemoTable">
<tbody>
<tr>
<td><strong>Name</strong></td>
<td><strong>City</strong></td>
<td><strong>Age</strong></td>
</tr>
<tr>
<td>John</td>
<td>Chicago</td>
<td>23</td>
</tr>
<tr>
<td>Lucy</td>
<td>Wisconsin</td>
<td>19</td>
</tr>
<tr>
<td>Amanda</td>
<td>Madison</td>
<td>22</td>
</tr>
</tbody>
</table>
<p>요롱롱롱</p>
"""

msg.attach(MIMEText(html_body, 'html'))

s=smtplib.SMTP(smtp_name, smtp_port)
s.starttls()
s.login(send_email, send_pwd)
s.sendmail(send_email, recv_email, msg.as_string())
s.quit()