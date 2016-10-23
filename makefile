#这些是需要每个项目都独立写一个的
#-------------------
main_name=project_record
ui_name=m
sys=linux


#后面就是不用独立修改的
#-------------------
ifeq ($(sys),win)
	py=d:\pf\python34\python.exe
	uic=D:\pf\Python34\Lib\site-packages\PyQt4\uic\pyuic.py
	ui_editor=D:\pf\Python34\Lib\site-packages\PyQt4\designer.exe
	rm_bin=del
	packer=d:\pf\python34\Scripts\cxfreeze
else
	py=python3
	uic=/usr/lib/python3/dist-packages/PyQt4/uic/pyuic.py
	ui_editor=designer
	rm_bin=rm
endif


run : $(ui_name).py $(main_name).py
	$(py) $(main_name).py

$(ui_name).py	:	$(ui_name).ui
	$(py) $(uic) $(ui_name).ui -o $(ui_name).py
	$(py) replace_str.py $(ui_name).py

e	: $(ui_name).ui $(ui_name).py
	$(ui_editor) $(ui_name).ui

c	:
	$(rm_bin) $(ui_name).py
	$(rm_bin) __pycache__ -r

t	:
	$(py) replace_str.py $(ui_name).py

out:
	$(py) $(packer) --icon=$(main_name).ico $(main_name).py --base-name=Win32GUI

out2:
	$(py) setup.py bdist_msi --icon=$(main_name).ico
