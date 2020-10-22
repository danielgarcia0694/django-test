# Como consumir el endpoint utilizando un curl.

### GET api/products/

```bash
curl -i -H "Accept: application/json" -H "Content-Type: application/json" -X GET http://localhost:8000/api/products/
```

### POST /api/products/bulk_insert/

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"products":[{"id":1,"name":"Sopa","value":99.90,"discount_value":29.90,"stock": 10}]}' \
  http://localhost:8000/api/products/bulk_insert/
```
