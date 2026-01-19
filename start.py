import subprocess
import time
import sys
import webbrowser

def start_system():
    print("============================================================")
    print("🧠 DREAM AI - INITIALIZING...")
    print("============================================================")

    # 1. Kill old processes to prevent "Address in Use" errors
    try:
        subprocess.run(["pkill", "-f", "brain/bridge.py"], stderr=subprocess.DEVNULL)
    except:
        pass

    # 2. Start the Bridge (The Server)
    print("🚀 Starting the Bridge...")
    bridge = subprocess.Popen([sys.executable, "brain/bridge.py"])
    
    time.sleep(2) # Give it a moment to wake up

    # 3. Open Dashboard
    if bridge.poll() is None:
        print("✅ System Online.")
        print("🖥️  Opening Dashboard...")
        webbrowser.open("http://localhost:3000")
    else:
        print("❌ Error: Bridge failed to start.")
        sys.exit(1)

    try:
        bridge.wait()
    except KeyboardInterrupt:
        print("\n🛑 Shutting down...")
        bridge.terminate()

if __name__ == "__main__":
    start_system()