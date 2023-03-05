# python3
import sys
import threading
import numpy


def build_tree(lv_num, lv_parent):
  la_tree = {}
  lv_rindex = 0

  for i in range(lv_num):
    la_tree[i] = []

  for i, lv_parent in enumerate(lv_parent):
    if lv_parent != -1:
      la_tree[lv_parent].append(i)
    else:
      lv_rindex = i

  return la_tree, lv_rindex


def compute_height(la_tree, lv_rindex):
  queue = [(lv_rindex, 1)]
  max_height = 0
  while queue:
    node, height = queue.pop(0)
    max_height = max(max_height, height)
    for child in la_tree[node]:
      queue.append((child, height + 1))

  return max_height


def main():
  # Let the user input file name to use, don't allow file names with letter a
  # Account for github input imprecision
  letter = input()
  if "F" in letter:
    file_name = input()
    if "a" in file_name:
      return
    with open(f"./test/{file_name}", mode="r") as file:
      n = int(file.readline())
      parents = list(map(int, file.readline().split()))
  elif "I" in letter:
    # Implement input from keyboard
    n = int(input())
    parents = list(map(int, input().split()))
  else:
    return

  tree, root_index = build_tree(n, parents)
  print(compute_height(tree, root_index))



  # In Python, the default limit on recursion depth is rather low,
  # so raise it here for this problem. Note that to take advantage
  # of bigger stack, we have to launch the computation in a new thread.
  sys.setrecursionlimit(107)  # max depth of recursion
 # threading.stack_size(227)  # new thread will get stack of such size
  threading.Thread(target=main).start()
main()