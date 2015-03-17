#!/usr/bin/env python
from sys import stdin
from  subprocess import check_output

GET_DEPS="apt-cache --no-recommends --no-suggests --no-conflicts --no-breaks --no-replaces --no-enhances depends {0} 2>/dev/null | awk '{{print $4}}'"

pkgs = []
for line in stdin:
    line = line .strip()
    if line:
        pkgs.append(line)

#Pakete mit Abhaengigkeiten innerhalb der Eingabeliste. Tupel: (pkg, [deps])
pkgDeps = filter(lambda (p,q): q, [(pkg, filter(lambda p: p in pkgs, filter(None, check_output(GET_DEPS.format(pkg), shell=True).split('\n')))) for pkg in pkgs])

#Pakete die selbst keine Abhaengkeit darstellen und daher installiert werden muessen
for (a,b) in pkgDeps:
    isRootPkg = True
    for(c,d) in pkgDeps:
        if a in d:
            isRootPkg = False
    if isRootPkg:
        print a
