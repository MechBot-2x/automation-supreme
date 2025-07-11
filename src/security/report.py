# Ejemplo de reporte mediante Quantum Encryption
from security_report import VulnerabilityReporter

reporter = VulnerabilityReporter(
    recipient="security@mechmind-dwv.quantum",
    encryption="quantum_aes-512",
    protocol="QSSP-v2"
)

report = reporter.create_report(
    vulnerability_type="temporal|quantum|dimensional",
    severity=0.0-1.0,
    proof_of_concept=True,
    suggested_fix=None
)
