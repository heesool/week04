#!/usr/bin/env bash

set -euo pipefail

mkdir -p backup
tar -czf backup/source.tar.gz source
sha256sum backup/source.tar.gz > backup/source.tar.gz.sha256

echo "Backup created successfully."
