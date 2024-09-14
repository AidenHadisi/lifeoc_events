# LifeOC Events

An easy wrapper around WP Events Calendar API to update events for lifeoc.org.

## Deploy It

```bash
gcloud functions deploy lifeoc-events
--gen2 \
--runtime=python312 \
--region=us-central1 \
--source=. \
--entry-point=handle \
--trigger-http
```

## Use it

```bash
curl https://us-central1-life-church-303612.cloudfunctions.net/lifeoc-events \
    -X POST \
    -H "Content-Type: application/json" \
    -H "x-api-key: API_KEY" \
    -d '{
        "title": "Sunday Service",
        "start_date": "2024-10-06 10:15:00"
        "end_date": "2024-10-06 10:15:00"
    }'
```
