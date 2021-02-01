import pync
import os

def enviar_notificacion(mensaje):
    pync.notify(mensaje, group=os.getpid())
