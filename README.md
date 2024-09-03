
<h1>MLFLOW docker compose working sample </h1>

---

<b>Introduction</b>

Welcome to the ultimate solution for setting up a secure artificial intelligence development environment—complete with your own database, machine learning manager, and distributed cloud-compatible file server—all in less than a minute. This repository was created with that goal in mind.



The main idea behind this project is to simplify the setup process by providing a Docker Compose configuration that includes everything you need to get started quickly. With just a few commands, you’ll have an MLflow server running, utilizing MinIO for artifact storage and PostgreSQL as the database, all while ensuring data persistence through Docker volumes.

<b>Features</b>

	•	One-Click Setup: Get your AI environment up and running with a single command.
	•	MLflow Integration: Easily track and manage your machine learning experiments.
	•	MinIO for Artifact Storage: A cloud-compatible, distributed file server for storing your ML artifacts.
	•	PostgreSQL Database: Robust and reliable database support with persistent data storage.
	•	Docker Volumes: Ensures data persistence across containers.

Quick Start

```

gh repo clone bygregonline/mlflow-docker-compose
cd mlflow-docker-compose
./build_containers.sh
./create_columens.sh
docker compose up -d



```



![diagram](img/mlflow.png)

Steps

1. clone the repo
2. ./build_containers.sh
3. ./create_columens.sh
4. docker compose up -d

</br>
</br>



VOILA thats all you need to do

---

if you want to stop
docker compose down


---

**NO SE COMO HACER QUE FUNCIONE EN WINDOWS NI ME INTERESA INVESTIGARLO
