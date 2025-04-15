# docs/README.md - Hướng dẫn sử dụng Qwen Coding Use Case MLOps

## 1. Giới thiệu
Hệ thống Coding Multiple Choice QA với Qwen2.5-Coder-1.5B-Instruct, FastAPI, Docker Compose, Prometheus, Grafana, Jaeger, Jenkins, Kubernetes, Helm, cloud-ready.

## 2. Chạy local với Docker Compose
```bash
docker-compose up --build
```
- Truy cập API: http://localhost:8000/docs
- Prometheus: http://localhost:9090
- Grafana: http://localhost:3000 (user/pass: admin/admin)
- Jaeger: http://localhost:16686

## 3. Test API
```bash
curl -X POST http://localhost:8000/predict -H 'Content-Type: application/json' \
  -d '{"question": "What is the output of print(1+1)?", "choices": ["1", "2", "3", "4"]}'
```

## 4. CI/CD với Jenkins
- Xem Jenkinsfile để biết pipeline build, test, lint, build image, push image, deploy.
- Cấu hình credential DockerHub, email notification.

## 5. Deploy Kubernetes
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
# Cài Prometheus, Grafana, Jaeger bằng Helm:
helm install -n monitoring -f k8s/prometheus.yaml prometheus prometheus-community/prometheus
helm install -n monitoring -f k8s/grafana.yaml grafana grafana/grafana
helm install -n monitoring -f k8s/jaeger.yaml jaeger jaegertracing/jaeger
```

## 6. Monitoring & Tracing
- Prometheus scrape metrics từ API, Grafana dashboard theo dõi request, latency, CPU, memory.
- Jaeger tracing request từ UI/API.

## 7. Troubleshooting
- Xem docs/troubleshooting.md

## 8. Changelog
- Xem docs/changelog.md

---

*Đồ án đáp ứng đầy đủ tiêu chí MLOps, CI/CD, monitoring, scaling, observability, cloud-ready.*
