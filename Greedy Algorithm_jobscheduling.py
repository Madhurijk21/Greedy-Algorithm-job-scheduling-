

#Team Members:

#1. Name:  Madhuri Bandari
#   Email Id: bandari.24@wright.edu

#2. Name:  Venkata Sireesha Marella
#   Email Id: marella.22@wright.edu

#3. Name:  Naga Deepthi Doddaka
#   Email Id: doddaka.3@wright.edu
   


# ======================================================
# Pseudocode:
# 1. To obtain the list of jobs (JobID, start, finish), parse the input.
#2. Arrange the tasks according to their deadlines (a self-serving tactic).
#3. Start two lists: one for jobs that are linked to machine M1, and another for machine M2.
#4. Work your way through the sorted jobs:
# a. Employ M1 to plan a job if possible (its start time >= M1's present free time).
# b. If not, see if the task can be scheduled on M2 (provided that its start time is greater than M2's available free time). 
# 5. After a work is scheduled, update the machine's (M1 or M2) free time.
# 6. Output all planned jobs as well as the jobs that are allocated to each machine.
# ======================================================

# ======================================================
# Greedy Heuristic Used:
# Jobs are chosen by the earliest finish time algorithm based on when their finish time.
#This guarantees that a machine is as free as feasible at all times, enabling the scheduling of more work at a later time. 
#Jobs that can be scheduled on M1 are given priority; if not, they are scheduled on M2, if space is available. 
#This method ensures that the number of non-overlapping jobs on both machines is maximized.
# ======================================================

# ======================================================
# Informal Argument for Correctness:
# We make sure that jobs have the largest feasible window of time to schedule them in the future by scheduling jobs with the earliest end time first.
# Because arranging a job with an earlier end time does not conflict with other tasks that may be booked later, this avaricious decision is the best one.
# We additionally guarantee effective task distribution between the two machines by giving M1 priority. 
# The number of scheduled jobs is maximized using this strategy.
# ======================================================

# ======================================================
# Computational Complexity:
# 1. Sorting the jobs by their end times takes ---> O(n log n), where n is the no. of jobs/duties.
# 2. Iterating through the duties to allocate them takes O(n).
# Therefore, overall time complexity (T.C) of the greedy algorithm is O(n log n).
# ======================================================

import sys
import os

def schedule_jobs(input_file, output_file):
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())  
        dts = []
        for _ in range(n):
            iddts, stss, fnss = map(int, f.readline().strip().split())
            dts.append((iddts, stss, fnss))

    dts.sort(key=lambda x: x[2])  

    dtsmahin1 = []
    dtsmahin2 = []
    ftimahin1 = 0
    ftimahin2 = 0
    
    for iddts, stss, fnss in dts:
        if stss >= ftimahin1: 
            dtsmahin1.append(iddts)
            ftimahin1 = fnss  
        elif stss >= ftimahin2:  
            dtsmahin2.append(iddts)
            ftimahin2 = fnss 

    jbscmptshdu = len(dtsmahin1) + len(dtsmahin2)

  
    with open(output_file, 'w') as f:
        f.write(f"{jbscmptshdu}\n")
        f.write(" ".join(map(str, dtsmahin1)) + "\n")
        f.write(" ".join(map(str, dtsmahin2)) + "\n")

if __name__ == "__main__":
   
    if len(sys.argv) != 2:
        sys.exit(1)

    input_file = sys.argv[1]

    input_prefix, input_ext = os.path.splitext(input_file)
    output_prefix = input_prefix.replace("Input", "Output")
    output_file = output_prefix + input_ext
	
    schedule_jobs(input_file, output_file)