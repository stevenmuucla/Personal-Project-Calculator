# !/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2023/6/29 9:21   xxx      1.0         None
"""
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from chipthermal.ui.form_ui import Ui_Form
from chipthermal.func.func import final
from openpyxl import Workbook


class Form(QWidget, Ui_Form):

    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)

        self.init_ui()
        self.export_num = 0
        self.cal_time = 0
        self.export_to_excel = [["次数", self.label_21.text(), self.label_23.text(), self.label_22.text(),
                                 self.label_24.text(), self.label_13.text(), self.label_25.text(),
                                 self.label_31.text(), self.label_32.text(), self.label_33.text(), self.label_34.text()]]
        self.pushButton.clicked.connect(self.write_list_to_excel)
        self.pushButton_2.clicked.connect(self.calc)

        self.pixmap1 = QPixmap(':/img/image/1.png').scaled(682, 291)
        # self.pixmap1 = QPixmap('./image/1.png').scaledToWidth(320)
        # self.pixmap1 = QPixmap('./image/1.png').scaled(self.label.size())
        self.pixmap2 = QPixmap(':/img//image/2.png').scaled(682, 291)
        self.pixmap3 = QPixmap(':/img/image/3.png').scaled(682, 291)

        self.label_35.setPixmap(self.pixmap1)
        self.label_35.setScaledContents(True)

        # self.toolButton_add.setText("+")
        # self.toolButton_add.clicked.connect(self.add_row)
        # self.toolButton_min.clicked.connect(self.min_row)
        # self.toolButton_min.setText("-")
        self.row_list = []
        # self.row_num = 0
        self.checkBox2.clicked.connect(self.button2)
        self.checkBox2.setChecked(False)
        self.checkBox3.clicked.connect(self.button3)
        self.checkBox3.setChecked(False)
        self.checkBox3.hide()
        self.label_50.hide()
        self.label_51.hide()
        self.label_52.hide()
        self.label_53.hide()
        self.label_54.hide()
        self.label_55.hide()
        self.label_56.hide()
        self.label_57.hide()
        self.label_58.hide()
        self.label_59.hide()
        self.label_60.hide()
        self.label_61.hide()
        self.lineEdit_11.hide()
        self.lineEdit_12.hide()
        self.lineEdit_13.hide()
        self.lineEdit_14.hide()
        self.lineEdit_15.hide()
        self.lineEdit_16.hide()
        self.lineEdit_17.hide()
        self.lineEdit_18.hide()
        self.lineEdit_19.hide()
        self.lineEdit_20.hide()
        self.lineEdit_21.hide()
        self.lineEdit_22.hide()
        self.comboBox.currentIndexChanged.connect(self.EdcomboBox)
        self.comboBox.highlighted.connect(self.EdcomboBox)
        self.comboBox.hide()
        # self.lineEdit_11.setText("")
        # self.lineEdit_12.setText("")
        # self.lineEdit_13.setText("")
        # self.lineEdit_14.setText("")
        # self.lineEdit_15.setText("")
        # self.lineEdit_16.setText("")
        # self.lineEdit_17.setText("")
        # self.lineEdit_18.setText("")
        # self.lineEdit_19.setText("")
        # self.lineEdit_20.setText("")
        # self.lineEdit_21.setText("")
        # self.lineEdit_22.setText("")

        # self.lineEdit_Q.setText("0.084")
        # self.lineEdit_Qt.setText("0.6534")
        # self.lineEdit_T0.setText("25")
        # self.lineEdit_v0.setText("5")
        # self.lineEdit_a.setText("0.64")
        # self.lineEdit_b.setText("0.64")
        # self.lineEdit_h.setText("0.33")
        # self.lineEdit_Tjmax.setText("125")
        # # self.lineEdit_Rjc.setText("0")
        # # self.lineEdit_Rjb.setText("0")
        # self.lineEdit_lambda.setText("150")
        # self.lineEdit_A0.setText("324")
        # self.lineEdit_lambda_b.setText("13.5")
        # self.lineEdit_hb.setText("0.8")
        # self.lineEdit_Ab.setText("324")
        # self.lineEdit_S.setText("324")
        # self.lineEdit_h1.setText("1")
        # self.lineEdit_A1.setText("1")
        # self.lineEdit_lambda1.setText("1")
        # self.lineEdit_hTIM1.setText("1")
        # self.lineEdit_ATIM1.setText("1")
        # self.lineEdit_lambdaTIM1.setText("1")

        self.lineEdit.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_2.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_3.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_4.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_5.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_6.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_7.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_8.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_9.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑
        self.lineEdit_10.setFocusPolicy(Qt.NoFocus)  # 设置不可编辑

    # def get_row_data(self):
    #     # [[[A1,B1,C1],[A2,B2,C2]] ]
    #     return [[j.text() for j in i] for i in self.row_list]

    def init_ui(self):
        self.label_40.setText(QCoreApplication.translate("Form", u"\u53d1\u70ed\u91cf\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u82af\u7247\u53d1\u70ed\u91cfQ(W)", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5355\u5c42\u57fa\u677f\u4e0a\u6240\u6709\u82af\u7247\u7684\u603b\u53d1\u70ed\u91cfQ\u209c\uff08W\uff09", None))
        self.label_10.setText("")
        self.label_29.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u6761\u4ef6\uff1a", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u73af\u5883\u7a7a\u6c14\u6e29\u5ea6T\u2080\uff08\u2103\uff09", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u7a7a\u6c14\u6765\u6d41\u901f\u5ea6v\u2080\uff08m/s\uff09", None))
        self.label_14.setText("")
        self.label_26.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7684\u8f93\u5165\u53c2\u6570\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u957fa\uff08mm\uff09", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u5bbdb\uff08mm\uff09", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u9ad8h\uff08mm\uff09", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7ed3\u8282\u7684\u6700\u9ad8\u8bb8\u7528\u6e29\u5ea6Tjmax\uff08\u2103\uff09", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7684\u7ed3\u8282-\u4e0a\u76d6\u70ed\u963bR\u2c7c\u03f2\uff08\u2103/W\uff09", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7684\u7ed3\u8282-\u57fa\u677f\u70ed\u963bR\u2c7c\u044c\uff08\u2103/W\uff09", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"\u672a\u63d0\u4f9b2\u70ed\u963b\u7684\u60c5\u51b5\u4e0b\u9700\u63d0\u4f9b\uff1a", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u6750\u6599\u70ed\u5bfc\u7387\u03bb\uff08W/m\u00b7\u2103\uff09", None))
        self.label_15.setText("")
        self.label_28.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u57fa\u677f\u7684\u8f93\u5165\u53c2\u6570\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u4e0e\u73af\u5883\u7a7a\u6c14\u63a5\u89e6\u7684\u8868\u9762\u79efA\u2080\uff08mm\u00b2\uff09", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u6750\u6599\u7684\u70ed\u5bfc\u7387\u03bb\u044c\uff08W/m\u00b7K\uff09", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u7684\u539a\u5ea6h\u044c\uff08mm\uff09", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u63a5\u89e6\u7a7a\u6c14\u7684\u8868\u9762\u79efA\u044c\uff08mm\u00b2\uff09", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u8868\u9762\u79efS(mm\u00b2)", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.checkBox2.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6750\u65992\u53ca\u754c\u9762\u6750\u65992", None))
        self.checkBox3.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u6750\u65993\u53ca\u754c\u9762\u6750\u65993", None))
        self.label_44.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u7684\u539a\u5ea6h\u2081\uff08mm\uff09", None))
        self.label_45.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u7684\u5bfc\u70ed\u622a\u9762\u79efA\u2081\uff08mm\u00b2\uff09", None))
        self.label_46.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u7684\u70ed\u5bfc\u7387\u03bb\u2081\uff08W/m\u00b7K\uff09", None))
        self.label_47.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c421\u7684\u539a\u5ea6h\u0442\u03b9\u043c\u2081\uff08mm\uff09", None))
        self.label_48.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c421\u5185\u4fa7\u7684\u63a5\u89e6\u9762\u79efA\u0442\u03b9\u043c\u2081\uff08mm\u00b2\uff09", None))
        self.label_49.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65991\u7684\u70ed\u5bfc\u7387\u03bb\u0442\u03b9\u043c\u2081\uff08W/m\u00b7K\uff09", None))
        self.label_50.setText(QCoreApplication.translate("Form", u"\u6750\u65992\u7684\u539a\u5ea6h\u2082\uff08mm\uff09", None))
        self.label_51.setText(QCoreApplication.translate("Form", u"\u6750\u65992\u7684\u5bfc\u70ed\u622a\u9762\u79efA\u2082\uff08mm\u00b2\uff09", None))
        self.label_52.setText(QCoreApplication.translate("Form", u"\u6750\u65992\u7684\u70ed\u5bfc\u7387\u03bb\u2082\uff08W/m\u00b7K\uff09", None))
        self.label_53.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c422\u7684\u539a\u5ea6h\u0442\u03b9\u043c\u2082\uff08mm\uff09", None))
        self.label_54.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c422\u5185\u4fa7\u7684\u63a5\u89e6\u9762\u79efA\u0442\u03b9\u043c\u2082\uff08mm\u00b2\uff09", None))
        self.label_55.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65992\u7684\u70ed\u5bfc\u7387\u03bb\u0442\u03b9\u043c\u2082\uff08W/m\u00b7K\uff09", None))
        self.label_56.setText(QCoreApplication.translate("Form", u"\u6750\u65993\u7684\u539a\u5ea6h\u2083\uff08mm\uff09", None))
        self.label_57.setText(QCoreApplication.translate("Form", u"\u6750\u65993\u7684\u5bfc\u70ed\u622a\u9762\u79efA\u2083\uff08mm\u00b2\uff09", None))
        self.label_58.setText(QCoreApplication.translate("Form", u"\u6750\u65993\u7684\u70ed\u5bfc\u7387\u03bb\u2083\uff08W/m\u00b7K\uff09", None))
        self.label_59.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c423\u7684\u539a\u5ea6h\u0442\u03b9\u043c\u2083\uff08mm\uff09", None))
        self.label_60.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u6599\u5c423\u5185\u4fa7\u7684\u63a5\u89e6\u9762\u79efA\u0442\u03b9\u043c\u2083\uff08mm\u00b2\uff09", None))
        self.label_61.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65993\u7684\u70ed\u5bfc\u7387\u03bb\u0442\u03b9\u043c\u2083\uff08W/m\u00b7K\uff09", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u7ed3\u679c", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"\u63a5\u89e6\u73af\u5883\u7a7a\u6c14\u7684\u6750\u65991\u8868\u9762\u6e29\u5ea6T\u2081\u208b\u2080 \uff08\u2103\uff09", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"\u6750\u65991\u4e0e\u754c\u9762\u6750\u65991\u63a5\u89e6\u9762\u6e29\u5ea6T\u0442\u03b9\u043c\u2081\u208b\u2081 \uff08\u2103\uff09", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"\u6750\u65992\u4e0e\u754c\u9762\u6750\u65991\u63a5\u89e6\u9762\u6e29\u5ea6T\u2082\u208b\u0442\u03b9\u043c\u2081\uff08\u2103\uff09", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65992\u4e0e\u6750\u65992\u63a5\u89e6\u9762\u6e29\u5ea6T\u0442\u03b9\u043c\u2082\u208b\u2082 \uff08\u2103\uff09", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"\u6750\u65993\u4e0e\u754c\u9762\u6750\u65992\u63a5\u89e6\u9762\u6e29\u5ea6T\u2083\u208b\u0442\u03b9\u043c\u2082\uff08\u2103\uff09", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"\u754c\u9762\u6750\u65993\u4e0e\u6750\u65993\u63a5\u89e6\u9762\u6e29\u5ea6T\u0442\u03b9\u043c\u2083\u208b\u2083\uff08\u2103\uff09", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u58f3\u4f53\u4e0a\u8868\u9762\u6e29\u5ea6Tc\uff08\u2103\uff09", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"\u82af\u7247\u7ed3\u8282\u6e29\u5ea6\u8ba1\u7b97\u503cT\u2c7c\uff08\u2103\uff09", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u4e0e\u82af\u7247\u63a5\u89e6\u9762\u7684\u6e29\u5ea6T\u2c7c\u208b\u044c\uff08\u2103\uff09", None))
        self.label_34.setText(QCoreApplication.translate("Form", u"\u57fa\u677f\u63a5\u89e6\u7a7a\u6c14\u7684\u4e0b\u8868\u9762\u6e29\u5ea6T\u044c\u208b\u2080\uff08\u2103\uff09", None))


    def calc(self):
        info_dict = {"Q": self.lineEdit_Q.text(), "Qt":self.lineEdit_Qt.text(),
                     "T0": self.lineEdit_T0.text(),  "v0": self.lineEdit_v0.text(),
                     "a": self.lineEdit_a.text(), "b": self.lineEdit_b.text(),
                     "h": self.lineEdit_h.text(), "Tjmax": self.lineEdit_Tjmax.text(),
                     "Rjc": self.lineEdit_Rjc.text(), "Rjb": self.lineEdit_Rjb.text(),
                     "lambda": self.lineEdit_lambda.text(), "A0": self.lineEdit_A0.text(),
                     "lambda_b": self.lineEdit_lambda_b.text(), "hb": self.lineEdit_hb.text(),
                     "Ab": self.lineEdit_Ab.text(), "S": self.lineEdit_S.text(),
                     "h1": self.lineEdit_h1.text(), "A1": self.lineEdit_A1.text(),
                     "lambda1": self.lineEdit_lambda1.text(), "hTIM1": self.lineEdit_hTIM1.text(),
                     "ATIM1": self.lineEdit_ATIM1.text(), "lambdaTIM1": self.lineEdit_lambdaTIM1.text()}
        name_dict = {"Q": "目标芯片发热量", "Qt": "单层基板上所有芯片的总发热量", "T0": "环境空气温度", "v0": "空气来流速度",
                     "a": "芯片长", "b": "芯片宽", "h": "芯片高", "Tjmax": "芯片结节的最高许用温度", "Rjc": "芯片的结节-上盖热阻",
                     "Rjb": "芯片的结节-基板热阻", "lambda": "芯片材料热导率", "A0": "材料1的对流换热表面积",
                     "lambda_b": "基板材料的热导率", "hb": "基板的厚度", "Ab": "基板接触空气的表面积", "S": "基板表面积",
                     "h1": "材料1的厚度（mm）", "A1": "材料1的导热截面积（mm²）", "lambda1": "材料1的热导率",
                     "hTIM1": "界面材料层1的厚度（mm）", "ATIM1": "界面材料层1内侧的接触面积（mm²）", "lambdaTIM1": "界面材料1的热导率"}

        msg = QMessageBox()

        try:
            for i in info_dict:
                if i not in ["Rjc", "Rjb", "lambda"]:
                    info_dict[i] = float(info_dict[i])
                elif info_dict[i] != "":
                    info_dict[i] = float(info_dict[i])
            self.get_values()
            new_row_list = self.row_list
            temp_list = [[info_dict["h1"], info_dict["A1"], info_dict["lambda1"]],
                         [info_dict["hTIM1"], info_dict["ATIM1"], info_dict["lambdaTIM1"]]]
            try:
                for i, list_i in enumerate(new_row_list):
                    for j, list_j in enumerate(list_i):
                        new_row_list[i][j] = float(list_j)
                        if new_row_list[i][j] == 0:
                            raise EOFError
                results = final(info_dict, temp_list + new_row_list)

                if results == [-1]:
                    msg.critical(self, "Error", '重新填写芯片的结节-上盖热阻，芯片的结节-基板热阻，或芯片材料热导率')
                    msg.show()

                elif len(results) == 2:
                    msg.critical(self, "Error", f'请确认{name_dict[results[1]]}，确保该项是不为0的数字')
                    msg.show()

                # elif results == [-3]:
                #     msg.critical(self, "Error", "额外材料数据不为0")
                #     msg.show()

                elif results == [-4]:
                    msg.critical(self, "Error", "环境温度超出范围")
                    msg.show()

                elif results == [-5]:
                    msg.critical(self, "Error", "芯片发热量不能大于总发热量")
                    msg.show()

                elif results == [-6]:
                    msg.critical(self, "Error", "芯片发热量过大")
                    msg.show()

                elif results == [-7]:
                    msg.critical(self, "Error", "计算中芯片温度过高，请检查数据")
                    msg.show()

                elif results == [-8]:
                    msg.critical(self, "Error", "空气来流速度不得小于0.01m/s")
                    msg.show()

                else:
                    for i in range(len(results)):
                        results[i] = "%.1f" % results[i]
                    T1_0, Ttim1_1, T2_tim1, Ttim2_2, T3_tim2, Ttim3_3, Tc, Tj, Tj_b, Tb_0 = results
                    self.lineEdit.setText(str(T1_0))
                    self.lineEdit_2.setText(str(Ttim1_1))
                    self.lineEdit_3.setText(str(T2_tim1))
                    self.lineEdit_4.setText(str(Ttim2_2))
                    self.lineEdit_5.setText(str(T3_tim2))
                    self.lineEdit_6.setText(str(Ttim3_3))
                    self.lineEdit_7.setText(str(Tc))
                    self.lineEdit_8.setText(str(Tj))
                    self.lineEdit_9.setText(str(Tj_b))
                    self.lineEdit_10.setText(str(Tb_0))
                    self.cal_time += 1
                    results.insert(0, f"第{self.cal_time}次计算结果")
                    self.export_to_excel.append(results)


            except Exception as e:
                if i == 0:
                    if j == 0:
                        msg.critical(self, "Error", f'请确认材料2的厚度（mm），确保该项是不为0的数字')
                        msg.show()
                    if j == 1:
                        msg.critical(self, "Error", f'请确认材料2的导热截面积（mm²），确保该项是不为0的数字')
                        msg.show()
                    if j == 2:
                        msg.critical(self, "Error", f'请确认材料2的热导率，确保该项是不为0的数字')
                        msg.show()
                if i == 1:
                    if j == 0:
                        msg.critical(self, "Error", f'请确认界面材料层2的厚度（mm），确保该项是不为0的数字')
                        msg.show()
                    if j == 1:
                        msg.critical(self, "Error", f'请确认界面材料层2内侧的接触面积（mm²），确保该项是不为0的数字')
                        msg.show()
                    if j == 2:
                        msg.critical(self, "Error", f'请确认界面材料2的热导率，确保该项是不为0的数字')
                        msg.show()
                if i == 2:
                    if j == 0:
                        msg.critical(self, "Error", f'请确认材料3的厚度（mm），确保该项是不为0的数字')
                        msg.show()
                    if j == 1:
                        msg.critical(self, "Error", f'请确认材料3的导热截面积（mm²），确保该项是不为0的数字')
                        msg.show()
                    if j == 2:
                        msg.critical(self, "Error", f'请确认材料3的热导率，确保该项是不为0的数字')
                        msg.show()
                if i == 3:
                    if j == 0:
                        msg.critical(self, "Error", f'请确认界面材料层3的厚度（mm），确保该项是不为0的数字')
                        msg.show()
                    if j == 1:
                        msg.critical(self, "Error", f'请确认界面材料层3内侧的接触面积（mm²），确保该项是不为0的数字')
                        msg.show()
                    if j == 2:
                        msg.critical(self, "Error", f'请确认界面材料3的热导率，确保该项是不为0的数字')
                        msg.show()

        except Exception as e:
            # print(e)
            if i not in ["Rjc", "Rjb", "lambda"]:
                msg.critical(self, "Error", f'请确认{name_dict[i]},确保该项为数字')
                msg.show()
            else:
                msg.critical(self, "Error", f"请确认{name_dict[i]}，填写不为0的数字。该项若无应不填。")


    # def get_double(self):
    #     box = QLineEdit()
    #     return box


    # def add_row(self):
    #     if self.row_num < 2:
    #         row_list = []
    #         row_list_2 = []
    #         row_list.append(self.get_double())
    #         row_list.append(self.get_double())
    #         row_list.append(self.get_double())
    #         row_list_2.append(self.get_double())
    #         row_list_2.append(self.get_double())
    #         row_list_2.append(self.get_double())
    #         self.row_list.append(row_list)
    #         self.row_list.append(row_list_2)
    #         self.row_num += 1
    #         self.formLayout_4.addRow(f'材料{int(self.row_num)+1}的厚度h{int(self.row_num)+1}（mm）', row_list[0])
    #         self.formLayout_4.addRow(f'材料{int(self.row_num)+1}的导热截面积A{int(self.row_num)+1}（mm²）', row_list[1])
    #         self.formLayout_4.addRow(f'材料{int(self.row_num)+1}的热导率λ{int(self.row_num)+1}（W/m·K）', row_list[2])
    #         self.formLayout_4.addRow(f'界面材料层{int(self.row_num)+1}的厚度hTIM{int(self.row_num)+1}（mm）', row_list_2[0])
    #         self.formLayout_4.addRow(f'界面材料层{int(self.row_num)+1}内侧的接触面积ATIM{int(self.row_num)+1}（mm²）', row_list_2[1])
    #         self.formLayout_4.addRow(f'界面材料{int(self.row_num)+1}的热导率λTIM{int(self.row_num)+1}（W/m·K）', row_list_2[2])


    # def min_row(self):
    #     if self.row_list != []:
    #         self.row_list.pop()
    #         self.row_list.pop()
    #     self.formLayout_4.removeRow(self.row_num * 6 - 1)
    #     self.formLayout_4.removeRow(self.row_num * 6 - 2)
    #     self.formLayout_4.removeRow(self.row_num * 6 - 3)
    #     self.formLayout_4.removeRow(self.row_num * 6 - 4)
    #     self.formLayout_4.removeRow(self.row_num * 6 - 5)
    #     self.formLayout_4.removeRow(self.row_num * 6 - 6)
    #     if self.row_num > 0:
    #         self.row_num -= 1


    def write_list_to_excel(self):
        self.export_num += 1
        # 创建一个新的Excel工作簿
        workbook = Workbook()
        # 获取活动的工作表
        worksheet = workbook.active
        # 写入字典的键作为表头
        for i in self.export_to_excel:
            worksheet.append(i)
        try:
            workbook.save(f"计算结果 {self.export_num}")

        except Exception as e:
            msg = QMessageBox()
            msg.critical(self, "Error", "文件名重复")
            msg.show()


    def button2(self):
        if self.checkBox2.isChecked() == True:
            self.label_50.show()
            self.label_51.show()
            self.label_52.show()
            self.label_53.show()
            self.label_54.show()
            self.label_55.show()
            self.lineEdit_11.show()
            self.lineEdit_12.show()
            self.lineEdit_13.show()
            self.lineEdit_14.show()
            self.lineEdit_15.show()
            self.lineEdit_16.show()
            self.label_35.setPixmap(self.pixmap2)
            self.label_35.setScaledContents(True)
            self.checkBox3.show()
            self.comboBox.show()
        else:
            if self.checkBox3.isChecked() == True:
                self.checkBox3.setChecked(False)
                self.button3()
            self.checkBox3.hide()
            self.lineEdit_11.hide()
            self.lineEdit_12.hide()
            self.lineEdit_13.hide()
            self.lineEdit_14.hide()
            self.lineEdit_15.hide()
            self.lineEdit_16.hide()
            self.label_50.hide()
            self.label_51.hide()
            self.label_52.hide()
            self.label_53.hide()
            self.label_54.hide()
            self.label_55.hide()
            self.label_35.setPixmap(self.pixmap1)
            self.label_35.setScaledContents(True)
            self.comboBox.hide()



    def button3(self):
        if self.checkBox3.isChecked() == True:
            self.label_56.show()
            self.label_57.show()
            self.label_58.show()
            self.label_59.show()
            self.label_60.show()
            self.label_61.show()
            self.lineEdit_17.show()
            self.lineEdit_18.show()
            self.lineEdit_19.show()
            self.lineEdit_20.show()
            self.lineEdit_21.show()
            self.lineEdit_22.show()
            self.label_35.setPixmap(self.pixmap3)
            self.label_35.setScaledContents(True)
        else:
            self.lineEdit_17.hide()
            self.lineEdit_18.hide()
            self.lineEdit_19.hide()
            self.lineEdit_20.hide()
            self.lineEdit_21.hide()
            self.lineEdit_22.hide()
            self.label_56.hide()
            self.label_57.hide()
            self.label_58.hide()
            self.label_59.hide()
            self.label_60.hide()
            self.label_61.hide()
            self.label_35.setPixmap(self.pixmap2)
            self.label_35.setScaledContents(True)


    def get_values(self):
        self.row_list = []
        if self.checkBox2.isChecked() == True:
            self.row_list.append([self.lineEdit_11.text(), self.lineEdit_12.text(), self.lineEdit_13.text()])
            self.row_list.append([self.lineEdit_14.text(), self.lineEdit_15.text(), self.lineEdit_16.text()])
            if self.checkBox3.isChecked() == True:
                self.row_list.append([self.lineEdit_17.text(), self.lineEdit_18.text(), self.lineEdit_19.text()])
                self.row_list.append([self.lineEdit_20.text(), self.lineEdit_21.text(), self.lineEdit_22.text()])


    def EdcomboBox(self):
        # self.comboBox.currentIndexChanged["默认"].connect(self.Edcoefficient(-1))
        # self.comboBox.currentIndexChanged["清空"].connect(self.Edcoefficient(0))
        print(self.comboBox.currentIndex())
        if self.comboBox.currentIndex() == 3:
            self.lineEdit_11.setText("")
            self.lineEdit_12.setText("")
            self.lineEdit_13.setText("")
            self.lineEdit_14.setText("")
            self.lineEdit_15.setText("")
            self.lineEdit_16.setText("")

        elif self.comboBox.currentIndex() == 1:
            self.lineEdit_11.setText("1")
            self.lineEdit_12.setText("1")
            self.lineEdit_13.setText("1")
            self.lineEdit_14.setText("1")
            self.lineEdit_15.setText("1")
            self.lineEdit_16.setText("1")
        elif self.comboBox.currentIndex() == 2:
            self.lineEdit_11.setText("2")
            self.lineEdit_12.setText("2")
            self.lineEdit_13.setText("2")
            self.lineEdit_14.setText("2")
            self.lineEdit_15.setText("2")
            self.lineEdit_16.setText("2")


        # self.comboBox.activated.connect(self.Edcoefficient(0))
        # self.comboBox.currentTextChanged[str].connect(self.Edcoefficient(1))
        # self.comboBox.currentTextChanged[str].connect(self.Edcoefficient(2))
        # self.comboBox.currentIndexChanged[int].connect(self.Edcoefficient(3))


    # def Edcoefficient(self, coef):
    #     if coef == 0:
    #     elif coef == 1:
    #         pass
    #
    #     elif coef == 2:
