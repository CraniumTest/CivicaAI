from my_legal_library import LegalAnalyzer

class AnalysisModule:

    def __init__(self, legal_database):
        self.analyzer = LegalAnalyzer(legal_database)

    def cross_reference(self, new_bill):
        conflicts = self.analyzer.check_conflicts(new_bill)
        return conflicts
