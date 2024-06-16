# Kafka Producer and Consumer Examples

This repository contains examples of Kafka producers and consumers implemented in Python. The producer reads city data from a JSON file and sends it to Kafka, while the consumer reads the data from Kafka. It also includes a docker-compose configuration to set up a Kafka cluster with three brokers for local development and testing.

## Prerequisites

- Docker and Docker Compose installed on your machine.
- Python 3.x installed on your machine.

## Setting Up the Python Environment

### Installing Poetry

If you don't have Poetry installed, you can install it by following the instructions on the Poetry website.

Alternatively, you can install it using the following command:

```
curl -sSL https://install.python-poetry.org | python3 -
```

### Installing Dependencies

To set up the Python environment and install the dependencies, follow these steps:

```
poetry install
```

## Start the Cluster

To start the Kafka cluster, run the following command in the directory containing the docker-compose.yml file:

```
docker-compose up -d
```

## Run consumer and producer

To start consumer and producer, run the following command in the directory:

```
python3 consumers/simple_consumer.py
```

and in a new terminal

```
python3 producers/simple_producer.py
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## License

This project is licensed under the MIT License.