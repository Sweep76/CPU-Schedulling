from CPU_Processes import Process

def FCFS(pInfo):
    # if the given processes contain the Priority or Level column, remove them as they are not needed in this algorithm.
    if not pInfo.multi_check and len(pInfo.processes_list[0]) > 3:
        pInfo.processes_list = [sublist[:3] for sublist in pInfo.processes_list]

    while pInfo.plist:
        if not pInfo.multi_check:
            if not pInfo.queue and pInfo.plist[0][1] > pInfo.time:
                pInfo.time = pInfo.plist[0][1]
                pInfo.timestamps.append(pInfo.time)
                pInfo.orderOfProcesses.append('idle')
            pInfo.queue.append(pInfo.plist[0])
            pInfo.plist.pop(0)
            pInfo.min_process = pInfo.queue[0]
        pInfo.time += pInfo.min_process[2]
        pInfo.timestamps.append(pInfo.time)
        pInfo.orderOfProcesses.append(pInfo.min_process[0])
        # Append ending pInfo.time
        integer_part = ''.join(char for char in pInfo.min_process[0] if char.isdigit())
        pInfo.processes_list[int(integer_part) - 1].append(pInfo.time)
        pInfo.queue.pop(0)
        if pInfo.multi_check:
            return
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



