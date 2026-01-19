import os

class SmartDeveloper:
    def __init__(self):
        self.skills_path = "brain/skills"
        self.generated_path = "brain/generated"
        
    def generate_solution(self, task):
        """
        Translates English -> Python Code
        """
        print(f"🔨 DEVELOPER: Writing code for '{task}'...")
        
        # Simple Logic for Phase 2 (We will make this AI-powered later)
        code = ""
        filename = "task_script.py"
        
        if "disk" in task.lower():
            code = "import shutil\ntotal, used, free = shutil.disk_usage('/')\nprint(f'💾 Disk Free: {free // (2**30)} GB')"
        elif "list" in task.lower():
            code = "import os\nprint(f'📂 Files here: {os.listdir(\".\")}')"
        elif "memory" in task.lower():
            code = "import sys\nprint('🧠 checking memory... (simulation)')"
        else:
            code = f"print('🤖 I am simply printing: {task}')"

        # Save the file
        filepath = os.path.join(self.generated_path, filename)
        with open(filepath, "w") as f:
            f.write(code)
            
        return filepath