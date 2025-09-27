# MoMo SMS Transactions API Documentation

## Authentication
All endpoints are protected with **Basic Authentication**.

- **Username:** `admin`  
- **Password:** `password123`  

If authentication fails, the server responds with:
```yaml
{"error": "Unauthorized"}
```

**HTTP Status:** `401 Unauthorized`

---

## Endpoints

### 1. Get All Transactions
**Method & URL**  
```bash
GET /transactions
```

**Example curl**
```bash
curl -u admin:password123 http://localhost:8000/transactions
```
### 2. Get Transaction by ID
**Method & URL**  
```bash
GET /transactions/{id}
```
Example curl
```bash
curl -u admin:password123 http://localhost:8000/transactions/1
```
### 3. Create New Transaction
**Method & URL** 
```bash
POST /transactions
```
Example curl

```bash
curl -u admin:password123 -X POST http://localhost:8000/transactions \
-H "Content-Type: application/json" \
-d '{...}'
```
### 4. Update Transaction by ID
**Method & URL**
```bash
PUT /transactions/{id}
```
Example curl

```bash
curl -u admin:password123 -X PUT http://localhost:8000/transactions/3 \
-H "Content-Type: application/json" \
-d '{...}'
```
### 5. Delete Transaction by ID
**Method & URL**
```bash
DELETE /transactions/{id}
```
Example curl

```bash
curl -u admin:password123 -X DELETE http://localhost:8000/transactions/3
```
### Error Codes Summary
- 401 Unauthorized → Missing or invalid credentials

- 404 Not Found → Transaction does not exist / Invalid endpoint

- 400 Bad Request → Malformed JSON in request body
