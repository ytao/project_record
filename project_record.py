from PyQt4 import QtCore,QtGui
import sys
import string
import datetime
import m
import sys, os,time
import edit_excel


if __name__=='__main__':

	# 建立窗口
	app=QtGui.QApplication(sys.argv)
	a=m.Ui_Dialog()

	# 初始化并读取数据
	mdata=edit_excel.project_data()
	if mdata.init_success==False:
		msg_box = QtGui.QMessageBox(QtGui.QMessageBox.Critical, "错误！", "未在可执行文件目录下找到aaa.xlsx，程序将退出!")
		msg_box.show()
		sys.exit(app.exec_())

	mdata.read_all()


	# 回调函数
	def on_read_record():
		mstr=a.cb_record_name.currentText()
		mdata.read_record(mstr)
		a.cb_record_state.setEditText(mdata.record_state)
		a.de_record_date.setDate(datetime.datetime.strptime(mdata.record_date,'%Y-%m-%d'))

	def on_write_record():
		temp_a=str(a.cb_record_name.currentText())
		temp_b=str(a.cb_record_state.currentText())
		temp_date=a.de_record_date.date()
		mdata.write_record(temp_a,temp_b,str(temp_date.toPyDate()))

	def on_record_today():
		a.de_record_date.setDate(QtCore.QDate.currentDate())

	for i in range(0,len(mdata.project_names)):
		a.cb_record_name.addItem(mdata.project_names[i])
	for i in range(0,len(mdata.project_states)):
		a.cb_record_state.addItem(mdata.project_states[i])

	a.cb_record_state.setEditText(mdata.record_state)
	a.de_record_date.setDate(datetime.datetime.strptime(mdata.record_date,'%Y-%m-%d'))
	a.setWindowTitle('打开的文件：'+mdata.filename)

	# 信号绑定
	a.cb_record_name.editTextChanged.connect(on_read_record)
	a.btnRecordToday.clicked.connect(on_record_today)
	a.buttonBox.accepted.connect(on_write_record)


	# 开始显示
	a.show();
	sys.exit(app.exec_())
