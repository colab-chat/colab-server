#!/usr/bin/env python 

import argparse
from subprocess import call

parser = argparse.ArgumentParser(description='CoLab Startup')

# Add acceptable arguments
parser.add_argument('-r', '--run',type=int, choices=[0, 1, 2], help='set run type: 0=production, 1=development, 2=testing', default=0)
parser.add_argument('-d', '--detach', action='store_true', help='start docker in detached mode')


# Get the arguments
args = parser.parse_args()

# -------------------------------------------
# Act on the arguments
# ------------------------------------------

# Check if we should run in detached mode
detach_mode = args.detach
detach_mode_specifier = "-d" if detach_mode else ""

# Set up sub system call
run_type = args.run
if run_type == 1:
  print("Running in development mode")
  call(["docker-compose", "-f", "docker-compose.yaml", "-f", "docker-compose.development.yaml", "up", detach_mode_specifier])
elif run_type == 2:
  print("Running in testing mode")
else:
  print("Running in production mode")
  call(["docker-compose", "-f", "docker-compose.yaml", "-f", "docker-compose.production.yaml", "up", detach_mode_specifier])

