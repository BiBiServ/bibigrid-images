#!/bin/bash
diff <(zcat dpkg-clean.gz | awk '{print $2}') <(zcat dpkg-slave.gz | awk '{print $2}') | grep '^>' | awk '{print $2}'
