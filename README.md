# Qwen Coding Use Case - MLOps Project

## Tổng quan
Đồ án MLOps triển khai hệ thống Coding Multiple Choice Question Answering sử dụng mô hình Qwen2.5-Coder-1.5B-Instruct, tích hợp FastAPI, Docker Compose, Prometheus, Grafana, Jaeger, Jenkins CI/CD, Kubernetes, Helm, cloud-ready.

## Cấu trúc thư mục
```
qwen_coding_use_case/
├── src/                  # Source code FastAPI, model inference, metrics, tracing
│   ├── main.py
│   ├── model.py
│   ├── metrics.py
│   └── tracing.py
├── streamlit_ui/         # (Optional) Streamlit UI giữ lại nếu cần
│   └── app.py
├── tests/                # Unit test, API test
│   └── test_api.py
├── requirements.txt      # Python dependencies
├── Dockerfile            # Build FastAPI service
├── docker-compose.yml    # Compose all services: api, ui, prometheus, grafana, jaeger
├── Jenkinsfile           # CI/CD pipeline
├── k8s/                  # K8s manifest, Helm chart
│   ├── deployment.yaml
│   ├── service.yaml
│   ├── prometheus.yaml
│   ├── grafana.yaml
│   └── jaeger.yaml
├── monitoring/           # Prometheus, Grafana, Jaeger config
│   ├── prometheus.yml
│   └── grafana_dashboard.json
├── docs/                 # Tài liệu, changelog, hướng dẫn sử dụng
│   ├── README.md
│   ├── changelog.md
│   └── troubleshooting.md
└── .pre-commit-config.yaml # Lint, format, security check
```

## Hướng dẫn sử dụng
- Xem docs/README.md để biết cách chạy local, CI/CD, deploy k8s, cloud.
- Xem Jenkinsfile để biết pipeline tự động hóa.
- Xem monitoring/ để cấu hình Prometheus, Grafana, Jaeger.

## Ghi chú
- Mỗi file sẽ có hướng dẫn chi tiết, code mẫu, dễ mở rộng.
- Đáp ứng đầy đủ các tiêu chí MLOps, monitoring, scaling, security, cloud-ready.

<!-- ---
# Qwen-Coding-ideation-to-production-mlops -->
# Phân tích chiến lược MLOps cho dự án Coding Multiple Choice QA

## 1. Phân tích tổng thể & mục tiêu đồ án
- **Mục tiêu:** Biến ứng dụng Streamlit (đã có model Qwen2.5-Coder-1.5B-Instruct) thành một hệ thống MLOps production-ready, đáp ứng các tiêu chí về CI/CD, monitoring, scaling, observability, automation.
- **Yêu cầu:** Tích hợp các công nghệ: Python, FastAPI, Docker Compose, Prometheus, Grafana, Jaeger, Jenkins, Kubernetes, Helm, Cloud.

## 2. Chiến lược triển khai & roadmap

### Giai đoạn 1: Chuẩn hóa codebase & API hóa
- Refactor code, tách phần inference thành FastAPI service (giữ lại Streamlit UI nếu cần).
- Đảm bảo API trả về kết quả đúng, có test case kiểm thử.

### Giai đoạn 2: Đóng gói & CI/CD
- Viết Dockerfile cho FastAPI, Streamlit, model.
- Tạo docker-compose.yml để chạy local nhiều service (API, UI, Prometheus, Grafana, Jaeger).
- Viết Jenkinsfile cho CI/CD: tự động build, test, lint, build image, push image, deploy (local/k8s).

### Giai đoạn 3: Monitoring & Observability
- Tích hợp Prometheus (metrics FastAPI, resource usage).
- Tích hợp Grafana (dashboard theo dõi CPU, RAM, request, latency).
- Tích hợp Jaeger + OpenTelemetry (tracing request từ UI → API → model).

### Giai đoạn 4: Scaling & Cloud Native
- Viết manifest Kubernetes (hoặc Helm chart) để deploy API với 3 replicas.
- Deploy Prometheus + Grafana trên k8s bằng Helm.
- (Bonus) Deploy lên cloud (GCP, AWS, Azure, hoặc cloud free-tier).

### Giai đoạn 5: Báo cáo, sáng tạo, hoàn thiện
- Viết tài liệu, dashboard, changelog, hướng dẫn sử dụng, troubleshooting.
- (Bonus) Tích hợp thêm cloud function, autoscaling, cost monitoring, hoặc bất kỳ ý tưởng sáng tạo nào.

## 3. Thời gian biểu gợi ý (2-3 tuần)

| Tuần | Công việc chính |
|------|----------------|
| 1 | Refactor code, FastAPI, test, Dockerfile, docker-compose, Jenkinsfile, CI/CD local |
| 2 | Prometheus, Grafana, Jaeger, OpenTelemetry, hoàn thiện monitoring, logging, notification |
| 3 | Kubernetes, Helm, scaling, cloud, báo cáo, sáng tạo, polish, demo |

