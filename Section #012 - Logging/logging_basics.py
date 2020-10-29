import logging

print('This is an example')

'''
logging levels
DEBUG
INFO
WARNING
ERROR
CRITICAL
'''

logging.basicConfig(level=logging.DEBUG)

logging.debug('This is a short information')
logging.info('This is a short information')
logging.warning('This is a short information')
logging.error('This is a short information')
logging.critical('This is a short information')