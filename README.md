# LifeOC Events

An easy wrapper around WP Events Calendar API to update events for lifeoc.org.

## Deploy

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
