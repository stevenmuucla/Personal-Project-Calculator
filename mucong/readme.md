# 项目使用依赖

Pyside6





gui 是带有可视化界面的。
main是不带的。


打包成一个文件夹
pyinstaller -D --add-data="image;image" -w -i integratedcircuitsics-_1_.ico  gui.py  -p ./ -n chip-thermal


