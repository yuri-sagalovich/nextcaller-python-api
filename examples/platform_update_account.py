import logging
from pynextcaller.client import NextCallerPlatformClient
from pynextcaller.exceptions import HttpException


logger = logging.getLogger('nextcaller')
handler = logging.StreamHandler()
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

username = 'XXXXX'
password = 'XXXXX'
account_id = 'test'
sandbox = True
data = {
    'email': 'test@test.com'
}

client = NextCallerPlatformClient(username, password, sandbox=sandbox)

try:
    response_content = client.update_platform_account(account_id, data, debug=True)
    logger.info(response_content)
except HttpException as err:
    logger.error(
        'Response message: {}'.format(err.message),
    )
