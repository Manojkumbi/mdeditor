import time
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
from datetime import datetime 

class GitAutoHandler(FileSystemEventHandler):
    def __init__(self):
        self.commit_counter = 1
        self.last_trigger_time = 0
        self.cooldown = 2

    def on_modified(self, event):
        current_time = time.time()
        if current_time - self.last_trigger_time < self.cooldown:
            return
        
        self.last_trigger_time = current_time
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"\n[{current_datetime}] Changes detected! Processing git operations...")
        
        try:
            # Execute git commands with output capture
            add_result = subprocess.run(['git', 'add', '.'], 
                                     capture_output=True, text=True)
            if add_result.returncode != 0:
                raise Exception(f"Git add failed: {add_result.stderr}")
            print(f"Git add status: {add_result.stdout or 'Success'}")
            
            commit_result = subprocess.run(['git', 'commit', '-m', f'test {self.commit_counter} of commit'], 
                                        capture_output=True, text=True)
            if commit_result.returncode != 0:
                raise Exception(f"Git commit failed: {commit_result.stderr}")
            print(f"Git commit status: {commit_result.stdout or 'Success'}")
            
            push_result = subprocess.run(['git', 'push'], 
                                      capture_output=True, text=True)
            if push_result.returncode != 0:
                raise Exception(f"Git push failed: {push_result.stderr}")
            print(f"Git push status: {push_result.stdout or 'Success'}")
            
            self.commit_counter += 1
            print(f"[{current_datetime}] Git operations completed successfully!")
            
        except Exception as e:
            print(f"[{current_datetime}] Error: {str(e)}")

def main():
    watch_path = r"c:\Users\SPKR\projects\mdroutine"
    os.chdir(watch_path)  # Set working directory
    
    event_handler = GitAutoHandler()
    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=True)
    observer.start()

    print("\nMonitoring directory for changes...")
    print("Press Ctrl+C to stop monitoring\n")
    
    try:
        while True:
            print(".", end="", flush=True)
            time.sleep(2)
    except KeyboardInterrupt:
        observer.stop()
        print("\nMonitoring stopped.")
    
    observer.join()

if __name__ == "__main__":
    main() 