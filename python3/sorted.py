#!/usr/bin/env python3
# -*- coding: utf-8 -*-

''' python排序算法 '''

def insert_sort(origin_list):
    ''' 插入排序 '''
    sorted_list = []
    print(origin_list)
    for i in range(0, len(origin_list)):
        print(sorted_list)
        if 0 == len(sorted_list):
            sorted_list.append(origin_list[i])
            continue
        for j in range(0, len(sorted_list)):
            if origin_list[i] >= sorted_list[-1]:
                sorted_list.append(origin_list[i])
            else:
                sorted_list.insert(j, origin_list[i])
