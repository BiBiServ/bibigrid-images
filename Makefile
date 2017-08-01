SHELL := /bin/bash
.PHONY: pack
pack: clean
	@cat <(echo -n "GIT COMMIT: ") <(git log -1) <(echo -n " --- BUILD DATE: ") <(date) > VERSION
	@cat <(echo -e "#!/usr/bin/env python\n#          for python2.7") <(zip -qr - __main__.py bibigrid_image_creator apt-slave.txt apt-master.txt conf_default.php VERSION) > bibigrid-image && chmod +x bibigrid-image
	@rm -f VERSION
.PHONY: clean
clean:
	@rm -f bibigrid-image
.PHONY: run
run: pack
	@./bibigrid-image -h
