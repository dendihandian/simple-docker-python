from datetime import datetime
import sys
import logging

if __name__ == "__main__":

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = 'Hello, this is an info.'

    sys.stdout.write(f"[{timestamp}] task.py sys.stdout.write - {message} (sys.stdout.write)\n")
    print(f"[{timestamp}] task.py PRINT - {message} (print)\n")
    logging.debug(f"[{timestamp}] task.py DEBUG - {message} (logging.debug)\n")
    logging.info(f"[{timestamp}] task.py INFO - {message} (logging.info)\n")
    logging.warning(f"[{timestamp}] task.py WARNING - {message} (logging.warning)\n")
    logging.error(f"[{timestamp}] task.py ERROR - {message} (logging.error)\n")
    logging.critical(f"[{timestamp}] task.py CRITICAL - {message} (logging.critical)\n")