# contract
首先安装docxtpl和docx2pdf库
pip install docxtpl
pip install docx2pdf
如果下载速度慢可以ctrl+c中止下载使用国内源
pip install docxtpl -i https://pypi.tuna.tsinghua.edu.cn/simple
pip install docx2pdf -i https://pypi.tuna.tsinghua.edu.cn/simple

demo.docx为模板，在模板中使用{{name}}来填充需要填写的内容，name是对所填充地方的命名
在contract.py文件中get_context（）函数中修改相应name对应的值即可。
在兼营商品中循环了{%p python %}格式的代码，同样在填充时要注意体里面的量的名称无需改变
text_1.pdf 为生成文件
