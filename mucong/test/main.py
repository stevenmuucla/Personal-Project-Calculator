# -*- encoding: utf-8 -*-
from func.func import final

# b3 = input("目标芯片发热量(W):")  chip_heat
# b4 = input("单层基板总发热量(W) (该值不为0):") singlelayer_heat
# b6 = input("环境温度(℃):")   environment_temp
# b7 = input("空气流速(m/s):")  air_velocity
# b8 = input("Rjc(℃/W):")   husk_res
# b9 = input("Rjb(℃/W):")   board_res
# b10 = input("若无Rjc与Rjb数据，请填写芯片材料热导率(W/m·℃)")   material_thermal_cond
# b11 = input("最高结温(℃):")  junc_temp
# b12 = input("芯片长(mm):")  chip_length
# b13 = input("芯片宽(mm):")  chip_width
# b14 = input("芯片高(mm):")  chip_height
# b15 = input("基板表面积(mm²):")     substrate_surf_area

# b17 = input("界面材料热导率（W/m·K）:")   interface_thermal_cond
# b18 = input("界面材料层厚度（mm）:")    interface_thickness  无则填0，当空气计算，取默认值

# b22 = input("材料热导率（W/m·K）:")
# b23 = input("材料层厚度（mm）:")
# b24 = input("材料层导热截面积（mm²）:")
# b29 = input("对流表面积（mm²）:")  convection_area
# b34 = input("材料热导率（W/m·K）:") lowboard_thermal_cond
# b35 = input("材料层厚度（mm）:") lowboard_thickness
# b36 材料层导热截面积  lowboard_cross_area
# 除环境温度b6和空气流速b7以外，其他输入均不为0
# check_list = [b3,b4,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b17,b18,b22,b23,b24,b29,b34,b35]



# 干空气的热物理性质:dry air thermophysical properties chart(DATPC)
# 温度（℃）	运动粘度（m²/s）	流体热导率（W/m*K）	Pr





# class
# pyside6
#
if __name__ == '__main__':

    # gene_dict = {"Qchip": 0.084, "Q1layer": 0.6534, "T0": 25, "air_velocity": 5, "Tjunction": 125,
    #              "chip_length": 0.64, "chip_width": 0.64, "chip_height": 0.33, "substrate_surf_area": 324,
    #              "interface_thermal_cond": 0.026, "interface_thickness": 0, "convection_area": 324,
    #              "lowboard_thermal_cond": 13.5, "lowboard_thickness": 0.4, "lowboard_cross_area": 324,
    #              "husk_res": 0, "board_res": 0, "material_thermal_cond": 150}

    info_dict = {"Q": 0.084, "Qt": 0.6534, "T0": 25, "v0": 5, "a": 0.64, "b": 0.64, "h": 0.33, "Tjmax": 125,
                 "Rjc": 0, "Rjb": 0, "lambda": 150, "A0": 324, "lambda_b": 13.5, "hb": 0.4, "Ab": 324, "S": 324}


    info_list = [[0.6, 324, 0.2], [0, 20, 0.026], [0.1, 10, 1], [0.2, 5, 5], [0.5, 10, 1], [0.2, 5, 2]]

    res = final(info_dict, info_list)
    print(res)




