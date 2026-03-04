
class Task:
    def __init__(self, title):
        self.title = title
        self.completed = False
        

    def complete(self):
        self.completed = True
        print(f"✅ Task '{self.title}' completed.")
        

# Add methods to add tasks and search tasks by title

class User:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"📌 Task '{task.title}' added to {self.name}.")

    def get_task_by_title(self, title):
        for t in self.tasks:
            if t.title == title:
                return t
        return None