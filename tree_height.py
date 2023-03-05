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
            queue.append((child, height+1))

    return max_height


def main():
    lv_input_method = input("Input(I) or file(F)?")
    if lv_input_method == 'I':
        gv_num = int(input("Innput the number of elements: "))       
        gl_parents = list(map(int, input("Enter the parent array, separated by space: ").strip().split()))
    elif lv_input_method == 'F':
        lv_filename = input("Enter the file name: ")     # implement input form keyboard and from files
        if 'a' in lv_filename:                          # let user input file name to use, don't allow file names with letter a
            print("Filename cannot contain the letter 'a'")
            return
        elif 'i' in lv_filename: 
            with  open(f"./test/{lv_filename}", mode="r") as file:
                gv_num=int(file.readline().strip())
                gl_parents = list(map(int, file.readline().strip().split()))

    la_tree, lv_rindex = build_tree(gv_num, gl_parents)
    print(compute_height(la_tree, lv_rindex))


sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
#main() I was set up to FAIL
