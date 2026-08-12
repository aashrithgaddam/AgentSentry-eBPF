import time
import psutil

print("--- SentinelFabric: Pure Python OS Process Monitor Active ---")
print("[+] Initializing real-time process lifecycle tracker...")

def watch_system_processes():
    print("[+] System Tracker: ONLINE. Watching for unauthorized breakouts...\n")
    
    # Track processes that are already running when we start
    known_pids = set(psutil.pids())
    
    try:
        while True:
            current_pids = set(psutil.pids())
            # Find any brand new processes that just spawned
            new_pids = current_pids - known_pids
            
            for pid in new_pids:
                try:
                    proc = psutil.Process(pid)
                    proc_name = proc.name().lower()
                    cmd_line = " ".join(proc.cmdline())
                    
                    # Log the process event to the terminal
                    if cmd_line:
                        print(f"[PROCESS_EVENT] PID {pid} [{proc_name}] executed: {cmd_line}")
                        
                        # Active Defensive Filter: Catch an AI agent breakout attempt
                        if "cat" in proc_name and "shadow" in cmd_line:
                            print(f"    └── [CRITICAL ALERT] Rogue out-of-bounds instruction captured!")
                            print(f"    └── [ACTION] Dispatching kill signal to target PID {pid} instantly.")
                            proc.kill() # Hard termination
                            print(f"    └── [STATUS] Threat Neutralized successfully.\n")
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    continue
            
            known_pids = current_pids
            time.sleep(0.1) # Small loop sleep to keep CPU overhead near 0%
            
    except KeyboardInterrupt:
        print("\nStopping system process monitor.")

if __name__ == "__main__":
    watch_system_processes()


