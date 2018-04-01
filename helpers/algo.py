class Algo:
    def __init__(self, name, algo_type, details_path, languages):
        self.name = name
        self.algo_type = algo_type
        self.details_path = details_path
        self.languages = languages

    def __str__(self):
        return "Name: %s\nType: %s\nDetails: %s\nLanguages: %s\n" % (self.name,
                                                                     self.algo_type,
                                                                     self.details_path,
                                                                     self.languages)

    def setName(self, value):
        self.name = value

    def setAlgoType(self, value):
        self.algo_type = value

    def setDetailsPath(self, value):
        self.details_path = value

    def setLanguages(self, value):
        self.languages = value
