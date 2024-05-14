import json
from datetime import datetime

class LogQueryInterface:
    def __init__(self, log_files):
        self.log_files = log_files

    def search_logs(self, level=None, log_string=None, timestamp=None, source=None):
        logs = []
        for log_file in self.log_files:
            with open(log_file, 'r') as file:
                for line in file:
                    log = json.loads(line)
                    if (level is None or log['level'] == level) and \
                       (log_string is None or log['log string'] == log_string) and \
                       (timestamp is None or log['timestamp'] == timestamp) and \
                       (source is None or log['metadata']['source'] == source):
                        logs.append(log)
        return logs

# Example usage
query_interface = LogQueryInterface(['log1.log', 'log2.log'])
results = query_interface.search_logs(level='ERROR')
for result in results:
    print(result)
