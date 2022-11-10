from random import randint
import os
# from ..bot.util import slack_call, get_today, get_all, get_specific
from .util import slack_call, get_today, get_all, get_specific

TEMPLATE = {
    "blocks": [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "@channel"
            }
        },
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "",    #
                "emoji": True
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": ""   #
            },
            "accessory": {
                "type": "image",
                "image_url": "",  #
                "alt_text": "PERSONA"
            }
        },
        {
            "type": "divider"
        }
    ],
    'username': 'Cumpleaños',
    'icon_emoji': ":tada:"
}

MENSAJES = [
    'Te deseamos alegría y éxitos en la vida. Feliz cumpleaños PERSONA!! Que tengas un hermoso día',
    'Le deseamos un muy feliz cumpleaños a PERSONA. Le mandamos los mejores deseos para que goce de mucha felicidad en su vida',
    'Hoy le deseamos un feliz cumpleaños a PERSONA un nuevo año lleno de felicidad y buenos momentos! Felicidades',
    'Muchas felicidades PERSONA en el dia de tu cumpleaños. Disfrútalo al máximo!',
    'Nuestros mejores deseos para PERSONA en tu cumpleaños, un dia tan especial porque celebras un año más de vida!',
    'Te deseamos otro año de grandes oportunidades, logros y crecimiento personal. Feliz cumpleaños PERSONA!!'
]
TABLA = os.getenv('BIRTHDAYS_TABLE')
BUCKET_IMAGENES = os.getenv('BUCKET_IMAGES')
WEBHOOK = os.getenv('SLACK_HOOK_BIRTHDAY')

def get_random_index():
    return randint(0, len(MENSAJES)-1 )

def saludar(persona:dict):
    try:
        mensaje = MENSAJES[ get_random_index() ]
        mensaje = mensaje.replace('PERSONA', f"<@{persona['slackID']}>")
        slack = dict(TEMPLATE)

        slack['blocks'][1]['text']['text'] = f':birthday: FELIZ CUMPLEAÑOS {persona["name"].upper()} :birthday:'
        slack['blocks'][3]['text']['text'] =  mensaje.replace('PERSONA', f"<@{persona['slackID']}>")
        slack['blocks'][3]['accessory']['image_url'] = f"https://{BUCKET_IMAGENES}.s3.us-east-2.amazonaws.com/birthday/{persona['id']}" # NOMBRE
        slack['blocks'][3]['accessory']['alt_text'] = persona["name"].upper()

        response = slack_call(slack, WEBHOOK)
        print(response.status)

    except Exception as ex: 
        print(ex)
    
def birthday_(data=None):
    try:
        day, month, year, bisiesto = get_today()
        if not data:
            # buscar en BD
            gente = get_all(TABLA, day, month)
            if month == 3 and day == 1 and not bisiesto:
                gente += get_all(TABLA, 29, 2)
            
        else:
            # usar la data
            gente = get_specific(TABLA, data['id'])

        if len(gente)>0:
            for persona in gente: saludar(persona)

    except Exception as ex:
        print(ex)
