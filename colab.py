#!/usr/bin/env python 

import argparse
from subprocess import call

parser = argparse.ArgumentParser(description='CoLab Startup')

# Add acceptable arguments and parse
parser.add_argument('-r', '--run', type=int, choices=[0, 1, 2],
                    help='set run type: 0=production, 1=development, 2=testing', default=0)
parser.add_argument('-d', '--detach', action='store_true', help='start docker in detached mode')
args = parser.parse_args()


# ---------------------------------
# Set up process for docker compose
# ---------------------------------
process_list = ["docker-compose", "-f", "docker-compose.yaml"]


# -----------------------------
# Select correct docker-compose
# -----------------------------
run_type = args.run
if run_type == 1:
    print("Running in development mode")
    development_flags = ["-f",  "docker-compose.development.yaml"]
    process_list.extend(development_flags)
elif run_type == 2:
    print("Running in testing mode")
else:
    print("Running in production mode")
    production_flags = ["-f",  "docker-compose.production.yaml"]
    process_list.extend(production_flags)

# ---------
# Up docker
# ---------
process_list.append("up")

# ---------------------------------------
# Add detached mode
# ---------------------------------------
detach_mode = args.detach
if detach_mode:
    process_list.append("-d")

# ----------------
# Run docker
# ----------------
print
call(process_list)
