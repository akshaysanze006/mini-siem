class BaseRule:
    rule_id: str
    name: str
    mitre_technique: str
    severity: str

    def evaluate(self, event: dict) -> dict:
        raise NotImplementedError
