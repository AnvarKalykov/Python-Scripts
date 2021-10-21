import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

import psycopg2
from psycopg2 import Error


PATHTOBEOBSERVED = 'C:/Users/Anvar Kalykov/Desktop/check_file'


def on_created(event):
    s = event.src_path
    head, sep, tail = s.replace('C:/Users/Anvar Kalykov/Desktop/check_file\\', '').partition('_')
    print(head)

    try:
        connection = psycopg2.connect(user="postgres", password=12345678, host="127.0.0.1", port=5432, database="postgres")
        cursor = connection.cursor()
        cursor.execute("SELECT name, surename FROM mobile WHERE number='+" + head + "';")
        rows = cursor.fetchall()
        for row in rows:
            print(row[0], row[1])
    except Error as e:
        print(f"The error '{e}' occurred")

        connection.close()





if __name__ == "__main__":

    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created


    path = PATHTOBEOBSERVED
    go_recursively = True

    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
    my_observer.join()