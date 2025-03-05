import json
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import requests

from create_bot import bot
from . import connection
from . import model

# resultIndication = {
#    "idCounter": "",
#    "oldIndications": "",
#    "newIndications": ""
# }

listResultIndication = []


def findIdLs(numberLs):
    with connection.dbhandle:
        idLs = model.NumberLs.select().where(model.NumberLs.long_ls == numberLs)
        return findCounter(idLs)


def findIdLsIdTelegram(id_telegram):
    id_user = requests.get(f'http://127.0.0.1:8000/operarions/getUser?id_messanger={id_telegram}').json()

    if len(id_user) == 0:
        return id_user
    else:
        id_ls = requests.get(f'http://127.0.0.1:8000/operarions/getIdLs?id_user={id_user[0]["id"]}').json()
        return id_ls


def getIndication(id):
    data = requests.get(f'http://127.0.0.1:8000/operarions/getIndicationCounter?id_counter={id}').json()
    return data[0]['current_indications']


def getIdLs(numberLs):
    id = requests.get(f"http://127.0.0.1:8000/operarions/getLs?number_ls={numberLs}").json()
    if len(id) != 0:
        return id[0]['id']
    else:
        return 0


def getNumberLs(id_telegram):
    id_user = requests.get(f'http://127.0.0.1:8000/operarions/getUser?id_messanger={id_telegram}').json()
    number_ls = requests.get(f"http://127.0.0.1:8000/operarions/getIdLs?id_user={id_user[0]['id']}").json()
    return number_ls[0]['number_ls']


def findCounter(idLS):
    data = requests.get(f"http://127.0.0.1:8000/operarions/getCounter?id_ls={idLS}").json()
    return data


def setNewIndication(id, newIndication):
    requests.put(f"http://127.0.0.1:8000/operarions/setIndicationCounter?id_counter={id}&new_indication={newIndication}")


def setIdUserTelegram(ls, telegram_id):
    requests.post(f'http://127.0.0.1:8000/operarions/setIDMessenger?id_messanger={telegram_id}&number_ls={ls}')


def addLsUser(ls, id_telegram):
    id_user = requests.get(f'http://127.0.0.1:8000/operarions/getUser?id_messanger={id_telegram}').json()
    requests.put(f"http://127.0.0.1:8000/operarions/setIdUserLs?id_user={id_user[0]['id']}&number_ls={ls}")


def userRequest(data: {}):
    result = requests.post("http://127.0.0.1:8000/operarions/postRequest?"
                           f"id_user={data['id_user']}&"
                           f"name_request={data['name_request']}&"
                           f"fio={data['fio']}&"
                           f"phone={data['phone']}&"
                           f"email={data['emai']}&"
                           f"link_picture={data['list_foto']}")
    return json.loads(result.text)[0]


def getPayment(id_telegram):
    result = requests.get(f'http://127.0.0.1:8000/operarions/payment?id_user={id_telegram}')
    return result


async def sent_email_request():
    fromaddr = "prosolupovK@yandex.ru"
    mypass = "(tAz!k163)"
    toaddr = "snoob163@mail.ru"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr

    image = await bot.get_file("AgACAgIAAxkBAAIHA2Uj84DklX2yAZ7Hk0pmr-XVPlmoAAK22jEbNnUgSWIxMJUJCoQeAQADAgADeQADMAQ")

    part_file = MIMEBase('application', 'octet-stream; name="{}"'.format(image))
    part_file.set_payload(open(image, "rb").read())
    part_file.add_header('Content-Description', image)
    part_file.add_header('Content-Disposition', 'attachment; filename="{}"; size={}'.format(image, image))
    encoders.encode_base64(part_file)

    msg['Subject'] = "Отправитель: Telegram bot"
    body = "Message: Telegram_bot \n\n" + "Привет"
    msg.attach(MIMEText(body, 'plain'))
    msg.attach(part_file)
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()