#!/bin/bash

docker run -p 8000:8000 -v $(pwd):/playground django python /playground/manage.py runserver 0.0.0.0:8000
