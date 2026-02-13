# 🚀 Apache Airflow Monitoring Stack (Prometheus & Grafana)

![Status](https://img.shields.io/badge/Status-Stable-green)
![Airflow](https://img.shields.io/badge/Airflow-2.7.1-blue)
![Grafana](https://img.shields.io/badge/Grafana-10.0.0-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

---

## 🇺🇸 English Version

### 📋 About the Project
This repository provides a professional **Observability** infrastructure for real-time monitoring of Apache Airflow instances. By integrating the `statsd-exporter`, this stack captures granular metrics from Airflow and visualizes them through Prometheus and Grafana, transforming silent logs into actionable insights.

### ✨ Key Features
* **Vitality Monitor (Heartbeat):** Binary status (Online/Offline) for the Airflow Scheduler using Value Mapping.
* **Throughput Tracking:** Real-time counter for successful task executions.
* **Performance Analysis:** Instantaneous task duration latency using the `rate()` function for high-precision monitoring.

### 🛠️ Technology Stack
* **Apache Airflow:** Workflow orchestrator.
* **Prometheus:** Time-series database for metric storage.
* **Grafana:** Analysis and visualization platform.
* **StatsD Exporter:** Translates Airflow UDP metrics into Prometheus-readable format.
* **Docker & Docker Compose:** Infrastructure containerization.

### 🏗️ Architecture
1.  **Airflow** sends metrics via the StatsD protocol (UDP).
2.  **StatsD Exporter** receives these packets and exposes them via HTTP.
3.  **Prometheus** scrapes these metrics periodically.
4.  **Grafana** queries Prometheus to render dynamic dashboards.

### 🚀 Getting Started
1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-user/airflow-monitoring-stack.git](https://github.com/your-user/airflow-monitoring-stack.git)<br>
    cd airflow-monitoring-stack
    ```
2.  **Deploy the stack:**
    ```bash
    docker compose up -d
    ```
3.  **Access the services:**
    * **Airflow:** `http://localhost:8080`
    * **Grafana:** `http://localhost:3000` (Default: admin/admin)
    * **Prometheus:** `http://localhost:9090`

### 📊 Advanced Metrics (PromQL)
To ensure accuracy, we utilize instant rate calculations instead of historical averages to identify current bottlenecks:
```promql
sum(rate(airflow_task_duration_sum[5m])) / sum(rate(airflow_task_duration_count[5m]))
```

## 🇧🇷 Versão em Português

### 📋 Sobre o Projeto
Este repositório fornece uma infraestrutura profissional de **Observabilidade** para monitoramento em tempo real de instâncias do Apache Airflow. Ao integrar o `statsd-exporter`, esta stack captura métricas granulares do Airflow e as visualiza por meio do Prometheus e Grafana, transformando logs silenciosos em insights acionáveis.

### ✨ Funcionalidades Principais
* **Monitor de Vitalidade (Heartbeat):** Status binário (Online/Offline) do Scheduler do Airflow utilizando Value Mapping.
* **Rastreamento de Throughput:** Contador em tempo real para execuções de tarefas bem-sucedidas.
* **Análise de Performance:** Latência instantânea da duração das tarefas usando a função `rate()` para monitoramento de alta precisão.

### 🛠️ Stack Tecnológica
* **Apache Airflow:** Orquestrador de workflows.
* **Prometheus:** Banco de dados de séries temporais para armazenamento de métricas.
* **Grafana:** Plataforma de análise e visualização.
* **StatsD Exporter:** Traduz métricas UDP do Airflow para o formato compreensível pelo Prometheus.
* **Docker & Docker Compose:** Containerização da infraestrutura.

### 🏗️ Arquitetura
1. **Airflow** envia métricas via protocolo StatsD (UDP).  
2. **StatsD Exporter** recebe esses pacotes e os expõe via HTTP.  
3. **Prometheus** coleta (scrape) essas métricas periodicamente.  
4. **Grafana** consulta o Prometheus para renderizar dashboards dinâmicos.

### 🚀 Como Começar
1. **Clone o repositório:**
    ```bash
    git clone https://github.com/your-user/airflow-monitoring-stack.git<br>
    cd airflow-monitoring-stack
    ```
2. **Suba a stack:**
    ```bash
    docker compose up -d
    ```
3. **Acesse os serviços:**
    * **Airflow:** `http://localhost:8080`
    * **Grafana:** `http://localhost:3000` (Padrão: admin/admin)
    * **Prometheus:** `http://localhost:9090`

### 📊 Métricas Avançadas (PromQL)
Para garantir precisão, utilizamos cálculos de taxa instantânea em vez de médias históricas, permitindo identificar gargalos em tempo real:
```promql
sum(rate(airflow_task_duration_sum[5m])) / sum(rate(airflow_task_duration_count[5m]))
