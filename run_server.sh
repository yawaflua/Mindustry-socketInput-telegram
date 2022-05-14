#!/usr/bin/env bash
gnome-terminal --command="python3 main.py"
echo "config socketInput true" | java  -jar server.jar  
