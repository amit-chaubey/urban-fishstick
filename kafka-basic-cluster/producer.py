import json
import uuid

from confluent_kafka import Producer


TOPIC = "orders"


def delivery_report(err, msg):
    if err:
        print(f"❌ Delivery failed: {err}")
        return

    # Note: callbacks fire from producer.poll()/flush().
    print(f"✅ Delivered {msg.value().decode('utf-8')}")
    print(
        f"✅ Delivered to {msg.topic()} : partition {msg.partition()} : at offset {msg.offset()}"
    )


def build_orders():
    # One dict per Kafka message (your consumer expects a dict, not a list).
    return [
        {
            "order_id": str(uuid.uuid4()),
            "user_name": "Monty Python",
            "item_id": "1234567890",
            "item_name": "Pizza",
            "quantity": 30,
        },
        {
            "order_id": str(uuid.uuid4()),
            "user_name": "Linus Torvalds",
            "item_id": "1234567890",
            "item_name": "Pizza",
            "quantity": 4,
        },
    ]


def main():
    producer = Producer({"bootstrap.servers": "localhost:9092"})

    for order in build_orders():
        value = json.dumps(order).encode("utf-8")

        # key makes partitioning stable per-order (optional but recommended)
        producer.produce(
            topic=TOPIC,
            key=order["order_id"].encode("utf-8"),
            value=value,
            callback=delivery_report,
        )

        # Serve delivery callbacks without blocking.
        producer.poll(0)

    # Wait for all queued messages to be delivered.
    producer.flush()


if __name__ == "__main__":
    main()