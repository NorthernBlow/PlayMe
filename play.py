import sys
from PyQt5.QtWidgets import *

#app = QApplication(sys.argv) #создаем приложение
#dlgMain = QWidget() #главное окно приложения
#dlgMain.setWindowTitle('Player GUI')
#dlgMain.show() #показываем главное окно

#app.exec_()  #запускаем приложение, здесь отслеживаются все события и вызываются соот. обработчики событий

#sys.exit(app.exec_())

class DlgMain(QDialog):
	def __init__(self):
		super().__init__()
		self.setWindowTitle('PlayMe') # добавляем виджет со свойствами

#проверяем, импортирован ли модуль, не используется ли он в другой программе
if __name__ == '__main__':     
	app = QApplication(sys.argv) #создаем приложение
	dlgMain = DlgMain() #создаем экземпляр класса DlgMain, который наследует от Qdialog
	dlgMain.show()  #показываем графический пользовательский интерфейс
	sys.exit(app.exec_()) # запускаем приложение

