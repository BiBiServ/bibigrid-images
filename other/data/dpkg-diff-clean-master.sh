#!/bin/bash
diff <(zcat dpkg-clean.gz | awk '{print $2}') <(zcat dpkg-master.gz | awk '{print $2}') | grep '^>' | awk '{print $2}'
