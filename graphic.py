from PyQt5.QtWidgets import QApplication, QLabel, QRadioButton, QWidget, QPushButton, QVBoxLayout, QMessageBox, \
    QLineEdit, QTextEdit
from main import createBF, createBR, satBF


def chooseFile():
    if (radio1.isChecked()):
        fileBF = r"BFMETEOROLOGIES.txt"
        fileBR = r"BRMETEOROLOGIES.txt"
    if (radio2.isChecked()):
        fileBF = r"BFVILLES.txt"
        fileBR = r"BRVILLES.txt"
    if (radio3.isChecked()):
        fileBF = r"BFMALADIES.txt"
        fileBR = r"BRMALADIES.txt"
    return fileBF, fileBR


def on_button_clicked():
    if (radio1.isChecked() or radio2.isChecked() or radio3.isChecked()):
        (fileBF, fileBR) = chooseFile()
        bf = createBF(fileBF)
        br = createBR(fileBR)
        (x, y) = satBF(bf, br)
        param = textbox.text()
        logOutput.clear()
        if param in x.keys():
            logOutput.insertPlainText(str(x[param]))
        else:
            logOutput.insertPlainText("Pas de résultat correspondant")
    else:
        logOutput.insertPlainText("please choose a file")


def on_button_clicked2():
    if (radio1.isChecked() or radio2.isChecked() or radio3.isChecked()):
        (fileBF, fileBR) = chooseFile()
        bf = createBF(fileBF)
        br = createBR(fileBR)
        (x, y) = satBF(bf, br)
        logOutput.clear()
        logOutput.insertPlainText(str(x))
    else:
        logOutput.clear()
        logOutput.insertPlainText("please choose a file")


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()
radio1 = QRadioButton('météorologies')
radio2 = QRadioButton('villes')
radio3 = QRadioButton('maladies')
button1 = QPushButton('recherche')
button1.clicked.connect(on_button_clicked)
button2 = QPushButton('saturer la base de faits')
button2.clicked.connect(on_button_clicked2)
textbox = QLineEdit()
logOutput = QTextEdit()
logOutput.setReadOnly(True)
layout.addWidget(radio1)
layout.addWidget(radio2)
layout.addWidget(radio3)
layout.addWidget(textbox)
layout.addWidget(button1)
layout.addWidget(button2)
layout.addWidget(logOutput)
window.setLayout(layout)
window.show()
app.exec_()
