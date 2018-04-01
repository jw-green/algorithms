class FileManager:
    def __init__(self):
        self.queue = []

    def addFile(self, filename):
            self.queue.append(filename)

    def closeAllFiles(self):
        for open_file in self.queue:
            open_file.close()
            self.queue.remove(open_file)
