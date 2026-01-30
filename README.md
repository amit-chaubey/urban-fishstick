## Kafka Playground (Local Dev)

<p align="center">
  <img alt="Kafka" src="https://img.shields.io/badge/Apache_Kafka-231F20?logo=apachekafka&logoColor=white" />
  <img alt="Docker" src="https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=white" />
  <img alt="Compose" src="https://img.shields.io/badge/Docker_Compose-v2-2496ED?logo=docker&logoColor=white" />
</p>

### Overview
This repository contains small, **self-contained Kafka projects** for local development and learning.

### Projects
- **`kafka-basic-cluster/`**: Single-node **Kafka (KRaft)** cluster via Docker Compose  
  Docs: see `kafka-basic-cluster/README.md`

### Quick start

```bash
cd kafka-basic-cluster
docker compose up -d
```

### Conventions
- Each project is self-contained with its own `README.md`
- Keep local data in Docker volumes; reset with `docker compose down -v` inside the project folder when needed

### References
- [Apache Kafka](https://kafka.apache.org/)
- [Docker Compose](https://docs.docker.com/compose/)
- [Confluent Docker image reference](https://docs.confluent.io/platform/current/installation/docker/image-reference.html)

