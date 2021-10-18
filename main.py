import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler

PATHTOBEOBSERVED = 'C:/Users/Anvar Kalykov/Desktop/check_file'


def on_created(event):
    s = event.src_path
    head, sep, tail = s.replace('C:/Users/Anvar Kalykov/Desktop/check_file\\', '').partition('_')
    print(head)



if __name__ == "__main__":

    patterns = "*"
    ignore_patterns = ""
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted


    path = PATHTOBEOBSERVED
    go_recursively = True

    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)

    my_observer.start()
    try:
        while True:
            time.sleep(0.3)
    except KeyboardInterrupt:
        my_observer.stop()
    my_observer.join()