#!/bin/bash
free -m | sed -n '2p' | awk '{print "  "$3/$2*100"%"}'
