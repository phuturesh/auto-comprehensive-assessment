## TJU自动综测
你觉得你的同学们上学期表现都不错, 所以决定给他们打满分 (95).

## Usage
你需要安装selenium, 在命令行中运行:
```shell
pip install selenium
```

**[注意]** 本科生和研究生每年的满分和小项规则不一样, 请根据学院以及年级要求自行调整脚本开头的小项分数grades. 如果你的给分溢出上限会自动取满分, 但要注意这是不是你们学院规定的满分.

如果你没有Chrome, 也可以修改14行附近的代码, 改为ChromiumEdge或者Firefox等浏览器.

现在你只需要在第2行填入你的学号, 然后直接运行脚本即可:
```shell
python3 auto_fill.py
```

## Appendix
如果你从来没有用过python, 使用的还是Windows系统: 在安装python时务必在Optional Features里勾选pip, 这样你才能使用上面的命令安装selenium
