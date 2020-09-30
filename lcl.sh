#!/bin/bash
if [ $# -eq 0 ]
  then
    python -m core.shell
else
    python main.py $@
fi
