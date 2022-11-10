from .util import slack_call, get_today, get_all, get_specific
import os

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
				"text": "",
				"emoji": True
			}
		}
	],
    'username': 'Eventos',
    'icon_emoji': ":calendar:"
}

SECTION = {
    "type": "section",
    "text": {
        "type": "mrkdwn",
        "text": ""
    }
}

IMAGE = {
    "type": "image",
    "title": {
        "type": "plain_text",
        "text": "",
        "emoji": True
    },
    "image_url": "",
    "alt_text": ""
}

TABLA = os.getenv('EVENTS_TABLE')
BUCKET_IMAGENES = os.getenv('BUCKET_IMAGES')
WEBHOOK = os.getenv('SLACK_HOOK_EVE_ANN')

def avisar(notice:dict):
    try:
        slack = dict(TEMPLATE)
        slack['blocks'][1]['text']['text'] = notice['name'].upper()
        for parrafo in notice['texts']['arriba']:
            seccion = dict(SECTION)
            seccion['text']['text'] = parrafo
            slack['blocks'].append(seccion)
        
        imagen = dict(IMAGE)
        imagen['title']['text'] = notice['name']
        imagen['image_url'] = f'https://{BUCKET_IMAGENES}.s3.{os.getenv("REGION")}.amazonaws.com/event/{notice["id"]}'
        imagen['alt_text'] = notice['name']
        slack['blocks'].append(imagen)

        for parrafo in notice['texts']['abajo']:
            seccion = dict(SECTION)
            seccion['text']['text'] = parrafo
            slack['blocks'].append(seccion)
        response = slack_call(slack, WEBHOOK)
        print(response.status)


    except Exception as ex: 
        print(ex)

def event_(data:dict=None):
    try:
        month, day, year, bisiesto = get_today()
        if not data:
            # buscar en BD
            notices = get_all(TABLA, day, month)
            if month == 3 and day == 1 and not bisiesto:
                notices += get_all(29, 2)
        else:
            # usar la data
            notices = get_specific(TABLA, data['id'])
        if len(notices)>0:
            for notice in notices:
                if notice['year'] in [ 0, year ]: avisar(notice)

    except Exception as ex:
        print(ex)