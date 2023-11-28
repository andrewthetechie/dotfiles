#!/bin/sh
script_dir="$(dirname "$(readlink -f "$0")")"

python3 "$script_dir/.get-machine-type.py"