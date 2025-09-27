
## Local Ollama Endpoint (1 mark)

### 1️⃣ Install Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

---

### 2️⃣ Run Ollama server with CORS enabled

```bash
export OLLAMA_ORIGINS="*"
ollama serve
```

* `OLLAMA_ORIGINS="*"` allows **all origins** to access your server.
* Make sure Ollama is **stopped and restarted** if it was running before setting this variable.

---

### 3️⃣ Run ngrok with custom headers for CORS and bypassing browser warning

```bash
ngrok http 11434 \
  --response-header-add "X-Email: 23f3004197@ds.study.iitm.ac.in" \
  --response-header-add "Access-Control-Expose-Headers: *" \
  --response-header-add "Access-Control-Allow-Headers: Ngrok-skip-browser-warning" \
  --host-header=localhost
```

#### Explanation of ngrok options

1. **`ngrok http 11434`**

   * Exposes your local Ollama server on port `11434` to a public URL.
   * Anyone with the ngrok URL can access your server (CORS rules still apply).

2. **`--response-header-add "X-Email: ..."`**

   * Adds a custom header `X-Email` to all responses.
   * Useful for debugging, tracking, or verifying requests from the frontend.

3. **`--response-header-add "Access-Control-Expose-Headers: *"`**

   * Allows JavaScript (e.g., `fetch`) to read **all headers** in cross-origin responses.
   * Without this, only default headers like `Content-Type` are accessible.

4. **`--response-header-add "Access-Control-Allow-Headers: Ngrok-skip-browser-warning"`**

   * Lets browsers send the custom `Ngrok-skip-browser-warning` header in requests.
   * Needed to bypass ngrok’s browser warning page.
   * Prevents CORS errors in your web app.

5. **`--host-header=localhost`**

   * Rewrites the `Host` header sent to your local server as `localhost`.
   * Ensures Ollama sees requests as coming from a local origin.
   * Avoids `403 Forbidden` errors when requests come through ngrok.

---

✅ **Notes / Tips**

* If Ollama is already running on `11434`, stop it first:

```bash
systemctl stop ollama
ollama serve
```

---
