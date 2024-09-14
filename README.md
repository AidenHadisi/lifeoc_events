# LifeOC Events

An easy wrapper around WP Events Calendar API to update events for lifeoc.org.

## Deploy It

```bash
gcloud functions deploy lifeoc-events
--gen2 \
--runtime=python312 \
--set-env-vars WP_USER=WP_USER, WP_PASS=WP_PASS, API_KEY=API_KEY \
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
        "title": "Test Event",
        "start_date": "2022-01-01T00:00:00",
        "end_date": "2022-01-01T23:59:59"
    }'
```
