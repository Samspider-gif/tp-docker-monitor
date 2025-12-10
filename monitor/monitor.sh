#!/bin/sh
echo "--- Monitoring demarre ---"
# Lit le fichier en continu
tail -f /logs/api.log
