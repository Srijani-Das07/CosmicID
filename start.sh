#!/bin/bash
gunicorn app_api:app --bind 0.0.0.0:$PORT