# main.py - FastAPI app với metrics, tracing, healthcheck
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from prometheus_fastapi_instrumentator import Instrumentator
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry import trace
from opentelemetry.exporter.jaeger.thrift import JaegerExporter
from opentelemetry.sdk.resources import SERVICE_NAME, Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
import uvicorn
import model

app = FastAPI(title="Qwen Coding MCQ API", version="1.0")

# Prometheus metrics
Instrumentator().instrument(app).expose(app)

# OpenTelemetry + Jaeger tracing
trace.set_tracer_provider(
    TracerProvider(resource=Resource.create({SERVICE_NAME: "qwen-coding-api"}))
)
jaeger_exporter = JaegerExporter(
    agent_host_name="jaeger",
    agent_port=6831,
)
span_processor = BatchSpanProcessor(jaeger_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)
FastAPIInstrumentor.instrument_app(app)

@app.get("/healthz")
def health():
    return {"status": "ok"}

@app.post("/predict")
async def predict(request: Request):
    data = await request.json()
    question = data.get("question")
    choices = data.get("choices")
    # Gọi model inference (giả lập)
    answer = model.answer_mcq(question, choices)
    return {"answer": answer}

@app.exception_handler(Exception)
async def exception_handler(request, exc):
    return JSONResponse(status_code=500, content={"error": str(exc)})

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
