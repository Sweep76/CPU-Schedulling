from CPU_Processes import Process
from FCFS import FCFS
from SJF import SJF
from PriorityNP import PriorityNP
from PriorityP import PriorityP
from RoundRobin import RoundRobin
from SRTF import SRTF
from MLQ import MLQ
import copy

def MLFQ(pInfo):

    while pInfo.plist or pInfo.queue1 or pInfo.queue2 or pInfo.queue3:
        if pInfo.plist:
            if not pInfo.queue1 and not pInfo.queue2 and not pInfo.queue3 and pInfo.plist[0][1] > pInfo.time:
                pInfo.time = pInfo.plist[0][1]
                pInfo.timestamps.append(pInfo.time)
                pInfo.timestamps1.append(pInfo.time)
                pInfo.timestamps2.append(pInfo.time)
                pInfo.timestamps3.append(pInfo.time)
                pInfo.orderOfProcesses.append('idle')
                pInfo.orderOfProcesses1.append('idle')
                pInfo.orderOfProcesses2.append('idle')
                pInfo.orderOfProcesses3.append('idle')
            while True:
                if pInfo.plist and pInfo.plist[0][1] <= pInfo.time:
                    pInfo.queue1.append(pInfo.plist[0])
                    pInfo.plist.pop(0)
                else:
                    break

        while pInfo.queue1:
            pInfo.min_process = pInfo.queue1[0]
            pInfo.orderOfProcesses.append(pInfo.min_process[0])
            pInfo.orderOfProcesses1.append(pInfo.min_process[0])
            pInfo.orderOfProcesses2.append(" ")
            pInfo.orderOfProcesses3.append(" ")
            if pInfo.min_process[2] > pInfo.QT1:
                pInfo.min_process[2] -= pInfo.QT1
                pInfo.time += pInfo.QT1
                pInfo.queue2.append(pInfo.min_process)
            else:
                pInfo.time += pInfo.min_process[2]
                integer_part = ''.join(char for char in pInfo.min_process[0] if char.isdigit())
                pInfo.processes_list[int(integer_part) - 1].append(pInfo.time)
            pInfo.queue1.pop(0)
            pInfo.timestamps.append(pInfo.time)
            pInfo.timestamps1.append(pInfo.time)
            pInfo.timestamps2.append(pInfo.time)
            pInfo.timestamps3.append(pInfo.time)
        if pInfo.plist and pInfo.plist[0][1] <= pInfo.time:
            continue
        elif not pInfo.queue2 and not pInfo.queue3:
            continue

        while pInfo.queue2:
            pInfo.orderOfProcesses.append(pInfo.queue2[0][0])
            pInfo.orderOfProcesses2.append(pInfo.queue2[0][0])
            pInfo.orderOfProcesses1.append(" ")
            pInfo.orderOfProcesses3.append(" ")
            if pInfo.queue2[0][2] > pInfo.QT2:
                pInfo.queue2[0][2] -= pInfo.QT2
                pInfo.time += pInfo.QT2
                pInfo.queue3.append(pInfo.queue2[0])
            else:
                pInfo.time += pInfo.queue2[0][2]
                integer_part = ''.join(char for char in pInfo.queue2[0][0] if char.isdigit())
                pInfo.processes_list[int(integer_part) - 1].append(pInfo.time)
            pInfo.queue2.pop(0)
            pInfo.timestamps.append(pInfo.time)
            pInfo.timestamps1.append(pInfo.time)
            pInfo.timestamps2.append(pInfo.time)
            pInfo.timestamps3.append(pInfo.time)
            if pInfo.plist and pInfo.plist[0][1] <= pInfo.time:
                break
        if (pInfo.plist and pInfo.plist[0][1] <= pInfo.time) or not pInfo.queue3:
            continue

        if pInfo.queue3:
            pInfo.queue = pInfo.queue3
            if len(pInfo.algo3) > 1:
                pInfo.multi_check = True
                MLQ(pInfo)
            elif pInfo.algo3[1] == "FCFS":
                FCFS(pInfo)
            elif pInfo.algo3[1] == "SJF":
                SJF(pInfo)
            elif pInfo.algo3[1] == "PriorityNP":
                PriorityNP(pInfo)
            elif pInfo.algo3[1] == "PriorityP":
                PriorityP(pInfo)
            elif pInfo.algo3[1] == "RoundRobin":
                RoundRobin(pInfo)
            elif pInfo.algo3[1] == "SRTF":
                SRTF(pInfo)
            else:
                print("Invalid algorithm.")

    pInfo.displayGanttChart()
    pInfo.calculateTable()
    pInfo.displayTable()
    pInfo.displayEfficiency()
    pInfo.displayGanttChart1()
    pInfo.displayGanttChart2()
    pInfo.displayGanttChart3()

if __name__ == "__main__":
    pInfo = Process("MLFQ")
    pInfo.QT = 2
    pInfo.QT1 = 2
    pInfo.QT2 = 3
    # Customization
    # pInfo.processes_list = [
    #     ["P1", 10, 5, 3],
    #     ["P2", 1, 4, 1],
    #     ["P3", 12, 12, 6],
    #     ["P4", 3, 3, 7],
    #     ["P5", 2, 4, 2]
    # ]

    MLFQ(pInfo)



