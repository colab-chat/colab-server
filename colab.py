#!/usr/bin/env python 

import argparse
from subprocess import call

parser = argparse.ArgumentParser(description='CoLab Startup')

# Add acceptable arguments and parse
parser.add_argument('-r', '--run', type=int, choices=[0, 1, 2],
                    help='set run type: 0=production, 1=development, 2=testing', default=0)
parser.add_argument('-d', '--detach', action='store_true', help='start docker in detached mode')
parser.add_argument('-s', '--stop', action='store_true', help='stop docker containers')
parser.add_argument('-b', '--build', action='store_true', help='build docker containers')
args = parser.parse_args()



# -------------------------------
# Check if colab is to be stopped
# ------------------------------
if args.stop:
  # TODO need to check if other commands have been set
  process_list = ["docker-compose", "stop"]
elif args.build:
  # TODO need to check if other commands have been set
  process_list = ["docker-compose", "build"]
else:
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
call(process_list)

