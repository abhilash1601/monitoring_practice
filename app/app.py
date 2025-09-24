from flask import Flask, Response, request, jsonify
from prometheus_client import Counter, Gauge, Histogram, generate_latest, CONTENT_TYPE_LATEST
import time, random, os

app = Flask(__name__)

ORDER_COUNTER = Counter('order_created_total', 'Total orders created')
ORDER_PROCESSING_SECONDS = Histogram('order_processing_seconds', 'Order processing time seconds',
                                     buckets=[0.001, 0.01, 0.05, 0.1, 0.5, 1, 2])
ORDERS_INPROGRESS = Gauge('order_inprogress', 'Orders currently being processed')

@app.route('/')
def index():
    return "demo-python service"

@app.route('/health')
def health():
    return "ok", 200

@app.route('/orders', methods=['POST'])
def create_order():
    ORDERS_INPROGRESS.inc()
    start = time.time()
    simulated = float(request.args.get('delay', random.uniform(0.01, 0.15)))
    time.sleep(simulated)
    elapsed = time.time() - start
    ORDER_PROCESSING_SECONDS.observe(elapsed)
    ORDER_COUNTER.inc()
    ORDERS_INPROGRESS.dec()
    return jsonify({"status": "created", "processing_seconds": round(elapsed, 3)}), 201

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, threaded=True)
