#include <stdio.h>

typedef struct {
    int id;          // Process ID
    int arrivalTime; // Arrival time of the process
    int burstTime;   // Burst time of the process
    int waitingTime; // Waiting time for the process
    int turnaroundTime; // Turnaround time for the process
    int endTime;     // End time for the process (end time)
} Process;

void calculateWaitingTime(Process processes[], int n) {
    processes[0].waitingTime = 0;

    for (int i = 1; i < n; i++) {
        int waitingTime = processes[i - 1].endTime - processes[i].arrivalTime;
        processes[i].waitingTime = (waitingTime > 0) ? waitingTime : 0;
    }
}

void calculateTurnaroundTime(Process processes[], int n) {
    for (int i = 0; i < n; i++) {
        processes[i].turnaroundTime = processes[i].waitingTime + processes[i].burstTime;
    }
}

void displayResults(Process processes[], int n) {
    printf("Process\tArrival Time\tBurst Time\tEnd Time\tTurnaround Time\tWaiting Time\n");

    for (int i = 0; i < n; i++) {
        printf("P%d\t%d\t\t%d\t\t%d\t\t%d\t\t%d\n", processes[i].id, processes[i].arrivalTime,
               processes[i].burstTime, processes[i].endTime, processes[i].turnaroundTime, processes[i].waitingTime);
    }

    // Calculate and display average turnaround time and average waiting time
    double avgTurnaroundTime = 0;
    double avgWaitingTime = 0;

    for (int i = 0; i < n; i++) {
        avgTurnaroundTime += processes[i].turnaroundTime;
        avgWaitingTime += processes[i].waitingTime;
    }

    avgTurnaroundTime /= n;
    avgWaitingTime /= n;

    printf("\nAverage Turnaround Time: %.2lf", avgTurnaroundTime);
    printf("\nAverage Waiting Time: %.2lf", avgWaitingTime);

    // Calculate and display CPU utilization
    int totalBurstTime = 0;
    for (int i = 0; i < n; i++) {
        totalBurstTime += processes[i].burstTime;
    }

    double cpuUtilization = (double)totalBurstTime / processes[n - 1].endTime * 100.0;
    printf("\nCPU Utilization: %.2lf%%\n", cpuUtilization);

    // Display Gantt chart
    printf("\nGantt Chart:\n");
    printf("\t");
    for (int i = 0; i < n; i++) {
        printf("P%d\t", processes[i].id);
    }
    printf("\n");

    int currentTime = 0;
    for (int i = 0; i < n; i++) {
        printf("%d\t", currentTime);
        processes[i].endTime = currentTime + processes[i].burstTime;
        currentTime += processes[i].burstTime;
    }
    printf("%d\n", currentTime);
}

int main() {
    int n;

    printf("Enter the number of processes: ");
    scanf("%d", &n);

    Process processes[n];

    for (int i = 0; i < n; i++) {
        printf("Enter arrival time and burst time for Process %d (e.g., 2 5): ", i + 1);
        scanf("%d %d", &processes[i].arrivalTime, &processes[i].burstTime);
        processes[i].id = i + 1;
    }

    // Sort processes based on their arrival time (FCFS)
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (processes[j].arrivalTime > processes[j + 1].arrivalTime) {
                Process temp = processes[j];
                processes[j] = processes[j + 1];
                processes[j + 1] = temp;
            }
        }
    }

    // Calculate end times for each process
    int currentTime = processes[0].arrivalTime;
    for (int i = 0; i < n; i++) {
        if (processes[i].arrivalTime > currentTime) {
            currentTime = processes[i].arrivalTime;
        }
        processes[i].endTime = currentTime + processes[i].burstTime;
        currentTime = processes[i].endTime;
    }

    calculateWaitingTime(processes, n);
    calculateTurnaroundTime(processes, n);

    displayResults(processes, n);

    return 0;
}
