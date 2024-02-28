[<img src="https://github.com/jghoman/awesome-apache-airflow/raw/master/airflow-logo.png" align="right">](https://airflow.apache.org/)
# 🗺 Airflow Learning Journey

Welcome to my Airflow learning journey! 🤓 This repository serves as a comprehensive documentation of my exploration and understanding of Apache Airflow. Whether you're a beginner or an experienced user, I hope this documentation serves as a valuable resource for understanding Airflow and its capabilities. 

## Airflow
Airflow has emerged as a leading open-source workflow management solution, offering unparalleled flexibility and scalability in orchestrating data pipelines, machine learning workflows, and ETL processes. 

## 🚀 Getting Started
### Running Airflow in PyEnv

In this section, I've delved into the process of setting up and running Airflow within a PyEnv environment. PyEnv allows for creating isolated Python environments, ensuring seamless management of dependencies for Airflow.

### Running Airflow in Docker

Dockerizing Apache Airflow facilitates seamless deployment across different environments, ensuring consistency and reproducibility. I've delved through the process of pulling Airflow Docker images, configuring Docker Compose files, and launching Airflow containers with custom settings.

## 📄 Core Concepts
### Airflow Core Concepts & Basic Architecture

Understanding the core concepts of Airflow is essential for effective workflow orchestration. I've thoroughly studied concepts like Directed Acyclic Graphs (DAGs), Operators, Executors, and the Airflow Scheduler to grasp the fundamental workings of Airflow. Comprehending the basic architecture of Airflow lays the foundation for building robust data pipelines. From the central role of the Scheduler to the distributed nature of Executors, I've explored how each component contributes to the overall functioning of Airflow.

### Airflow Task Lifecycle

The lifecycle of tasks within Airflow DAGs plays a crucial role in defining workflow behavior. The lifecycle of an Airflow task involves various states and transitions, from being scheduled and queued to running, success, or failure. I explore each stage of the task lifecycle, discussing strategies for handling task failures, retries, and dependencies.

## 📈 DAGs (Directed Acyclic Graphs) 

### BashOperator

Creating DAGs with the BashOperator has been one of the initial steps in my Airflow journey. The BashOperator enables the execution of bash commands or scripts as individual tasks within a DAG. I've practiced use cases of the BashOperator for performing file operations, data transformations, and system commands within Airflow workflows. 

### PythonOperator

Utilizing PythonOperators within DAGs has enabled me to execute Python functions as tasks. This flexibility has allowed me to incorporate custom Python logic directly into Airflow workflows, enhancing automation and extensibility. I illustrate how to define Python functions as tasks within DAGs, passing inputs and outputs between tasks, and leveraging external libraries and APIs.

### PostgresOperator

The PostgresOperator in Airflow facilitates the execution of SQL commands and scripts against Postgres databases. I've utilized this operator to perform various database operations, including data ingestion, transformation, and extraction.

## 📝 Advanced Concepts 

### Data sharing via Airflow XComs

Airflow XComs provide a mechanism for sharing data between tasks within a DAG. I've explored various use cases where XComs facilitate communication and data exchange between tasks, promoting modular and scalable workflow design. I delve into the mechanics of XComs, demonstrating how to pass data between tasks, retrieve XCom values, and handle data serialization and deserialization.

### Airflow TaskFlow API

The TaskFlow API offers a higher-level abstraction for defining complex workflows in Airflow. By leveraging TaskFlow features such as branching, joining, and error handling, I've streamlined the development of intricate data pipelines.

### Airflow Catchup & Backfill

The catchup and backfill capabilities of Airflow enable historical data processing and rerunning of DAGs for past time periods. I discuss strategies for configuring catchup behavior, handling backfilling of data, and managing the execution of retroactive tasks.

## ⏳ Schedulers, Executors & Hooks 

### Airflow Scheduler with Cron Expression

Configuring the Airflow Scheduler with Cron expressions allows for precise scheduling of DAG runs. I've mastered the syntax and semantics of Cron expressions to orchestrate workflows at specific intervals or timeframes.

### Airflow Hooks

Airflow Hooks provide a convenient interface for interacting with external systems and services. I've leveraged Hooks to establish connections and perform operations with various services such as AWS, GCP, and databases, enhancing the extensibility and interoperability of Airflow workflows.

### Airflow Executors

Understanding the different types of Executors in Airflow is crucial for optimizing task execution and resource utilization. I've explored Local, Sequential, Celery, and Kubernetes Executors, evaluating their performance characteristics and suitability for different deployment scenarios.

## ⚒ Hands-on Practice Tasks 

### Airflow Connection with PostGres

Establishing connections with Postgres databases is a common requirement in Airflow environments. I've configured and managed connections to Postgres databases, enabling seamless interaction with external data sources and destinations, and performed troubleshooting connection issues.

### Airflow Docker Install Python Dependencies

Managing Python dependencies within Dockerized Airflow environments is crucial for reproducibility and consistency. I've explored different approaches for installing and managing Python dependencies using Docker, like Docker Image Extending and Docker Image Customizing for for optimizing dependency management and reducing image size.

### Airflow AWS S3/Minio Sensor Operator

The AWS S3 and Minio Sensor Operators in Airflow enable the detection of file presence or changes in S3 buckets or Minio storage. I've utilized these operators to trigger DAG execution based on file events, facilitating real-time data processing and integration.

## Acknowledgments

I extend my heartfelt gratitude to the Apache Airflow community for their invaluable contributions, insights, and support. Special thanks to the maintainers, contributors, and users of Apache Airflow for creating a vibrant and thriving ecosystem.

## Connect with Me

Let's connect and continue the conversation! Feel free to reach out to me via [LinkedIn](https://www.linkedin.com/in/sr099/) or [Twitter](https://twitter.com/wtfisshivang) to share your thoughts, insights, and experiences with Apache Airflow. I look forward to connecting with fellow Airflow enthusiasts and data engineering enthusiasts! I'm excited to continue my learning journey and explore further advancements in Airflow and data engineering.

