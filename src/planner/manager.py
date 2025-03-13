# Target flow
# Calls:   1                        2                                 3                                                              4                                              5
# Formulate search query  ->  Parse website    ->   Create plan, check if further research required    ->  Parse two additional sites with one target query -> Back to planner to create final installation plan


class Planner:

    def run(software: str):
        """Create plan to download and install the given software"""
