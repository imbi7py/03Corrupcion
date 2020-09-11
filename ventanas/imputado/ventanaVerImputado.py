# inicio ventanaVerImputado

from ventanas.imputado.ventanaEditarImputado import VentanaEditarImputado
from PyQt5 import QtWidgets
from ventanas.errorCampoModal import ErrorCampoModal
from ventanas.imputado.seleccionarImputados import SeleccionarImputados
from ventanas.clases.conectarMysql import ConectarMysql


class VentanaVerImputado(VentanaEditarImputado):
    '''
    Ventana para Ver un Imputado
    '''

    def __init__(self, identificador: int):
        super(VentanaVerImputado, self).__init__(identificador)
        self.setWindowTitle("Ver un Imputado")
        self.botonAceptar.setText("Aceptar")
        self.botonCancelar.setEnabled(False)
        self.botonResetear.setEnabled(False)
        self.inputNombre.setEnabled(False)
        self.inputApellidos.setEnabled(False)
        self.inputPartido.setEnabled(False)
        self.inputCargo.setEnabled(False)
        self.inputGrupoRH.setEnabled(False)
        self.inputFecha.setEnabled(False)
    # fin __init__

    def _accion(self):
        self.close()
# fin VentanaVerImputado


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication([])
        id = 1
        ventana = VentanaVerImputado(id)
        ventana.show()
        app.exec_()
        try:
            conexion = ConectarMysql.conectar()
            id = 1
            lista = SeleccionarImputados.obtenerImputado(conexion, id)
            conexion.close()
            if len(lista) == 0:
                raise ValueError
            print(lista)
            print(lista[0][1])
        except ValueError:
            ErrorCampoModal.errorNoRegistro(id)
        except ConnectionError:
            ErrorCampoModal.errorConexion()
    except ValueError:
        ErrorCampoModal.errorNoRegistro(id)
    except ConnectionError:
        ErrorCampoModal.errorConexion()
# fin if test

# fin ventanaVerImputado