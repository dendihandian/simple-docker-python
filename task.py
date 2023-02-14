from datetime import datetime
import sys

if __name__ == "__main__":

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = 'INFO'
    message = 'Hello, this is an info.'

    sys.stdout.write(f"[{timestamp}] {{__name__}} {level} - {message}")