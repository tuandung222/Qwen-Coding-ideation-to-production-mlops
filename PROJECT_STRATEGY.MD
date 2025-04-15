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
- Deploy lên cloud (GCP, AWS, Azure, hoặc cloud free-tier).

### Giai đoạn 5: Báo cáo, sáng tạo, hoàn thiện
- Viết tài liệu, dashboard, changelog, hướng dẫn sử dụng, troubleshooting.
- Tích hợp thêm cloud function, autoscaling, cost monitoring, hoặc bất kỳ ý tưởng sáng tạo nào.

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
