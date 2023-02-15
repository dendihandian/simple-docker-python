from datetime import datetime
import sys
import logging

if __name__ == "__main__":

    # NOTE: by default, logging only print warning, error, critical. we need to set level to DEBUG to see all logging in the logs.
    logging.basicConfig(filename='service.log', encoding='utf-8', level=logging.DEBUG)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = 'Hello, this is an info.'

    sys.stdout.write(f"[{timestamp}] task.py sys.stdout.write - Hello, this is python\'s sys.stdout.write() message")
    print(f"[{timestamp}] task.py PRINT - Hello, this is python's print() message")
    logging.debug(f"[{timestamp}] task.py DEBUG - Hello, this is a debug (logging.debug) message")
    logging.info(f"[{timestamp}] task.py INFO - Hello, this is an info (logging.info) message")
    logging.warning(f"[{timestamp}] task.py WARNING - Hello, this is a warning (logging.warning) message")
    logging.error(f"[{timestamp}] task.py ERROR - Hello, this is an error (logging.error) message")
    logging.critical(f"[{timestamp}] task.py CRITICAL - Hello, this is a critical (logging.critical) message")