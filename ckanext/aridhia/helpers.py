import os
import json
import logging

log = logging.getLogger(__name__)

def language_options():
    '''ISO-639-1 Languages''' 
    path = os.path.join(os.path.dirname(os.path.realpath(__file__)),
                        'language-codes.json')
    languages = []
    try:
        with open(path) as f:
            try:
                languages = json.loads(f.read())
                log.info('Successfully loaded {} languages'.format(len(languages)))
                
            except ValueError as e:
                log.error(str(e))
                
    except IOError as e:
        log.error(str(e))
            
    return languages