## Kafka Basic Cluster (KRaft) — Docker Compose

<p align="center">
  <img alt="Kafka (KRaft)" src="https://img.shields.io/badge/Kafka-KRaft-231F20?logo=apachekafka&logoColor=white" />
  <img alt="Docker Compose" src="https://img.shields.io/badge/Docker_Compose-v2-2496ED?logo=docker&logoColor=white" />
  <img alt="Image" src="https://img.shields.io/badge/Image-confluentinc%2Fcp--kafka-0B3D91" />
</p>

### What this is
This project starts a **single-node Kafka broker** (via Confluent’s `confluentinc/cp-kafka` image) running in **KRaft mode (no ZooKeeper)** using Docker Compose. It is intended for **local development** and quick Kafka testing.

### Prerequisites
- **Docker Desktop** (or Docker Engine)
- **Docker Compose v2** (`docker compose` command)
- **Kafka Image** (confluentinc/cp-kafka:7.8.3)

### Quick start
Run Kafka:

```bash
docker compose up -d
```

Verify it’s running:

```bash
docker compose ps
docker compose logs -f kafka
```

Stop:

```bash
docker compose down
```

Remove all data (fresh cluster):

```bash
docker compose down -v
```

### Python demo (producer + consumer)
Create a virtualenv and install deps:

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run the consumer (leave it running):

```bash
python consumer.py
```

In another terminal, publish a few orders:

```bash
python producer.py
```

Notes:
- The scripts default to `KAFKA_BOOTSTRAP_SERVERS=localhost:9092`.
- To re-read from the beginning, use a new group id:

```bash
KAFKA_GROUP_ID=order-tracking-2 python consumer.py
```

### Connectivity (ports + listeners)
This compose config defines **three listeners**:
- **HOST**: for clients on your laptop
  - **Published port**: `localhost:9092`
- **DOCKER**: for clients running in other containers on the same Compose network
  - **Internal only**: `kafka:9094` (not published to host)
- **CONTROLLER**: internal KRaft controller listener
  - **Internal only**: `kafka:9093` (not published to host)

### Example client configs
- **From your host machine** (CLI tools, apps running on your laptop):
  - `bootstrap.servers=localhost:9092`

- **From another container in the same Compose project/network**:
  - `bootstrap.servers=kafka:9094`

### Kafka CLI (inside the broker container)

```bash
docker exec -it kafka kafka-console-consumer --bootstrap-server localhost:9092 --topic orders --from-beginning
```

### Notes (KRaft `CLUSTER_ID`)
`CLUSTER_ID` must remain **stable** once the data volume exists.

- If you change `CLUSTER_ID` after the volume is created, Kafka will fail to start.
- To reset safely, run `docker compose down -v` and start again.

### Files
- `docker-compose.yaml`: Kafka service definition
- `producer.py`: publishes sample `orders` events
- `consumer.py`: prints received `orders` events

### Troubleshooting
- **Port already in use (9092)**: stop the conflicting process/container or change the published port mapping.
- **Clients can’t connect from another container**: use `kafka:9094` (not `localhost:9092`).
- **Kafka won’t start after config changes**: try a clean reset with `docker compose down -v`.

### References
- [Apache Kafka](https://kafka.apache.org/)
- [Confluent cp-kafka Docker image](https://docs.confluent.io/platform/current/installation/docker/image-reference.html)
- [Docker Compose](https://docs.docker.com/compose/)
