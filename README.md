

---

# 📊 Monitoring Demo with Prometheus, Grafana & cAdvisor

This repository contains a complete **monitoring stack** using **Docker Compose**.

It demonstrates how to monitor:

* 🐍 **Python microservice app** – exposes `/orders` and `/metrics`
* 📈 **Prometheus** – collects metrics
* 📦 **cAdvisor** – container-level metrics
* 💻 **Node Exporter** – host-level metrics
* 🌐 **Blackbox Exporter** – endpoint probing (HTTP, ICMP, TCP)
* 📊 **Grafana** – visualization & dashboards

---

## 🚀 How to Run

### 1. Start the stack

```bash
docker compose up -d --build
```

Verify running containers:

```bash
docker ps --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
```

---

### 2. Test the Python microservice

Check health:

```bash
curl http://localhost:8000/health
```

Create an order:

```bash
curl -X POST http://localhost:8000/orders
```

View metrics:

```bash
curl http://localhost:8000/metrics
```

---

### 3. Prometheus – Metrics Collection

Prometheus runs at:
👉 [http://localhost:9090](http://localhost:9090)

Check scrape targets:
👉 [http://localhost:9090/targets](http://localhost:9090/targets)

You should see:

* Python app
* cAdvisor
* Node Exporter
* Blackbox Exporter

---

### 4. Grafana – Visualization

Grafana runs at:
👉 [http://localhost:3000](http://localhost:3000)

#### Add Prometheus datasource:

1. Log in (default user: `admin` / `admin`).
2. Go to **Configuration → Data Sources → Add data source**.
3. Choose **Prometheus**.

   * Inside Compose: `http://prometheus:9090`
   * Outside Compose: `http://localhost:9090`
4. Click **Save & Test** → should say *"Data source is working"*.

#### Import Grafana dashboard:

1. Go to **Dashboards → Import**.
2. Click **Upload JSON file**.
3. Select JSON from `grafana_dash/` (e.g., `container_dashboard.json`).
4. Choose your Prometheus datasource → **Import**.

---

## 📊 Metrics You’ll See

### 🔹 System Metrics

* CPU usage per container
* Memory usage per container
* Network in/out bytes
* Filesystem usage
* Host CPU/Memory from **Node Exporter**

### 🔹 App Metrics

From the Python app:

* `order_created_total` – count of created orders
* `order_processing_seconds_bucket` – order processing latency histogram

### 🔹 Blackbox Metrics

From **Blackbox Exporter**:

* HTTP response times
* Status of endpoints (up/down)
* Ping latency

---

## 📂 Project Structure

```
.
├── app/                 # Python microservice
├── prometheus/          # Prometheus config (prometheus.yml, alerts.yml)
├── grafana_dash/        # Prebuilt Grafana dashboards (.json)
├── docker-compose.yml   # Orchestration
└── README.md            # This guide
```

---

✅ With this setup, you can **monitor your app, containers, host system, and endpoints** — all in one place.

---

