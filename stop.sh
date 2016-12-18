#!/bin/bash
#uwsgi --stop /tmp/frozenbubble-master.pid
killall -s INT /usr/local/bin/uwsgi
killall -s INT uwsgi_python