## 4. Công nghệ & tài nguyên gợi ý
- **Python:** FastAPI, Streamlit, pytest, flake8, black, isort, pre-commit.
- **Docker Compose:** Quản lý multi-service local.
- **Jenkins:** CI/CD (build, test, lint, build image, push image, deploy).
- **Prometheus:** metrics FastAPI (dùng prometheus_fastapi_instrumentator), resource node_exporter.
- **Grafana:** Dashboard resource, request, latency.
- **Jaeger + OpenTelemetry:** Tracing request, visualize flow.
- **Kubernetes + Helm:** Deploy API 3 replicas, Prometheus, Grafana.
- **Cloud:** GCP/AWS/Azure/Oracle Cloud Free Tier (bonus).
- **GitHub/GitLab:** Quản lý code, trigger Jenkins.

## 5. Phân tích chuyên sâu: Jenkins trong đồ án này
### CI/CD Pipeline:
- Lint, test, coverage: Đảm bảo code sạch, không bug trước khi build.
- Build Docker image: Tự động build image cho API, UI, model.
- Push image: Đẩy image lên DockerHub/GCR/ECR.
- Deploy: Tự động deploy lên local (docker-compose) hoặc k8s (kubectl/helm).
- Notification: Gửi email/Slack khi build thành công/thất bại.
- Artifact: Lưu log, model, metrics, changelog.
- Trigger: Tự động chạy pipeline khi có commit mới (webhook).
- Test automation: Tích hợp test API, test UI, test model.
- Security: Quản lý secret (API key, token) qua Jenkins Credential Store.
- Monitoring pipeline: Theo dõi pipeline, log, resource Jenkins agent.
- Scaling: Có thể tích hợp Jenkins agent trên k8s để build, test, deploy song song.

## 6. Ý tưởng mở rộng
- Autoscaling Jenkins agent trên k8s khi build nhiều job.
- Canary deployment: Deploy model mới cho 1 replica, kiểm thử trước khi rollout toàn bộ.
- Cost dashboard: Theo dõi chi phí cloud, resource usage.
- Model registry: Tích hợp MLflow/DVC cho versioning model.
- Observability: Full tracing từ UI → API → model → DB (nếu có).

## 7. Checklist hoàn thành đồ án
- [ ] FastAPI API trả về đúng kết quả, có test case.
- [ ] Docker Compose chạy đủ các service (API, UI, Prometheus, Grafana, Jaeger).
- [ ] Jenkinsfile CI/CD hoàn chỉnh, tự động build, test, deploy.
- [ ] Prometheus + Grafana theo dõi resource, request, latency.
- [ ] Jaeger tracing hoạt động, visualize flow.
- [ ] K8s deploy API 3 replicas, Prometheus + Grafana bằng Helm.
- [ ] Báo cáo, dashboard, changelog, tài liệu đầy đủ.
- [ ] Cloud, autoscaling, model registry, cost monitoring.

# Brainstorming & Phác thảo chiến lược đồ án MLOps: Qwen Coding Use Case

## 1. Mục tiêu tổng thể
- Biến ứng dụng Coding Multiple Choice QA (Qwen2.5-Coder-1.5B-Instruct) thành hệ thống MLOps production-ready.
- Tích hợp: FastAPI, Docker Compose, Prometheus, Grafana, Jaeger, Jenkins, Kubernetes, Helm, Cloud.

## 2. Chiến lược triển khai
### Giai đoạn 1: Chuẩn hóa codebase & API hóa
- Refactor code, tách inference thành FastAPI service.
- Đảm bảo API trả về đúng, có test case.

### Giai đoạn 2: Đóng gói & CI/CD
- Viết Dockerfile, docker-compose cho API, UI, monitoring.
- Viết Jenkinsfile: build, test, lint, build image, push image, deploy.

### Giai đoạn 3: Monitoring & Observability
- Tích hợp Prometheus, Grafana, Jaeger, OpenTelemetry.

### Giai đoạn 4: Scaling & Cloud Native
- Viết manifest K8s/Helm, deploy API 3 replicas, monitoring trên k8s.
- (Bonus) Deploy cloud.

### Giai đoạn 5: Báo cáo, sáng tạo, polish
- Viết tài liệu, dashboard, changelog, hướng dẫn sử dụng, troubleshooting.

## 3. Công nghệ & tài nguyên
- Python, FastAPI, Streamlit, pytest, flake8, Docker Compose, Jenkins, Prometheus, Grafana, Jaeger, K8s, Helm, Cloud, GitHub/GitLab.

## 4. Jenkins trong đồ án
- CI/CD: lint, test, build image, push, deploy, notification, artifact, security, monitoring pipeline, scaling agent.

## 5. Checklist hoàn thành
- [ ] FastAPI API đúng, test case đủ
- [ ] Docker Compose đủ service
- [ ] Jenkinsfile CI/CD hoàn chỉnh
- [ ] Prometheus + Grafana + Jaeger hoạt động
- [ ] K8s deploy 3 replicas, monitoring Helm
- [ ] Báo cáo, dashboard, changelog, tài liệu
- [ ] (Bonus) Cloud, autoscaling, model registry

---

*Bản phác thảo này là kim chỉ nam cho toàn bộ quá trình triển khai, giúp bám sát mục tiêu, công nghệ, checklist và chiến lược thực hiện đồ án MLOps hiện đại.*
