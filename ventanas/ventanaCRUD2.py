# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ventanaCRUD2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ventanaCrud2(object):
    def setupUi(self, ventanaCrud2):
        ventanaCrud2.setObjectName("ventanaCrud2")
        ventanaCrud2.resize(500, 450)
        ventanaCrud2.setMinimumSize(QtCore.QSize(500, 450))
        ventanaCrud2.setMaximumSize(QtCore.QSize(500, 450))
        font = QtGui.QFont()
        font.setPointSize(14)
        ventanaCrud2.setFont(font)
        self.gridLayout = QtWidgets.QGridLayout(ventanaCrud2)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.crearRegistro = QtWidgets.QPushButton(ventanaCrud2)
        self.crearRegistro.setMinimumSize(QtCore.QSize(250, 40))
        self.crearRegistro.setMaximumSize(QtCore.QSize(250, 40))
        self.crearRegistro.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.crearRegistro.setFont(font)
        self.crearRegistro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.crearRegistro.setObjectName("crearRegistro")
        self.horizontalLayout.addWidget(self.crearRegistro)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem2 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.editarRegistro = QtWidgets.QPushButton(ventanaCrud2)
        self.editarRegistro.setMinimumSize(QtCore.QSize(250, 40))
        self.editarRegistro.setMaximumSize(QtCore.QSize(250, 40))
        self.editarRegistro.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.editarRegistro.setFont(font)
        self.editarRegistro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.editarRegistro.setObjectName("editarRegistro")
        self.horizontalLayout_2.addWidget(self.editarRegistro)
        spacerItem3 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.verRegistro = QtWidgets.QPushButton(ventanaCrud2)
        self.verRegistro.setMinimumSize(QtCore.QSize(250, 40))
        self.verRegistro.setMaximumSize(QtCore.QSize(250, 40))
        self.verRegistro.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.verRegistro.setFont(font)
        self.verRegistro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.verRegistro.setObjectName("verRegistro")
        self.horizontalLayout_3.addWidget(self.verRegistro)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_4.setSpacing(10)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem6 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.borrarRegistro = QtWidgets.QPushButton(ventanaCrud2)
        self.borrarRegistro.setMinimumSize(QtCore.QSize(250, 40))
        self.borrarRegistro.setMaximumSize(QtCore.QSize(250, 40))
        self.borrarRegistro.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.borrarRegistro.setFont(font)
        self.borrarRegistro.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.borrarRegistro.setObjectName("borrarRegistro")
        self.horizontalLayout_4.addWidget(self.borrarRegistro)
        spacerItem7 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label = QtWidgets.QLabel(ventanaCrud2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(250, 40))
        self.label.setSizeIncrement(QtCore.QSize(0, 1))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_5.addWidget(self.label)
        self.comboCrear = QtWidgets.QComboBox(ventanaCrud2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboCrear.sizePolicy().hasHeightForWidth())
        self.comboCrear.setSizePolicy(sizePolicy)
        self.comboCrear.setMinimumSize(QtCore.QSize(100, 40))
        self.comboCrear.setSizeIncrement(QtCore.QSize(0, 10))
        self.comboCrear.setObjectName("comboCrear")
        self.horizontalLayout_5.addWidget(self.comboCrear)
        self.botonCrearMul = QtWidgets.QPushButton(ventanaCrud2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.botonCrearMul.sizePolicy().hasHeightForWidth())
        self.botonCrearMul.setSizePolicy(sizePolicy)
        self.botonCrearMul.setMinimumSize(QtCore.QSize(100, 40))
        self.botonCrearMul.setSizeIncrement(QtCore.QSize(0, 10))
        self.botonCrearMul.setObjectName("botonCrearMul")
        self.horizontalLayout_5.addWidget(self.botonCrearMul)
        self.gridLayout.addLayout(self.horizontalLayout_5, 4, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(ventanaCrud2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMinimumSize(QtCore.QSize(250, 40))
        self.label_2.setSizeIncrement(QtCore.QSize(0, 1))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        self.comboBorrar = QtWidgets.QComboBox(ventanaCrud2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBorrar.sizePolicy().hasHeightForWidth())
        self.comboBorrar.setSizePolicy(sizePolicy)
        self.comboBorrar.setMinimumSize(QtCore.QSize(100, 40))
        self.comboBorrar.setSizeIncrement(QtCore.QSize(0, 10))
        self.comboBorrar.setObjectName("comboBorrar")
        self.horizontalLayout_7.addWidget(self.comboBorrar)
        self.botonBorrarMul = QtWidgets.QPushButton(ventanaCrud2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(40)
        sizePolicy.setVerticalStretch(40)
        sizePolicy.setHeightForWidth(self.botonBorrarMul.sizePolicy().hasHeightForWidth())
        self.botonBorrarMul.setSizePolicy(sizePolicy)
        self.botonBorrarMul.setMinimumSize(QtCore.QSize(100, 40))
        self.botonBorrarMul.setSizeIncrement(QtCore.QSize(0, 10))
        self.botonBorrarMul.setObjectName("botonBorrarMul")
        self.horizontalLayout_7.addWidget(self.botonBorrarMul)
        self.gridLayout.addLayout(self.horizontalLayout_7, 5, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setContentsMargins(-1, 5, -1, 5)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem8 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.cancelar = QtWidgets.QPushButton(ventanaCrud2)
        self.cancelar.setMinimumSize(QtCore.QSize(250, 40))
        self.cancelar.setMaximumSize(QtCore.QSize(250, 40))
        self.cancelar.setSizeIncrement(QtCore.QSize(4, 4))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancelar.setFont(font)
        self.cancelar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelar.setObjectName("cancelar")
        self.horizontalLayout_6.addWidget(self.cancelar)
        spacerItem9 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.gridLayout.addLayout(self.horizontalLayout_6, 6, 0, 1, 1)

        self.retranslateUi(ventanaCrud2)
        QtCore.QMetaObject.connectSlotsByName(ventanaCrud2)

    def retranslateUi(self, ventanaCrud2):
        _translate = QtCore.QCoreApplication.translate
        ventanaCrud2.setWindowTitle(_translate("ventanaCrud2", "Ventana Crud Ampliada"))
        self.crearRegistro.setText(_translate("ventanaCrud2", "Crear un Registro Registro"))
        self.editarRegistro.setText(_translate("ventanaCrud2", "Editar un Registro Registro"))
        self.verRegistro.setText(_translate("ventanaCrud2", "Ver un Registro Registro"))
        self.borrarRegistro.setText(_translate("ventanaCrud2", "Borrar un Registro Registro"))
        self.label.setText(_translate("ventanaCrud2", "Crear Relación Multiple de"))
        self.botonCrearMul.setText(_translate("ventanaCrud2", "Crear"))
        self.label_2.setText(_translate("ventanaCrud2", "Borrar Relación Multiple de"))
        self.botonBorrarMul.setText(_translate("ventanaCrud2", "Borrar"))
        self.cancelar.setText(_translate("ventanaCrud2", "Cancelar"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ventanaCrud2 = QtWidgets.QDialog()
    ui = Ui_ventanaCrud2()
    ui.setupUi(ventanaCrud2)
    ventanaCrud2.show()
    sys.exit(app.exec_())

