"""API endpoints for various results"""

import logging


def get_result(id):
    # TODO this is just a a stub
    logging.info('logging from index action')
    return {"id": id, "welcome_message": "Will return the result"}, 200
