## PROTOCOLOS DE USO

### 1. Inicialización del Clasificador
```python
# Configuración para eventos de alta energía
classifier = CosmicClassifier(
    input_shape=(512, 512, 4),  # Formato de entrada
    num_classes=24,             # Tipos de eventos cósmicos
    quantum_bits=12             # Mayor precisión cuántica
)
```

### 2. Clasificación de Eventos
```python
# Carga de evento cósmico (formato: HWC)
event_data = np.load('cosmic_event.npy')  

# Predicción de categoría
class_id, confidence = classifier.predict_event(event_data)
print(f"Evento clasificado como {class_id} con confianza {confidence:.2f}")
```

### 3. Explicación de Predicciones
```python
# Mapa de atención cuántica
attention_map = classifier.explain_prediction(event_data)
plt.imshow(attention_map[0, :, :, 0])
plt.title('Regiones de interés cuántico')
```
