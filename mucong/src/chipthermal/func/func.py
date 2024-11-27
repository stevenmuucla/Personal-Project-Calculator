#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/6/29 9:13   xxx      1.0         None
"""


def check_RjcRjb(my_dict):
    if my_dict["lambda"] != "":
        if my_dict["Rjc"] == "":
            my_dict["Rjc"] = my_dict["h"] / 2 / my_dict["lambda"] / my_dict["a"] / my_dict["b"] * 1000
        if my_dict["Rjb"] == "":
            my_dict["Rjb"] = my_dict["h"] / 2 / my_dict["lambda"] / my_dict["a"] / my_dict["b"] * 1000
        return my_dict
    elif my_dict["Rjc"] == "" or my_dict["Rjb"] == "":
        return {}
    else:
        return my_dict


def cal_resistance(info_list: list, b5):
    # print(info_list)
    totResist = 0
    resistance = 0
    for i in info_list:
        if 0 in i:
            return [-3]
        else:
            resistance = i[1] / i[0] / (i[2]*b5) * 1000
    totResist += resistance
    # print(totResist)
    return totResist



def get_resistance(user_list, heat_percent):
    total = []
    total_resist = 0
    for i in range(len(user_list)):
        if i == 0:
            resist = user_list[i][0] / user_list[i][2] / user_list[i][1] / heat_percent * 1000
        else:
            resist = user_list[i][0] / user_list[i][2] / user_list[i][1] * 1000
        total_resist += resist
        total.append(resist)
        # print(total_resist)
    return [total, total_resist]
    # return total


def cal_Tw(Q, T0, v0, Rjc, Rjb, Ac, Rb, Tw, Ae, heat_percent, constants, user_list):

    x = Ae ** (0.5)  # 特征尺寸x（m）
    tm = (T0 + Tw) / 2  # 特征温度tm（℃），若环境温度与假设壁温相同，则特征温度（经计算）也与环境温度相等
    for i in range(len(constants) - 1):
        if constants[i][0] <= tm < constants[i + 1][0] or constants[-1][0] == tm:
            alpha = constants[i][1] + (constants[i + 1][1] - constants[i][1]) * (tm - constants[i][0]) / (
                    constants[i + 1][0] - constants[i][0])  # 运动粘度alpha（m²/s）
            lambda_l = constants[i][2] + (constants[i + 1][2] - constants[i][2]) * (tm - constants[i][0]) / (
                    constants[i + 1][0] - constants[i][0])  # 流体热导率lambda_l（W/m*K）
            Pr = constants[i][3] + (constants[i + 1][3] - constants[i][3]) * (tm - constants[i][0]) / (
                    constants[i + 1][0] - constants[i][0])  # Pr
        if tm > constants[-1][0]:
            return [-7]
    Rex = v0 * x / alpha  # 雷诺数

    if Rex > 500000:
        delta = (0.037 * (Rex ** 0.8) - 870) * (Pr ** (1 / 3)) * lambda_l / x  # 平均对流换热系数delta（W/m²·K）
    else:
        delta = 0.664 * lambda_l / x * (Rex ** 0.5) * (Pr ** (1 / 3))

    R0 = 1 / delta / Ac * 1000000  # R0（℃/W）

    Rup = get_resistance(user_list, heat_percent)[1] + Rjc + R0  # 上表面路径热阻之和R1（℃/W）
    Rdown = Rjb + Rb + R0  # 下表面路径热阻之和R2（℃/W）

    Tw_calculated = Q * Rdown / (Rup + Rdown) / Ae / delta + T0  # 计算壁温Tw（℃）
    return [Rup, Rdown, Tw_calculated, get_resistance(user_list, heat_percent)[0]]


def cal(userdict, userlist, constants):

    Q = userdict["Q"]
    Qt = userdict["Qt"]
    T0 = userdict["T0"]
    v0 = userdict["v0"]
    a = userdict["a"]
    b = userdict["b"]
    Rjc = userdict["Rjc"]
    Rjb = userdict["Rjb"]
    S = userdict["S"]
    A0 = userdict["A0"]
    lambda_b = userdict["lambda_b"]
    hb = userdict["hb"]
    Ab = userdict["Ab"]
    heat_percent = Q / Qt  # 计算发热量占比
    Ac = A0 * heat_percent  # 当量对流面积（mm²）
    Ae = S * heat_percent * 0.000001  # 等效换热面积（m²）


    Rb = hb / Ab / heat_percent / lambda_b * 1000  # 基板自身热阻Rb（℃/W）

    if not constants[0][0] <= T0 <= constants[-1][0]:
        return [-4]

    if Q > Qt:
        return[-5]

    if Q / a / b * 100 > 200:
        return [-6]

    if v0 < 0.01:
        return [-8]


    Tw = T0  # 初始假设壁温等于环境温度
    my_list = cal_Tw(Q, T0, v0, Rjc, Rjb, Ac, Rb, Tw, Ae, heat_percent, constants, userlist)

    if my_list == [-7]:
        return [-7]

    Tw_cal = my_list[-2]

    while abs(Tw_cal - Tw) >= 0.2:
        Tw += (Tw_cal - Tw) / 2
        my_list = cal_Tw(Q, T0, v0, Rjc, Rjb, Ac, Rb, Tw, Ae, heat_percent, constants, userlist)
        if my_list == [-7]:
            return [-7]
        Tw_cal = my_list[-2]


    Rup = my_list[0]
    Rdown = my_list[1]
    Tw_cal = my_list[2]
    resistance_list = my_list[3]

    T1_0 = Tw_cal  # 接触环境空气的材料1表面温度T1-0 （℃）

    Ttim1_1, T2_tim1, Ttim2_2, T3_tim2, Ttim3_3, Tc = 0, 0, 0, 0, 0, 0


    if len(resistance_list) >= 2:
        Ttim1_1 = T1_0 + resistance_list[0] * Rdown / (Rdown + Rup) * Q  # 材料1与界面材料1接触面温度TTIM1-1 （℃）
        Tc = Ttim1_1 + resistance_list[1] * Rdown / (Rdown + Rup) * Q  # 芯片壳体上表面温度Tc（℃）

        if len(resistance_list) >= 4:
            T2_tim1 = Ttim1_1 + resistance_list[1] * Rdown / (Rdown + Rup) * Q  # 材料2与界面材料1接触面温度T2 - TIM1（℃）
            Ttim2_2 = T2_tim1 + resistance_list[2] * Rdown / (Rdown + Rup) * Q  # 界面材料2与材料2接触面温度TTIM2 - 2 （℃）
            Tc = Ttim2_2 + resistance_list[3] * Rdown / (Rdown + Rup) * Q  # 芯片壳体上表面温度Tc（℃）

            if len(resistance_list) == 6:
                T3_tim2 = Ttim2_2 + resistance_list[3] * Rdown / (Rdown + Rup) * Q  # 材料3与界面材料2接触面温度T3-TIM2（℃）
                Ttim3_3 = T3_tim2 + resistance_list[4] * Rdown / (Rdown + Rup) * Q  # 界面材料3与材料3接触面温度TTIM3-3 （℃）
                Tc = Ttim3_3 + resistance_list[5] * Rdown / (Rdown + Rup) * Q  # 芯片壳体上表面温度Tc（℃）

    Tj = Tc + Rjc * Rdown / (Rdown + Rup) * Q  # 芯片结节温度计算值Tj（℃）
    Tj_b = Tj - Rjb * Rup / (Rdown + Rup) * Q  # 基板与芯片接触面的温度Tj - b（℃）
    Tb_0 = Tj_b - Rb * Rup / (Rdown + Rup) * Q  # 基板接触空气的下表面温度Tb-0（℃）
    return [T1_0, Ttim1_1, T2_tim1, Ttim2_2, T3_tim2, Ttim3_3, Tc, Tj, Tj_b, Tb_0]


def final(user_dict, user_list):
    constants = [[0, 0.00001328, 0.0244, 0.707],
                 [10, 0.00001416, 0.0251, 0.705],
                 [20, 0.00001506, 0.0259, 0.703],
                 [30, 0.00001600, 0.0267, 0.701],
                 [40, 0.00001696, 0.0276, 0.699],
                 [50, 0.00001795, 0.0283, 0.698],
                 [60, 0.00001897, 0.0290, 0.696],
                 [70, 0.00002002, 0.0296, 0.694],
                 [80, 0.00002109, 0.0305, 0.692]]

    for key, value in user_dict.items():
        if value == 0 and key != "T0":
            return [-2, key]

    # for i in user_list:
    #     if 0 in i:
    #         return [-3]

    user_dict = check_RjcRjb(user_dict)

    if user_dict == {}:
        return [-1]

    if cal(user_dict, user_list, constants) == [-4]:
        return [-4]

    elif cal(user_dict, user_list, constants) == [-5]:
        return [-5]

    elif cal(user_dict, user_list, constants) == [-6]:
        return [-6]

    elif cal(user_dict, user_list, constants) == [-7]:
        return [-7]

    else:
        return cal(user_dict, user_list, constants)
