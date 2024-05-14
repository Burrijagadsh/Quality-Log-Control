import logging

class LogIngestor:
    def __init__(self, log_files):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        self.loggers = {file: logging.getLogger(file) for file in log_files}

    def log(self, level, log_string, source):
        if source in self.loggers:
            self.loggers[source].log(level, log_string)

# Example usage
ingestor = LogIngestor(['log1.log', 'log2.log'])
ingestor.log(logging.INFO, 'Inside the Search API', 'log1.log')
ingestor.log(logging.ERROR, 'Failed to connect to the database', 'log2.log')
