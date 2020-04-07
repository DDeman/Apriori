#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = ''
__author__ = '任晓光'
__mtime__ = '2020/3/26'
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
class Apriori():
    def __init__(self):
        pass

    #构造项集，排列组合
    def fun(self,w, n_item):
        res = []
        temp = []
        i = 0
        # 由于w可能是嵌套的这里需要找出所有的里面的不重复子项
        if w == []:
            return
        if type(w[0]) is str:
            pass
        elif type(w[0]) is list:
            new_w = []
            for item in w:
                for f in item:
                    if f not in new_w:
                        new_w.append(f)
            w = new_w
        self.back(res, temp, i, w, n_item)
        return res
    def back(self,res, temp, i, w, n_item):
        if i == len(w):
            return
        temp.append(w[i])
        tem = temp.copy()
        if len(temp) == n_item:
            res.append(tem)
        self.back(res, temp, i + 1, w, n_item)
        temp.pop()
        self.back(res, temp, i + 1, w, n_item)

    #构造起始的项集，就是数据集中所有不重复的项，单一拎出来
    def start_a(self,data):
        c1 = []
        for item in data:
            for ite in item:
                if [ite] not in c1:
                    c1.append([ite])
        self.c1 = list(map(frozenset, c1))
        self.n_items = len(self.c1)


    #判断是否为子集,这里由于是[[],[].....]这种嵌套形式的，所有写一个函数
    def issubset_(self,c_, item):
        r = True
        for i in c_:
            if i not in item:
                r = False
        return r

    #扫描数据集
    def scan(self,data, C, n_data, min_support):
        result = {}
        L = {}
        for i in C:
            if frozenset(i) not in result:
                result[frozenset(i)] = 0
        new_C = []
        for c_ in C:
            for item in data:
                r = self.issubset_(c_, item)
                if self.issubset_(c_, item):
                    result[frozenset(c_)] += 1
                    new_C.append(c_)
            result[frozenset(c_)] = result[frozenset(c_)] / n_data
            if result[frozenset(c_)] > min_support:
                L[frozenset(c_)] = result[frozenset(c_)]
        return L, result, new_C

    def support(self,data,min_support):
        '''
        :param data:
        :param min_support: 最小支持度
        :return: 满足最小支持度的所有项集
        '''
        self.start_a(data)
        new_C = data
        n_data = len(data)
        self.result_L_min = []
        self.result_L_full = []
        for n_item in range(1, self.n_items):
            C = self.fun(new_C, n_item)
            L, result_n_item, new_C = self.scan(data, C, n_data, min_support)
            self.result_L_min.append(L)
            self.result_L_full.append(result_n_item)
        return self.result_L_min,self.result_L_full

    #把支持度转为key_value格式
    def k_v_inlist(self,data,dic):
        for i in data:
            for j in i:
                dic[j] = i[j]
        return dic


    def confidence(self):
        result_L_min_dic = dict()
        result_L_full_dic = dict()
        self.result_L_min_dic = self.k_v_inlist(self.result_L_min,result_L_min_dic)    #脱内括号，列表
        self.result_L_full_dic = self.k_v_inlist(self.result_L_full,result_L_full_dic)
        # res = self.fun_2(result_L_full)

        #单独取key，用于排列组合
        lis = []
        for v, k in enumerate(self.result_L_min_dic):
            for j in k:
                if j not in lis:
                    lis.append(j)

        re = self.fun_2(lis)
        confidence = {}
        for ite in re:
            lll = []
            lian_he_p = result_L_full_dic[ite]
            for i in ite:
                p_ = self.result_L_full_dic[frozenset({i})]
                lll.append(lian_he_p / p_)
            confidence[ite] = lll
        return confidence
    #排列组合
    def fun_2(self,data):
        res = []
        temp = []
        i = 0
        self.back_2(res,temp,i,data)
        return res
    def back_2(self,res,temp,i,data):
        if i == len(data):
            return
        temp.append(data[i])
        tem = temp.copy()
        if len(tem) >= 2:
            res.append(frozenset(tem))
        self.back_2(res,temp,i+1,data)
        temp.pop()
        self.back_2(res,temp,i+1,data)

    def result_L_min_dic_(self):
        return self.result_L_min_dic

    def result_L_full_dic_(self):
        return self.result_L_full_dic

if __name__ == '__main__':
    def createData():
        lis = [['面包', '牛奶', '啤酒', '尿布'], ['面包', '牛奶', '啤酒'], ['啤酒', '尿布'], ['面包', '牛奶', '花生']]
        return lis
    data = createData()
    Apriori = Apriori()
    min_support = 0.5
    result_L_min,result_L_full = Apriori.support(data,min_support)
    # result_L_min_dic, result_L_full_dic = Apriori.confidence()
    con = Apriori.confidence()
    print(Apriori.result_L_full_dic_())

    print(con)
    '''
    a = frozenset({'牛奶', '面包'})
    print(result_L_full_dic[a])
    print(result_L_min_dic)
    lis = []
    for v,k in enumerate(result_L_min_dic):
        for j in k:
            if j not in lis:
                lis.append(j)
    def fun_2(data):
        res = []
        temp = []
        i = 0
        back_2(res,temp,i,data)
        return res
    def back_2(res,temp,i,data):
        if i == len(data):
            return
        temp.append(data[i])
        tem = temp.copy()
        if len(tem) >= 2:
            res.append(frozenset(tem))
        back_2(res,temp,i+1,data)
        temp.pop()
        back_2(res,temp,i+1,data)



    print(lis)
    re = fun_2(lis)

    confidence = {}
    for ite in re:
        lll = []
        lian_he_p = result_L_full_dic[ite]
        for i in ite:
            p_ = result_L_full_dic[frozenset({i})]
            lll.append(p_)
        confidence[ite] = lll
    print(confidence)
        # print(result_L_full_dic[ite])
    '''
    class Tree():
        def __init__(self,node):
            self.node = node
            self.left = None
            self.right = None


