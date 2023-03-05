# python3
import sys
import threading
import numpy

def build_tree(lv_num, ll_parent):
    la_tree = {}
    lv_rindex = 0

    for i in range(lv_num):
        la_tree[i] = []

    for i, ll_parent in enumerate(ll_parent):
        if ll_parent != -1:
            la_tree[ll_parent].append(i)
        else:
            lv_rindex = i

    return la_tree, lv_rindex

def compute_height(la_tree, lv_rindex):
    la_queue = [(lv_rindex, 1)]
    lv_max_height = 0
    while la_queue:
        node, height = la_queue.pop(0)
        lv_max_height = max(lv_max_height, height)
        for lv_child in la_tree[node]:
            la_queue.append((lv_child, height+1))

    return lv_max_height


def main():
    lv_input_method = input()
    if lv_input_method == 'I':
        lv_num = int(input())       
        gl_parents = list(map(int, input().split()))
    elif lv_input_method == 'F':
        lv_filename = input()     # implement input form keyboard and from files
        if 'a' in lv_filename:                          # let user input file name to use, don't allow file names with letter a
            return
        with open(f"./test/{lv_filename}", mode="r") as file:
            lv_num = int(file.readline())
            gl_parents = list(map(int, file.readline().split())) 

    la_tree, lv_rindex = build_tree(lv_num, gl_parents)
    print(compute_height(la_tree, lv_rindex))


#sys.setrecursionlimit(10**7)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()
main()
