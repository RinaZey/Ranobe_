from ranobes.models import Ranobe
from ranobes.types import RanobeObject

from apps.common.services import model_update, get_fields_to_update

from backend.rabbitmq_config import get_rabbitmq_connection, RABBITMQ_QUEUE
import json

from django.db import transaction

import logging

logger = logging.getLogger(__name__)

@transaction.atomic

def send_message_to_queue(message):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    channel.queue_declare(queue=RABBITMQ_QUEUE)
    channel.basic_publish(exchange='', routing_key=RABBITMQ_QUEUE, body=json.dumps(message))
    connection.close()

def create_ranobe(data: RanobeObject) -> Ranobe:
    """Сервис для создания рунабэ"""
    ranobe = Ranobe(title=data.title, status=data.status,
                  creator_id=data.creator)

    ranobe.clean()
    ranobe.save()

    ranobe.genres.set(data.genres)
    ranobe.tags.set(data.tags)

    logger.info(f"Ранобэ {ranobe.title} создана")

    # Отправка сообщения в RabbitMQ
    send_message_to_queue({"action": "create", "data": data.dict()})

    return ranobe

def update_ranobe(ranobe: Ranobe, data: RanobeObject) -> Ranobe:
    """Сервис для обновления рунабэ"""
    fields = get_fields_to_update(data)

    ranobe, _ = model_update(instance=ranobe, fields=fields,
                            data=data.dict())

    logger.info(f"Ранобэ {ranobe.title} data: {data.dict()} обновлена")

    # Отправка сообщения в RabbitMQ
    send_message_to_queue({"action": "update", "data": data.dict()})

    return ranobe
