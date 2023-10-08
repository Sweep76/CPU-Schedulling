from CPU_Processes import Process
from FCFS import FCFS
from SJF import SJF
from PriorityNP import PriorityNP
from PriorityP import PriorityP
from SRTF import SRTF

def MLQ(pInfo):
    if not pInfo.prio_check:
        pInfo.processes_list = [sublist[:4] for sublist in pInfo.processes_list]

    while pInfo.plist or pInfo.queue:
        if pInfo.plist and not pInfo.multi_feedback_check:
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
        if pInfo.prio_check:
            pInfo.min_process = min(pInfo.queue, key=lambda x: (x[4], x[3], x[2], x[1], x[0]))
            colML = 4
        else:
            pInfo.min_process = min(pInfo.queue, key=lambda x: (x[3], x[2], x[1], x[0]))
            colML = 3
        algo = pInfo.algorithms[pInfo.min_process[colML]] if not pInfo.multi_feedback_check else pInfo.algo3[pInfo.min_process[colML]]
        if algo == "FCFS":
            FCFS(pInfo)
        elif algo == "SJF":
            SJF(pInfo)
        elif algo == "PriorityNP":
            PriorityNP(pInfo)
        elif algo == "PriorityP":
            PriorityP(pInfo)
        elif algo == "SRTF":
            SRTF(pInfo)
        else:
            print("Invalid algorithm.")
    if not pInfo.multi_feedback_check:
        pInfo.displayGanttChart()
        pInfo.calculateTable()
        pInfo.displayTable()
        pInfo.displayEfficiency()

if __name__ == "__main__":
    pInfo = Process("SRTF", "PriorityP", "FCFS")
    # Customization
    # pInfo.processes_list = [
    #     ["P1", 10, 5, 3],
    #     ["P2", 1, 4, 1],
    #     ["P3", 12, 12, 6],
    #     ["P4", 3, 3, 7],
    #     ["P5", 2, 4, 2]
    # ]

    MLQ(pInfo)



