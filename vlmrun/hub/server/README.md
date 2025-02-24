### 🌐 Server Usage

The hub includes a FastAPI server for easy access to schemas:

```bash
# Install with server dependencies
pip install "vlmrun-hub[server]"

# Run the server
uvicorn vlmrun.hub.server.app:app --reload
```

Access the API:
```python
import requests

# Get hub info
response = requests.get("http://localhost:8000/info")
print(response.json())

# List all domains
response = requests.get("http://localhost:8000/domains")
print(response.json())

# Get schema for specific domain
response = requests.post(
    "http://localhost:8000/schema",
    json={"domain": "document.invoice"}
)
print(response.json())
```

API documentation is available at http://localhost:8000/docs
