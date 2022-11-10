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
	]
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
        "text": "assasas",
        "emoji": True
    },
    "image_url": "",
    "alt_text": "image1"
}



TABLA = os.getenv('ANNOUNCEMENTS_TABLE')
BUCKET_IMAGENES = os.getenv('BUCKET_IMAGES')
WEBHOOK = os.getenv('SLACK_HOOK_EVE_ANN')

def anunciar(anuncio:dict):
    try:
        slack = dict(TEMPLATE)
        slack['blocks'][1]['text']['text'] = anuncio['name'].upper()
        for parrafo in anuncio['texts']['arriba']:
            seccion = dict(SECTION)
            seccion['text']['text'] = parrafo
            slack['blocks'].append(seccion)
        
        imagen = dict(IMAGE)
        imagen['title']['text'] = anuncio['name']
        imagen['image_url'] = f'https://{BUCKET_IMAGENES}.s3.{os.getenv("REGION")}.amazonaws.com/announcement/{anuncio["id"]}'
        imagen['alt_text'] = anuncio['name']
        slack['blocks'].append(imagen)

        for parrafo in anuncio['texts']['abajo']:
            seccion = dict(SECTION)
            seccion['text']['text'] = parrafo
            slack['blocks'].append(seccion)

        response = slack_call(slack, WEBHOOK)
        print(response.status)


    except Exception as ex: 
        print(ex)

def announcement_(data=None):
    try:
        month, day, year, bisiesto = get_today()
        if not data:
            # buscar en BD
            announcements = get_all(TABLA, day, month)
            if month == 3 and day == 1 and not bisiesto:
                announcements += get_all(29, 2)
        else:
            # usar la data
            announcements = get_specific(TABLA, data['id'])

        if len(announcements)>0:
            for announcement in announcements:
                if announcement['year'] in [ 0, year ]: anunciar(announcement)

    except Exception as ex:
        print(ex)