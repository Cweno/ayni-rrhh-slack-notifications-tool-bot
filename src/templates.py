birthday = {
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
                        "text": ":birthday: FELIZ CUMPLEAÑOS PERSONA :birthday:",    #
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
                        "text": "MENSAJE"   #
                    },
            "accessory": {
                        "type": "image",
                        "image_url": "https://aynitech-employees-profile-pics.s3.us-east-2.amazonaws.com/IMAGEN",  #
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

announcement = {
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
				"text": "TITULO",
				"emoji": True
			}
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "TEXTO_ARRIBA"
			}
		},
		{
			"type": "image",
			"title": {
				"type": "plain_text",
				"text": "image1",
				"emoji": True
			},
			"image_url": "https://aynitech-employees-profile-pics.s3.us-east-2.amazonaws.com/IMAGEN",
			"alt_text": "image1"
		},
		{
			"type": "section",
			"text": {
				"type": "mrkdwn",
				"text": "TEXTO_ABAJO"
			}
		}
	]
}