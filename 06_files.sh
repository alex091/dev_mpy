#!/usr/bin/env bash

USER=$(whoami)
find . -user ${USER} -mtime -7 -printf "%T+\t%p\n" | sort