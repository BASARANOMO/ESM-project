#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 18 14:45:46 2021

@author: gglj
"""

import numpy as np


def model(para):
    """
    para: 输入参数
    output: 返回模型预测结果
    """
    output = []
    for x in [0.01, 0.05, 0.1, 0.14, 0.2]:
        y = x*para[0] # 模型公式
        output.append(y)
    return output


def evaluate(output, set_error=1):
    """
    output: 预测值
    set_error: 允许误差范围
    accept: 返回是否接受（如果五个预测值的误差都在允许误差范围内，则接受，否则不接受）
    """
    accept = 1
    y_list = [50, 150, 500, 850, 1000]
    for i in range(5):
        error = output[i]/y_list[i]-1
        if error > set_error or error < -set_error:
            accept = 0
            break
    return accept


def HSY(n, para_range):
    """
    n: 采样次数
    para_range: 参数均匀分布的上下限，比如[[0,1],[0,1]]表示有2个参数，都是0-1均匀分布
    accept_para_list: 返回可接受的参数
    unaccept_para_list: 返回不可接受的参数
    """
    para_num = len(para_range)
    # 采样
    para_list = []
    for i in range(para_num):
        a = para_range[i][0]
        b = para_range[i][1]
        para_list.append(np.random.uniform(a, b, n))
    # 模型
    output_list = []
    for i in range(n):
        para = []
        for j in range(para_num):
            para.append(para_list[j][i])
        output = model(para)
        output_list.append(output)
    # 评估，划分接受和不接受
    evaluate_list = []
    for i in range(n):
        output = output_list[i]
        evaluate_result = evaluate(output, set_error=1)
        evaluate_list.append(evaluate_result)
    accept_para_list = []
    unaccept_para_list = []
    for i in range(para_num):
        accept_para = []
        unaccept_para = []
        for j in range(n):
            if evaluate_list[j] == 1:
                accept_para.append(para_list[i][j])
            else:
                unaccept_para.append(para_list[i][j])
        accept_para_list.append(accept_para)
        unaccept_para_list.append(unaccept_para)
    return accept_para_list, unaccept_para_list
                

accept_para_list, unaccept_para_list = HSY(1000, [[1000, 10000]])        

