import random
import time
import multiprocessing

def process_task(task_id, node_id, network_latency):
    time.sleep(random.uniform(0.1, 0.5) + network_latency) 
    print(f"Task {task_id} completed on Node {node_id}")

def schedule_tasks(tasks, nodes):
    task_index = 0
    node_index = 0
    while task_index < len(tasks):
        node = nodes[node_index]
        task = tasks[task_index]
        network_latency = random.uniform(0.0, 0.2) 
        process = multiprocessing.Process(target=process_task, args=(task, node, network_latency))
        process.start()
        node_index = (node_index + 1) % len(nodes)
        task_index += 1

if __name__ == "__main__":
    tasks = list(range(10)) 
    nodes = ["node 1", "node 2", "node 3"] 
    schedule_tasks(tasks, nodes)
    for process in multiprocessing.active_children():
        process.join()
