import sys
from PyQt5.QtWidgets import *

#####ПРОЦЕДУРНАЯ ПАРАДИГМА######

#app = QApplication(sys.argv) #создаем приложение
#dlgMain = QWidget() #главное окно приложения
#dlgMain.setWindowTitle('Player GUI')
#dlgMain.show() #показываем главное окно

#app.exec_()  #запускаем приложение, здесь отслеживаются все события и вызываются соот. обработчики событий

#sys.exit(app.exec_())

#рефакторинг

#####ООП ПАРАДИГМА######

class DlgMain(QDialog):
    def __init__(self): #метод конструктора
        super().__init__() #вызываем конструктор класса родителя для всех необходимых инициализаций
        self.setWindowTitle('PlayMe') # добавляем виджеты и устанавливаем свойства
        self.resize(400, 200)

        self.ledText = QLineEdit('Default Text', self) 
        self.ledText.move(170, 50) #выставляем положение текстового поля

        self.btnUpdate = QPushButton('Update Window Title', self)  # собственно кнопка
        self.btnUpdate.move(90, 80)   #здесь надо выставлять положение кнопки на экране
        self.btnUpdate.clicked.connect(self.evt_btnupdate_clicked)

    def evt_btnupdate_clicked(self):
        self.setWindowTitle(self.ledText.text())
#проверяем, импортирован ли модуль, не используется ли он в другой программе
if __name__ == '__main__':     
    app = QApplication(sys.argv) #создаем приложение
    dlgMain = DlgMain() #создаем экземпляр класса DlgMain, который наследует от Qdialog
    dlgMain.show()  #показываем графический пользовательский интерфейс
    sys.exit(app.exec_()) # запускаем приложение

