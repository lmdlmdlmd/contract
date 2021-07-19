# -*- codeing = utf-8 -*-
# @Time : 2021/7/19 15:37
# @Author : songdk
# @File : text.py
# @Software: PyCharm

import os
from docxtpl import DocxTemplate
from docx2pdf import convert

doc = DocxTemplate("demox.docx")
context = {
        'con_num': "431254",
        'area': "96",
        'jf': "西安大明宫家居实业有限公司",
        'yf': "代蕾",
        'shi': "郑州",
        'qu': "中原高新区",
        'hao': "翻斗花园349",
        'dian': "拉面",
        'weizhi': "巴萨",
        'pinpai_1': "康师傅",
        'shangpin_1': "冰红茶",
        'year_1': "2021",
        'mon_1': "7",
        'dar_1': "19",
        'year_2': "2021",
        'mon_2': "7",
        'dar_2': "19",
        'dj_1': "80",
        'hj_1': "328342",
        'hjupper_1': "叁拾贰万捌仟叁佰肆拾贰元整",
        'dj_2': "80",
        'hj_2': "328342",
        'hjupper_2': "叁拾贰万捌仟叁佰肆拾贰元整",
        'dj_3': "80",
        'hj_3': "328342",
        'hjupper_3': "叁拾贰万捌仟叁佰肆拾贰元整",
        'dj_4': "80",
        'hj_4': "328342",
        'hjupper_4': "叁拾贰万捌仟叁佰肆拾贰元整",
        'hj': "3712849",
        'hjupper': "叁佰柒拾壹万贰仟捌佰肆拾玖元整",
        'hjyh': "1689437",
        'hjyhupper': "壹佰陆拾捌万玖仟肆佰叁拾柒元整",
        'fkfs': "分期付款",
        'fkzq': "12",
        'sdj': "5.6",
        'ddj': "0.56",
        'qtfy': "33443",
        'qtfyupper': "叁万叁仟肆佰肆拾叁元整",
        'glbzj': "37298",
        'zlbzj': "374892",
        'jsr_1': "张三",
        'lxdh_1': "17823874178",
        'wechatqq_1': "374291324",
        'email_1': "7324983@379.com",
        'sddz_1': "掉色u分红爱妃阿弗吉尔啊减肥带哦",
        'jsr_2': "张三",
        'lxdh_2': "17823874178",
        'wechatqq_2': "374291324",
        'email_2': "7324983@379.com",
        'sddz_2': "掉色u分红爱妃阿弗吉尔啊减肥带哦",
        'p_contents':[
                {
                        'num':"1",
                        'pinpai_2':"dsafda",
                        'shangpin_2':"hfaofdsa"
                },{
                        'num':"2",
                        'pinpai_2':"hdsaui",
                        'shangpin_2':"hcsdaui"
                },{
                        'num':"3",
                        'pinpai_2':"hdsau",
                        'shangpin_2':"dhsoi"
                }
        ]
    }
doc.render(context)
doc.save("text_1.docx")
convert("A:/contract/text_1.docx","A:/contract/text_1.pdf")
os.remove("A:/contract/text_1.docx")
