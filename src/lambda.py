# from dotenv import load_dotenv
# from dotenv import load_dotenv 

from datetime import datetime
# load_dotenv()
# from ..bot.birthday import birthday_
from .birthday import birthday_
from .event import event_
from .announce import announcement_

TYPES = [
    {
        'hour': 14,
        'minute': 0,
        'type': 'birthday'
    },
    {
        'hour': 13,
        'minute': 30,
        'type': 'event'
    },
    {
        'hour': 17,
        'minute': 0,
        'type': 'announcement'
    },
]
    
def get_type(dt:str):
    event_time = datetime.strptime(dt, '%Y-%m-%dT%H:%M:%S%z')
    return list(
        filter(lambda t: t['hour'] == event_time.hour and t['minute'] == event_time.minute,
        TYPES)
    )[0]['type']

def handler(event, context):
    try:
        if 'time' in event:
            # clodwatch event
            event_type = get_type(event['time'])
            if event_type == 'birthday': birthday_()
            if event_type == 'event': event_()
            if event_type == 'announcement': announcement_() 
        else:
            # remote triggered
            if event['type'] == 'birthday': birthday_( { 'id': event['id'] } )
            if event['type'] == 'event': event_( { 'id': event['id'] } )
            if event['type'] == 'announcement': announcement_( { 'id': event['id'] } )
            
    except Exception as ex:
        print(ex)

handler(None, None)
