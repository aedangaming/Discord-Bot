import logsetup
import logging

import events
import features
import commands

from bot import client, TOKEN

_logger = logging.getLogger("main")


_logger.info("main: Starting the bot...")
client.run(TOKEN)
