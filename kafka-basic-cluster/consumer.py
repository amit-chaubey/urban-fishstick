import json
import os
import time
from typing import Any, Dict, Iterable

from confluent_kafka import Consumer


TOPIC = "orders"
BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "localhost:9092")
GROUP_ID = os.getenv("KAFKA_GROUP_ID", "order-tracking")


def iter_orders(payload: Any) -> Iterable[Dict[str, Any]]:
    """
    Support both shapes:
    - a single order dict (recommended: 1 Kafka message = 1 order)
    - a list of order dicts (older producer versions)
    """
    if isinstance(payload, dict):
        yield payload
        return
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                yield item


def main() -> None:
    consumer = Consumer(
        {
            "bootstrap.servers": BOOTSTRAP_SERVERS,
            "group.id": GROUP_ID,
            "auto.offset.reset": "earliest",
        }
    )

    consumer.subscribe([TOPIC])

    last_idle_log_at = 0.0

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                now = time.time()
                if now - last_idle_log_at >= 10:
                    print("…waiting for new messages")
                    last_idle_log_at = now
                continue

            if msg.error():
                print(f"❌ Kafka message error: {msg.error()}")
                continue

            raw = msg.value()
            if raw is None:
                print("⚠️  Received message with empty value")
                continue

            try:
                payload = json.loads(raw.decode("utf-8"))
            except Exception as e:
                print(f"❌ Failed to parse JSON: {e}. raw={raw!r}")
                continue

            for order in iter_orders(payload):
                quantity = order.get("quantity", "?")
                item = order.get("item_name") or order.get("item") or "?"
                user = order.get("user_name") or order.get("user") or "?"
                print(f"📦 Received order: {quantity} x {item} from {user}")

    except KeyboardInterrupt:
        print("\n🔴 Stopping consumer")
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
