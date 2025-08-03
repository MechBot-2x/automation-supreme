# =============================================
# INTERFAZ DE OPERACIÓN
# =============================================

if __name__ == "__main__":
    # Ejemplo de uso básico
    singularity = DataSingularity(
        event_horizon="sqlite:///blackhole.db",
        compression_level=0.95
    )
    
    # Ingesta de datos
    sample_data = {
        "stellar_objects": ["quasar", "pulsar", "neutron_star"],
        "coordinates": [{"x": 12.5, "y": 42.3, "z": 88.8}],
        "energy_levels": [1e9, 1e12, 1e15]
    }
    
    data_id = singularity.ingest_data(sample_data)
    print(f"Datos absorbidos con ID: {data_id}")
    
    # Recuperación de datos
    recovered = singularity.retrieve_data(data_id)
    print("Datos recuperados:", recovered)
