## Kafka Playground (Local Dev)

<p align="center">
  <a href="https://kafka.apache.org/">
    <img alt="Apache Kafka" height="48" src="https://raw.githubusercontent.com/apache/kafka/trunk/docs/images/kafka_logo--simple.png" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://www.docker.com/">
    <img alt="Docker" height="48" src="https://raw.githubusercontent.com/docker/docs/main/content/manuals/engine/images/docker-logo.png" />
  </a>
  &nbsp;&nbsp;&nbsp;
  <a href="https://docs.confluent.io/platform/current/installation/docker/image-reference.html">
    <img alt="Confluent" height="48" src="https://raw.githubusercontent.com/confluentinc/confluent-kafka-python/master/docs/images/confluent-logo.png" />
  </a>
</p>

<p align="center">
  <img alt="Kafka" src="https://img.shields.io/badge/Apache_Kafka-231F20?logo=apachekafka&logoColor=white" />
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
  <img alt="Compose" src="https://img.shields.io/badge/Docker_Compose-v2-2496ED?logo=docker&logoColor=white" />
</p>

### What this repo is
This folder is my **Kafka dumping ground / playground** for local development experiments: quick Docker Compose stacks, small producers/consumers, and notes.

### Projects
- **`kafka-basic-cluster/`**: Single-node **Kafka (KRaft)** cluster via Docker Compose
  - Start it:

```bash
cd kafka-basic-cluster
docker compose up -d
```

  - Docs: see `kafka-basic-cluster/README.md`

### Conventions
- Each project is **self-contained** with its own `README.md`
- Keep local data in Docker volumes; reset with `docker compose down -v` when needed

### References
- [Apache Kafka](https://kafka.apache.org/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Confluent Docker image reference](https://docs.confluent.io/platform/current/installation/docker/image-reference.html)

