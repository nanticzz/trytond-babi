import os

TRYTON_DATABASE = os.environ['TRYTON_DATABASE']
TRYTON_CONFIG = os.environ['TRYTON_CONFIG']

#Enable this options to debug. More info in celery page.
CELERY_ALWAYS_EAGER = False
CELERY_EAGER_PROPAGATES_EXCEPTIONS = False
