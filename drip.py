import pulp
import subprocess
from collections import defaultdict

N, M, t = input().split()
N = int(N)
M = int(M)

inp_file = open("input.txt", "w") 
inp_file.write(str(N) + " " + str(M) + " " + t + "\n")

for nd_idx in range(N):
  nghrs = list(map(int, input().split()))
  
  for nghr in nghrs:
    inp_file.write(str(nghr) + " ")
 
  inp_file.write("\n")

inp_file.close()

subprocess.run("./reductions")

mfvs_file = open('mfvs.txt', 'r')
feas_solution = mfvs_file.readlines()
mfvs_file.close()

final_fvs = []

for nd_line in feas_solution:
   fvs_nd = int(nd_line)
   final_fvs.append(fvs_nd)


reduced_graph_file = open('reduced_graph.txt', 'r')
reduced_graph = reduced_graph_file.readlines()
reduced_graph_file.close()

graph = defaultdict(list)

flag = True
nd_idx = 0

for line in reduced_graph:

   nghrs = list(map(int, line.split()))
   
   if flag:
      flag = False
   else: 
      graph[nd_idx + 1] = nghrs
      nd_idx += 1

cost = []
fvs_possibility = {}
topo_ordering = {}

for nd in range(1, N+1):
    
    x_var = pulp.LpVariable("x_{0}".format(nd), lowBound=0, upBound=1, cat=pulp.LpBinary)
    d_var = pulp.LpVariable("d_{0}".format(nd), lowBound=1, upBound=N, cat=pulp.LpInteger)  
        
    cost.append(x_var)
      
    fvs_possibility[nd] = x_var
    topo_ordering[nd] = d_var


# model
fvs_model = pulp.LpProblem("FVS_Model", pulp.LpMinimize)

# objective function
fvs_model += pulp.lpSum(cost)

# specify constraints
for u in range(1, N+1):
    for v in graph[u]:
          fvs_model += (topo_ordering[v] - topo_ordering[u] + N*fvs_possibility[v] >= 1)

solver = pulp.PULP_CBC_CMD(msg=False)
#solver = pulp.SCIP_CMD(msg=True)
#solver = pulp.GUROBI_CMD(msg=True, warmStart=True)
fvs_model.solve(solver)

for nd in range(1, N+1):
    if (round(fvs_possibility[nd].value()) == 1):
       final_fvs.append(nd)

for nd in final_fvs:
   print(nd)
