# coding: utf-8

class fixed_value:
    """fixed-value class"""  # 三重クォートによるコメント

    def __init__(self):  # コンストラクタ
        self.name = ""

    """for teach_data"""
    cont = 0
    test_samplenumber = 100
    randmax = 3
    randmin = -3

    """for init_network"""
    W1size = [2, 30]
    W2size = [30, 30]
    W3size = [30, 1]
    b1 = 1
    b2 = 1
    b3 = 1

    """for main"""
    batch_size = 10
