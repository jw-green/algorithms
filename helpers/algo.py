class Algo:
    def __init__(self, name, algo_type, details_path, languages):
        self.name = name
        self.algo_type = algo_type
        self.details_path = details_path
        self.languages = languages

    def __str__(self):
        return "Name: %s\nType: %s\nDetails: %s\nLanguages: %s" % (self.name, 
                                                                   self.algo_type, 
                                                                   self.details_path, 
                                                                   self.languages)

    def set_name(self, value):
        self.name = value

    def set_algo_type(self, value):
        self.algo_type = value

    def set_details_path(self, value):
        self.details_path = value

    def set_languages(self, value):
        self.languages = value


