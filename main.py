from util import to_pickle
from util import read_pickle
from whatsapp import open_whatsapp
from whatsapp import send_messages

real_phones = read_pickle('data/real_phones.pickle')
fake_phones = read_pickle('data/fake_phones.pickle')

# emojis = ['🔥','😀','💥','🎧','🎸','✌','🙌','😄','🙂','🙃']
emojis = [':)', ':D', '!!']

msg_1 = 'Oi, td bem? Meu nome é Layane, to divulgando o novo single dos meninos do Passageiro, dá uma olhada, ve o que vc achou e me conta depois!'
msg_2 = 'Oie, tudo joia? Eu sou a Layane, queria te mostrar a nova música do Passageiro, os meninos são MUITO BONS, aqui de Uberlândia, clica pra ver!'
msg_3 = 'E aí, tá joia? Só queria te contar que o duo Passageiro lançou uma música muito massa! Quer ver? Clica aí no link... Já está no Spotify e no YouTube! Muito obrigada pela atenção' 

phones = read_pickle('data/34988.pickle')
phones = [phone for phone in phones if phone not in real_phones and phone not in fake_phones]

adlink = 'https://www.youtube.com/watch?v=DyBvq1x0qwY&list=RDEMQpWOLGqXNbM7x1yAl8Rnqw&start_radio=1'
msg_list = [msg_1, msg_2, msg_3]

def scan_qr(phones):
    driver = open_whatsapp(headless=False, phone=phones[0])
    return driver
    
def run(driver, msg_list=msg_list, adlink=adlink):
	send_messages(driver, phones, msg_list, adlink)
    
driver = scan_qr(phones)
run(driver)

