from CPU_Processes import Process
import copy

def SRTF(pInfo):
    # if the given processes contain the Priority or Level column, remove them as they are not needed in this algorithm.
    if not pInfo.multi_check and len(pInfo.processes_list[0]) > 3:
        pInfo.processes_list = [sublist[:3] for sublist in pInfo.processes_list]

    while pInfo.plist or pInfo.queue:
        if not pInfo.multi_check and pInfo.plist:
            if not pInfo.queue and pInfo.plist[0][1] > pInfo.time:
                pInfo.time = pInfo.plist[0][1]
                pInfo.timestamps.append(pInfo.time)
                pInfo.orderOfProcesses.append('idle')
            while True:
                if pInfo.plist and pInfo.plist[0][1] <= pInfo.time:
                    pInfo.queue.append(pInfo.plist[0])
                    pInfo.plist.pop(0)
                else:
                    break
        if not pInfo.multi_check:
            pInfo.min_process = min(pInfo.queue, key=lambda x: (x[2], x[1], x[0]))
        pInfo.orderOfProcesses.append(pInfo.min_process[0])
        if pInfo.plist and pInfo.time + pInfo.min_process[2] > pInfo.plist[0][1]:
            pInfo.min_process[2] -= pInfo.plist[0][1] - pInfo.time
            pInfo.time = pInfo.plist[0][1]
        else:
            pInfo.time += pInfo.min_process[2]
            integer_part = ''.join(char for char in pInfo.min_process[0] if char.isdigit())
            pInfo.processes_list[int(integer_part) - 1].append(pInfo.time)
            pInfo.queue.remove(pInfo.min_process)
        pInfo.timestamps.append(pInfo.time)
        if pInfo.multi_check:
            print("IT IS MULTICHECK SRTF")
            return
    pInfo.displayGanttChart()
    pInfo.calculateTable()
    pInfo.displayTable()
    pInfo.displayEfficiency()

if __name__ == "__main__":
    pInfo = Process("SRTF")
    # Customization
    # pInfo.processes_list = [
    #     ["P1", 10, 5, 3],
    #     ["P2", 1, 4, 1],
    #     ["P3", 12, 12, 6],
    #     ["P4", 3, 3, 7],
    #     ["P5", 2, 4, 2]
    # ]

    SRTF(pInfo)



