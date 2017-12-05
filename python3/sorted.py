#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' python排序算法 '''

def insert_sort(origin_list):
    ''' 插入排序 '''
    sorted_list = []
    for i in range(0, len(origin_list)):
        if len(sorted_list) == 0:
            sorted_list.append(origin_list[i])
            continue
        for j in range(len(sorted_list) - 1, -1, -1):
            if origin_list[i] >= sorted_list[j]:
                sorted_list.insert(j + 1, origin_list[i])
                break
            if j == 0:
                sorted_list.insert(0, origin_list[i])
    origin_list[:] = sorted_list[:]


origin_list = [5, 3, 1, 7, 9, 8]
insert_sort(origin_list)
print('插入排序:', origin_list)

def bubble_sort(origin_list):
    ''' 冒泡排序 '''
    for i in range(len(origin_list), 0, -1):
        for j in range(0, i - 1):
            if origin_list[j] > origin_list[j + 1]:
                origin_list[j], origin_list[j + 1] = origin_list[j + 1], origin_list[j]

origin_list = [5, 3, 1, 7, 9, 8]
bubble_sort(origin_list)
print('冒泡排序:', origin_list)
