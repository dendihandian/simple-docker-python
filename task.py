from datetime import datetime
import sys
import logging

if __name__ == "__main__":

    # NOTE: by default, logging only print warning, error, critical. we need to set level to DEBUG to see all logging in the logs.
    logging.basicConfig(filename='service.log', encoding='utf-8', level=logging.DEBUG)

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = 'Hello, this is an info.'

    sys.stdout.write(f"[{timestamp}] task.py sys.stdout.write - {message} (sys.stdout.write)")
    print(f"[{timestamp}] task.py PRINT - {message} (print)")
    logging.debug(f"[{timestamp}] task.py DEBUG - {message} (logging.debug)")
    logging.info(f"[{timestamp}] task.py INFO - {message} (logging.info)")
    logging.warning(f"[{timestamp}] task.py WARNING - {message} (logging.warning)")
    logging.error(f"[{timestamp}] task.py ERROR - {message} (logging.error)")
    logging.critical(f"[{timestamp}] task.py CRITICAL - {message} (logging.critical)")