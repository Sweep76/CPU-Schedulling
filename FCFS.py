from CPU_Processes import Process

def FCFS(pInfo):
    # pInfo.queue is needed in this condition in case FCFS gets chosen as algo3 in MLFQ.
    # originally, fcfs would not need pInfo.queue in the condition since if pInfo.plist is empty, pInfo.queue is also
    # empty, but if fcfs is chosen as algo3 in MLFQ, plist is already empty while the queue is still there.
    while pInfo.plist or pInfo.queue:
        if not pInfo.multi_check and not pInfo.multi_feedback_check:
            if not pInfo.queue and pInfo.plist[0][1] > pInfo.time:
                pInfo.time = pInfo.plist[0][1]
                pInfo.timestamps.append(pInfo.time)
                pInfo.orderOfProcesses.append('idle')
            pInfo.queue.append(pInfo.plist[0])
            pInfo.plist.pop(0)
        # This should not be executed when FCFS is chosen as an algo in MLQ because MLQ decides the value of
        # min_process variable, not this FCFS function
        if not pInfo.multi_check:
            pInfo.min_process = pInfo.queue[0]
        pInfo.time += pInfo.min_process[2]
        pInfo.timestamps.append(pInfo.time)
        pInfo.orderOfProcesses.append(pInfo.min_process[0])
        # Append ending pInfo.time
        integer_part = ''.join(char for char in pInfo.min_process[0] if char.isdigit())
        pInfo.processes_list[int(integer_part) - 1].append(pInfo.time)
        pInfo.queue.remove(pInfo.min_process)
        if pInfo.multi_feedback_check:
            pInfo.timestamps1.append(pInfo.time)
            pInfo.timestamps2.append(pInfo.time)
            pInfo.timestamps3.append(pInfo.time)
            pInfo.orderOfProcesses1.append(" ")
            pInfo.orderOfProcesses2.append(" ")
            pInfo.orderOfProcesses3.append(pInfo.min_process[0])
        if pInfo.multi_check:
            print("IT IS MULTICHECK FCFS")
            return
    if not pInfo.multi_feedback_check:
        pInfo.displayGanttChart()
        pInfo.calculateTable()
        pInfo.displayTable()
        pInfo.displayEfficiency()

if __name__ == "__main__":
    pInfo = Process("FCFS")
    # Customization
    # pInfo.processes_list = [
    #     ["P1", 10, 5],
    #     ["P2", 0, 4],
    #     ["P3", 12, 12],
    #     ["P4", 3, 3],
    #     ["P5", 2, 5]
    # ]

    FCFS(pInfo)



