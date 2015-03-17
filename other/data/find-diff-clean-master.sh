#!/bin/bash
diff <(zcat find-clean.gz | awk '{print $2}') <(zcat find-master.gz) | grep '^>' | awk '{print $2}'
