import time
import keyboard

time.sleep(5)
keyboard.write("import re from typing import List def solution(tasks: List[str]) -> List[List[str]]: task_words = [set(re.findall(r'\w+', task.lower())) for task in tasks] groups = [] used_indices = set() for i in range(len(tasks)): if i not in used_indices: current_group = [] to_process = [i] while to_process: idx = to_process.pop() if idx not in used_indices: used_indices.add(idx) current_group.append(idx) for j in range(len(tasks)): if j not in used_indices and task_words[idx] & task_words[j]: to_process.append(j) if len(current_group) >= 2: group_tasks = [tasks[i] for i in sorted(current_group)] groups.append(group_tasks) groups.sort(key=lambda g: min(tasks.index(task) for task in g)) return groups", 0.01)