import json
import random
import secrets
from dataclasses import dataclass

from src.streams import ALL_TOPICS, BrokerMessage, BrokerMessageHeaders


@dataclass
class KafkaMessage:
    key: str
    value: str
    topic: str
    headers: tuple[tuple[str, bytes], ...]


class KafkaMessageFactory:
    @staticmethod
    def build(**kwargs) -> KafkaMessage:
        data = {
            "key": secrets.token_hex(12),
            "value": json.dumps({"data": "message"}),
            "topic": random.choice(list(ALL_TOPICS)),
            "headers": (
                (
                    "event_type",
                    random.choice(
                        [
                            b"NEW_METRICS",
                            b"OTHER",
                        ]
                    ),
                ),
            ),
            **kwargs,
        }
        return KafkaMessage(**data)


class BrokerMessageHeadersFactory:
    @staticmethod
    def build(**kwargs) -> BrokerMessageHeaders:
        data = dict(
            event_type=secrets.token_hex(8),
            code=str(random.randrange(1000, 3000)),
            device_primary_identifier=secrets.token_hex(12),
        )
        data.update(**kwargs)
        return BrokerMessageHeaders(**data)


class BrokerMessageFactory:
    @staticmethod
    def build(**kwargs) -> BrokerMessage:
        data = dict(
            key=secrets.token_hex(12),
            source_topic=random.choice(list(ALL_TOPICS)),
            value=json.dumps({"data": "message"}),
            headers=BrokerMessageHeadersFactory.build(),
        )
        data.update(**kwargs)
        return BrokerMessage(**data)