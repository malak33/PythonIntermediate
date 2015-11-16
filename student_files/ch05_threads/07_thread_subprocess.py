import threading
import subprocess

external_process_cmd = r'dir c:\temp'

class ExternalCommandThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.stdout = None
        self.stderr = None

    def run(self):
        p = subprocess.Popen(external_process_cmd.split(),
                             shell=True,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE)

        self.stdout, self.stderr = p.communicate()

extCmd = ExternalCommandThread()
extCmd.start()
extCmd.join()
print(extCmd.stdout.decode())