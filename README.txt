background_image: 存放背景图片
code_process: 存放的是生成图片过程中所需要的调用的代码
fonts: 存放的是字体库
gen_text:存放的是调用code_gen_text.py生成的预料文本
output:目录下Images中存放的是调用code_run.py 生成的图片,Labels中存放的是xml格式坐标

code_gen_image.py  # 调用语料生成图片,一图多行文本
code_gen_text.py   # 生成语料文本库
code_run.py        # 通过多线程调用code_gen_image.py生成图片
code_setting.py    # 统一存放文件路径
template.py        # 存放的是模板


执行：
1、生成语料，直接执行code_gen_text.py 即可

2、生成图片
1) 在code_setting.py 中修改template_image值
2) 在code_gen_image.py中修改第36行的template.#，替换# 替换名为 template.py中的模板名;
   同时修改第81行、85行'#_{}.{}' 中 #处内容，即生成图片命名
3) 在code_run.py 中修改第31行 default=10 即，需要生成图片个数，然后执行 code_run.py 即可
