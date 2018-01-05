#!/bin/bash

export SARRI_DEV=1
gunicorn main:app
