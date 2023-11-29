#!/bin/sh
script_dir="$(dirname "$(readlink -f "$0")")"

CZ_DIR="$script_dir" python3 "$script_dir/.get-machine-type.py"