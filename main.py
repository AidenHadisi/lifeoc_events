import os
from typing import TypedDict

import requests
import requests.auth
from dotenv import load_dotenv
from flask import Request
from functions_framework import http

load_dotenv()

URL = "https://cms.lifeoc.org/wp-json/tribe/events/v1/events"
WP_USER = os.getenv("WP_USER", "admin")
WP_PASS = os.getenv("WP_PASS", "password")
API_KEY = os.getenv("API_KEY", "test")


class Event(TypedDict):
    title: str
    start_date: str
    end_date: str


@http
def handle(request: Request) -> tuple[dict, int]:
    # Only allow POST requests
    if request.method != "POST":
        return {"error": "Method Not Allowed"}, 405

    # Check if the request has a valid API key
    if request.headers.get("x-api-key") != API_KEY:
        return {"error": "Unauthorized"}, 401

    # Get the request body as Event
    event: Event | None = request.get_json(silent=True)
    if not event or not is_valid_event(event):
        return {"error": "Invalid event"}, 400

    # Create the event in the WordPress site
    try:
        add_event(event)
    except Exception as e:
        return {"error": str(e)}, 500

    return {"message": "Event added successfully"}, 200


def is_valid_event(event: Event) -> bool:
    """Check if the event has a title, start_date, and end_date"""
    return (
        "title" in event
        and "start_date" in event
        and "end_date" in event
        and bool(event["title"] and event["start_date"] and event["end_date"])
    )


def add_event(event: Event) -> None:
    """Add an event to the WordPress site.

    Args:
        event (Event): The event to add.
    """

    response = requests.post(
        URL, json=event, auth=requests.auth.HTTPBasicAuth(WP_USER, WP_PASS)
    )
    match response.status_code:
        case 201:
            return
        case _:
            raise Exception(f"Failed to add event: {response.text}")
