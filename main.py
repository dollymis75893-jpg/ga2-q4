from fastapi import FastAPI, HTTPException
import redis

app = FastAPI()

# Redis container se connect karna (host='redis' docker-compose service name hai)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.post("/hit/{key}")
def hit_counter(key: str):
    # INCR command atomically count badhata hai
    count = r.incr(key)
    return {"key": key, "count": count}

@app.get("/count/{key}")
def get_count(key: str):
    # Current count get karna, agar key nahi hai toh 0 return karna
    count = r.get(key)
    if count is None:
        count = 0
    return {"key": key, "count": int(count)}

@app.get("/healthz")
def health_check():
    try:
        # ping() se check karte hain ki Redis chal raha hai ya nahi
        r.ping()
        return {"status": "ok", "redis": "up"}
    except redis.ConnectionError:
        # Agar redis down hai toh error throw karein
        raise HTTPException(status_code=503, detail={"status": "error", "redis": "down"})
