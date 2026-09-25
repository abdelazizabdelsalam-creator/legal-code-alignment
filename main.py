import json
from src.formal_mapper import FormalMapper

if __name__ == "__main__":
    print("[INFO] Initializing Legal-Code Alignment Pipeline Execution...")
    
    mock_ontology = {
        "data_assets": {"credit_card_data": {"classification": "PCI-DSS High-Risk"}},
        "infrastructure": {"network_protocols": ["HTTPS", "TLS-1.2"]}
    }
    
    mapper = FormalMapper(mock_ontology)
    results = mapper.compile_to_formal_specs()
    
    print("=== EXTRACTED VERIFIABLE FORMAL SPECIFICATIONS ===")
    print(json.dumps(results, indent=4))
