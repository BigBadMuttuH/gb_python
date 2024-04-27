# отправлка запросов через curl
# в записывается в одну строчку

# curl -X 'POST' 'http://127.0.0.1:8000/items/'
# -H "accept: application/json"
# -H "Content-Type: application/json"
# -d '{"name": "Foo", "description": "A very nice Item", "price": 35.4, "tax": 3.2}'
# вывод
# {"name":"Foo","description":"A very nice Item","price":35.4,"tax":3.2}
# запрос
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42'
# -H "accept: application/json"
# -H "Content-Type: application/json"
# -d '{"name": "Foo", "description": "A very nice Item", "price": 35.4, "tax": 3.2}'
# {"item_id":42,"item":{"name":"Foo","description":"A very nice Item","price":35.4,"tax":3.2}}
# хороший запрос
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42'
# -H "accept: application/json"
# -H "Content-Type: application/json"
# -d '{"name": "NewName", "price": 60}'
# плохой запрос
# curl -X 'PUT' 'http://127.0.0.1:8000/items/42'
# -H "accept: application/json"
# -H "Content-Type: application/json"
# -d '{"name": "NewName", "tax": 60}'
# curl -X 'POST' \
#   'http://127.0.0.1:8000/items/' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#   "name": "string",
#   "description": "string",
#   "price": 0,
#   "tax": 0
# }'
