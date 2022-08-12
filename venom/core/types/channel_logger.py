# channel_logger.py

from typing import Union

from venom import Config
from .. import client as _client


def _get_string(name: str) -> str:
    return "**ChannelLogger** : #" + name.split('.')[-1].upper() + "\n\n{}"


class ChannelLogger:

    def __init__(self, client: Union['_client.Venom', '_client.VenomBot'], name: str) -> None:
        self._id = Config.LOG_CHANNEL_ID
        self._client = client
        self._string = _get_string(name)

    async def log(self, input_: str):
        string_ = self._string.format(input_)
        return await self._client.send_message(chat_id=self._id, text=string_, dis_preview=True)