#!/bin/bash
cd /app && exec daphne -b 0.0.0.0 -p 8000 example_project.asgi:channel_layer
