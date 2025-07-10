# Verificación de Entorno
import sys
assert sys.version_info >= (3, 10), "Se requiere Python 3.10+ (Quantum Edition)"
assert platform.machine() in ['quantum_x64', 'neutron_arm64'], "Arquitectura no soportada"
