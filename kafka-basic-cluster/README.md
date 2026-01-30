## Kafka Basic Cluster (KRaft) — Docker Compose

<p align="center">
  <a href="https://kafka.apache.org/">
    <img alt="Apache Kafka" height="44" src="https://raw.githubusercontent.com/apache/kafka/trunk/docs/images/kafka_logo--simple.png" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://docs.confluent.io/platform/current/installation/docker/image-reference.html">
    <img alt="Confluent" height="44" src="https://raw.githubusercontent.com/confluentinc/confluent-kafka-python/master/docs/images/confluent-logo.png" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.docker.com/">
    <img alt="Docker" height="44" src="https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/images/docker-logo.png" />
  </a>
</p>

<p align="center">
  <img alt="Kafka (KRaft)" src="https://img.shields.io/badge/Kafka-KRaft-231F20?logo=apachekafka&logoColor=white" />
  <img alt="Docker Compose" src="https://img.shields.io/badge/Docker_Compose-v2-2496ED?logo=docker&logoColor=white" />
  <img alt="Image" src="https://img.shields.io/badge/Image-confluentinc%2Fcp--kafka-0B3D91" />
</p>

### What this is
This repo starts a **single-node Apache Kafka broker** running in **KRaft mode (no ZooKeeper)** using Docker Compose. It is intended for **local development** and quick Kafka testing.

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

### Notes (KRaft `CLUSTER_ID`)
`CLUSTER_ID` must remain **stable** once the data volume exists.

- If you change `CLUSTER_ID` after the volume is created, Kafka will fail to start.
- To reset safely, run `docker compose down -v` and start again.

### Files
- `docker-compose.yaml`: Kafka service definition

### Troubleshooting
- **Port already in use (9092)**: stop the conflicting process/container or change the published port mapping.
- **Clients can’t connect from another container**: use `kafka:9094` (not `localhost:9092`).
- **Kafka won’t start after config changes**: try a clean reset with `docker compose down -v`.

### References
- [Apache Kafka](https://kafka.apache.org/)
- [Confluent cp-kafka Docker image](https://docs.confluent.io/platform/current/installation/docker/image-reference.html)
- [Docker Compose](https://docs.docker.com/compose/)
