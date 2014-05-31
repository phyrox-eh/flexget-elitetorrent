flexget-elitetorrent
====================

This plugin enables the flexget discovery search in elitetorrent. 
This is a test and it is meant to learn how to develop in Python using GIT, and it doesn't encourage piracy.

How to use
====================
Add this single file in the following folder: ~/.flexget/plugins/
Then you can setup your config.yml file using the "ET" search engine in your tasks.

Example of usage:


discover:
	what:
	- emit_series:
		from_start: yes
	from:
		- ET: ok

This will search your series in elitetorrent. 

NOTE
==================
The series name MUST be in Spanish, so be sure that you can search files in the website
