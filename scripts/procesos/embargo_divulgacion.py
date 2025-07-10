## POLÍTICA DE DIVULGACIÓN
### Embargo Temporal
- **Duración**: 30 días terrestres
- **Condiciones**:
  - Vulnerabilidades con severidad >0.7
  - Afecta múltiples dimensiones
  - Requiere coordinación interestelar

### Divulgación Pública
```mermaid
graph LR
  A[Reporte] --> B{Severidad}
  B -->|>0.9| C[Divulgación Inmediata]
  B -->|0.7-0.9| D[Embargo 30 días]
  B -->|<0.7| E[Divulgación en Notas de Versión]
```
