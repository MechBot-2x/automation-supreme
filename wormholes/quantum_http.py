# Configuración avanzada
folder = APIFolder(
    max_folds=7,               # Máximo de dobleces
    quantum_entanglement=True, # Entrelazamiento cuántico
    temporal_compression=0.5   # Mayor compresión
)

# Agregar rutas personalizadas
folder.add_route('/custom', handle_custom_request)

# Iniciar servidor
folder.run_server(port=8080)
