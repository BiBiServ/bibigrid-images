#!/bin/bash
diff <(zcat find-clean.gz | awk '{print $2}') <(zcat find-slave.gz) | grep '^>' | awk '{print $2}'
