import code_setting as _path

invoice_electronic = {
    "bank_ground": _path.template_invoice_elc,
    "key_1": {  # 大标题	北京增值税电子发票
        "text": _path.text_inc_large_title,
        "font_type": [_path.font_elc_kai],
        "font_size": [36, 28],
        "font_color": ['#8d6649', '#805332', '#914d17', '#9d5224'],
        "count": 3
    },
    "key_2": {  # 标题,标签		表格内的名称等、表格下的审核人等、表格上的机器编号等
        "text": _path.text_inc_label,
        "font_type": [_path.font_elc_hei, _path.font_elc_song],
        "font_size": [14],
        "font_color": ['#8d6649', '#805332', '#914914', '#af724d', '#9d5224'],
        "count": 42
    },
    "value_1": {  # 纯汉字填写的内容:  公司名称，大写金额，审核人等人名等
        "text": _path.text_inc_company,
        "font_type": [_path.font_elc_song],
        "font_size": [14, 9],
        "font_color": ['#444444', '#020202'],
        "count": 6
    },
    "value_2": {  # 纯汉字填写的内容:  公司名称，大写金额，审核人等人名等
        "text": _path.text_inc_large_amount,
        "font_type": [_path.font_elc_song],
        "font_size": [14, 9],
        "font_color": ['#444444', '#020202'],
        "count": 6
    },
    "value_3": {  # 纯汉字填写的内容:  公司名称，大写金额，审核人等人名等
        "text": _path.text_inc_name,
        "font_type": [_path.font_elc_song],
        "font_size": [14, 9],
        "font_color": ['#444444', '#020202'],
        "count": 6
    },
    "value_4": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_machine,  # 语料-机器码
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 4
    },
    "value_5": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_code,  # 语料-发票代码
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 4
    },
    "value_6": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_number,  # 语料-发票号码
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 4
    },
    "value_7": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_nums,  # 语料-数量
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 8
    },
    "value_8": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_total,  # 语料-总价
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 8
    },
    "value_9": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_price,  # 语料-单价
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 8
    },
    "value_10": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_rate,  # 语料-税率
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 8
    },
    "value_11": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_id,  # 语料-纳税人识别号
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 4
    },
    "value_12": {  # 数字、字母、符号混合但字体同一的内容   机器编号、发票代码、发票号码、单价、数量、金额、税率、税额、纳税人识别号、总金额、总税额、总价
        "text": _path.text_inc_pwd,  # 语料-密码区
        "font_type": [_path.font_elc_arial],
        "font_size": [14],
        "font_color": ['#444444', '#020202'],
        "count": 2
    },
    "mixed_1": {  # 汉字和数字混合    地址电话，开户行及账号、开票日期等
        "text": _path.text_inc_address,
        "font_type": {0: [_path.font_elc_song], 1: [_path.font_elc_arial]},
        "font_size": {0: [14, 9], 1: [14, 9]},
        "font_color": {0: ['#444444', '#020202'], 1: ['#444444', '#020202']},
        "count": 4
    },
    "mixed_2": {  # 汉字和数字混合    地址电话，开户行及账号、开票日期等
        "text": _path.text_inc_account,
        "font_type": {0: [_path.font_elc_song], 1: [_path.font_elc_arial], 2: [_path.font_elc_arial]},
        "font_size": {0: [14, 9], 1: [14, 9], 2: [14, 9]},
        "font_color": {0: ['#444444', '#020202'], 1: ['#444444', '#020202'], 2: ['#444444', '#020202']},
        "count": 4
    },
    "mixed_3": {  # 汉字和数字混合    地址电话，开户行及账号、开票日期等
        "text": _path.text_inc_time,
        "font_type": {0: [_path.font_elc_song], 1: [_path.font_elc_arial]},
        "font_size": {0: [14, 9], 1: [14, 9]},
        "font_color": {0: ['#444444', '#020202'], 1: ['#444444', '#020202']},
        "count": 4
    },
}
invoice_paper = {
    "bank_ground": _path.template_invoice_paper,
    "key_1": {  # 大标题	北京增值税纸质发票
        "text": _path.text_inc_large_title,  # 语料-大标题
        "font_type": [_path.font_pa_kai],
        "font_size": [36, 48],
        "font_color": ['#9a8779', '#a28273', '#9f8574', '#2f5540', '#394e3d'],
        "count": 2
    },
    "key_2": {  # 标题,标签		表格内的名称等、表格下的审核人等、表格上的机器编号等
        "text": _path.text_inc_label,  # 语料-标签
        "font_type": [_path.font_pa_kai],
        "font_size": [14, 24],
        "font_color": ['#9a8779', '#a28273', '#9f8574', '#2f5540', '#394e3d'],
        "count": 42
    },
    "value_1": {  # 所有的填写内容
        "text": _path.text_inc_large_amount,  # 语料-大写金额
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 4
    },
    "value_2": {  # 所有的填写内容
        "text": _path.text_inc_price,  # 语料-单价
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 4
    },
    "value_3": {  # 所有的填写内容
        "text": _path.text_inc_address,  # 语料-地址电话
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    }, "value_4": {  # 所有的填写内容
        "text": _path.text_inc_code,  # 语料-发票代码
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
    "value_5": {  # 所有的填写内容
        "text": _path.text_inc_number,  # 语料-发票号码
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    }, "value_6": {  # 所有的填写内容
        "text": _path.text_inc_company,  # 语料-公司名称
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    }, "value_7": {  # 所有的填写内容
        "text": _path.text_inc_machine,  # 语料-机器码
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
    "value_8": {  # 所有的填写内容
        "text": _path.text_inc_account,  # 语料-开户行及账号
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
    "value_9": {  # 所有的填写内容
        "text": _path.text_inc_time,  # 语料-开票时间
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    }, "value_10": {  # 所有的填写内容
        "text": _path.text_inc_pwd,  # 语料-密码区
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
    "value_11": {  # 所有的填写内容
        "text": _path.text_inc_id,  # 语料-纳税人识别号
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
    "value_12": {  # 所有的填写内容
        "text": _path.text_inc_name,  # 语料-人名
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
    "value_13": {  # 所有的填写内容
        "text": _path.text_inc_nums,  # 语料-数量
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
    "value_14": {  # 所有的填写内容
        "text": _path.text_inc_rate,  # 语料-税率
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
    "value_15": {  # 所有的填写内容
        "text": _path.text_inc_total,  # 语料-总价
        "font_type": [_path.font_pa_xinsong, _path.font_pa_songjian],
        "font_size": [22, 28, 18],
        "font_color": ['#668ed6', '#4a6dc1', '#042487', '#4d6080', '#505b7b'],
        "count": 2
    },
}
license_ticket = {
    "bank_ground": _path.template_license_image,
    "key_1": {  # 大标题
        "text": _path.text_lic_large_title,
        "font_type": [_path.font_lic_hei],
        "font_size": [90, 150, 48],
        "font_color": ['#5d663b', '#4e5a28', '#fee80d', '#3c2807', '#1d2a19', '#222009', '#42361e', '#524324',
                       '#685334'],
        "count": 2
    },
    "key_2": {  # 标题,例如名称、住所、注册资金等
        "text": _path.text_lic_label,
        "font_type": [_path.font_lic_hei, _path.font_lic_song],
        "font_size": [26, 11, 44],
        "font_color": ['#05060b', '#100f0d', '#07060c', '#595a55', '#2d2e33', '#403f3b', '#262626', '#6e7075',
                       '#41454c', '#61625d', '#686964'],
        "count": 6
    },
    "key_3": {  # 执照上的温馨提示
        "text": _path.text_lic_key_note,
        "font_type": [_path.font_lic_song],
        "font_size": [11],
        "font_color": ['#5a5a5a', '#bcbcbc', '#262626', '#676767'],
        "count": 1,
    },
    "key_4": {  # 二维码右边的提示和下面的脚注
        "text": _path.text_lic_annotation,
        "font_type": [_path.font_lic_jian, _path.font_lic_song],
        "font_size": [13, 6, 12],
        "font_color": ['#080000', '#3a3a3a', '#3e3f3a', '#5a5b56', '#9a9e9c', '#767a85', '#848887', '#150a28',
                       '#120701', '#000400'],
        "count": 2,
    },
    "value_1": {  # 落款:某某市管理
        "text": _path.text_lic_foot_note,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian],
        "font_size": [21, 20, 12],
        "font_color": ['#303136', '#282828', '#212121', '#2e2e2e', '#3b3b3b', '#3e3e3e', '#1c0309', '#281b32',
                       '#110b0f'],
        "count": 2,
    },
    "value_2": {  # 信用代码：18位字母数字、证书编号：20位编号、注册号：15位数字
        "text": _path.text_lic_lang_num,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian],
        "font_size": [21, 20, 12],
        "font_color": ['#303136', '#282828', '#212121', '#2e2e2e', '#3b3b3b', '#3e3e3e', '#1c0309', '#281b32',
                       '#110b0f'],
        "count": 2,
    },
    "value_3": {  # 填写的主题内容：公司名、注册时间等
        "text": _path.text_lic_register_date,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song],
        "font_size": [18, 24, 11],
        "font_color": ['#4b4b4b', '#393939', '#262626', '#060100', '#090002', '#040406', '#a3a5a0', '#35363b',
                       '#666863'],
        "count": 2,
    },
    "value_4": {  # 填写的主题内容：公司名、注册时间等
        "text": _path.text_lic_name,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song],
        "font_size": [18, 24, 11],
        "font_color": ['#4b4b4b', '#393939', '#262626', '#060100', '#090002', '#040406', '#a3a5a0', '#35363b',
                       '#666863'],
        "count": 2,
    },
    "value_5": {  # 填写的主题内容：公司名、注册时间等
        "text": _path.text_lic_company_type,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song],
        "font_size": [18, 24, 11],
        "font_color": ['#4b4b4b', '#393939', '#262626', '#060100', '#090002', '#040406', '#a3a5a0', '#35363b',
                       '#666863'],
        "count": 2,
    },
    "value_6": {  # 填写的主题内容：公司名、注册时间等
        "text": _path.text_lic_company_name,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song],
        "font_size": [18, 24, 11],
        "font_color": ['#4b4b4b', '#393939', '#262626', '#060100', '#090002', '#040406', '#a3a5a0', '#35363b',
                       '#666863'],
        "count": 1,
    },
    "value_7": {  # 填写的主题内容：公司名、注册时间等
        "text": _path.text_lic_date_limit,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song],
        "font_size": [18, 24, 11],
        "font_color": ['#4b4b4b', '#393939', '#262626', '#060100', '#090002', '#040406', '#a3a5a0', '#35363b',
                       '#666863'],
        "count": 2,
    },
    "value_8": {  # 填写的主题内容：公司名、注册时间等
        "text": _path.text_lic_address,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song],
        "font_size": [18, 24, 11],
        "font_color": ['#4b4b4b', '#393939', '#262626', '#060100', '#090002', '#040406', '#a3a5a0', '#35363b',
                       '#666863'],
        "count": 1,
    },
    "value_9": {  # 填写的主题内容：公司名、注册时间等
        "text": _path.text_lic_amount,
        "font_type": [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song],
        "font_size": [18, 24, 11],
        "font_color": ['#4b4b4b', '#393939', '#262626', '#060100', '#090002', '#040406', '#a3a5a0', '#35363b',
                       '#666863'],
        "count": 2,
    },
    "mixed_1": {  # 落款日期 二〇一九年一月十一日
        "text": _path.text_lic_large_date,
        "font_type": {0: [_path.font_lic_hei], 1: [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song]},
        "font_size": {0: [20, 28, 14, 18], 1: [20, 28, 14, 18]},
        "font_color": {0: ['#292929', '#3b3b3b', '#474747', '#06060e', '#0b0300', '#090907', '#696b66', '#44443f',
                           '#84817a', '#3c3c3a', '#4e4e4c'],
                       1: ['#292929', '#3b3b3b', '#474747', '#06060e', '#0b0300', '#090907', '#696b66', '#44443f',
                           '#84817a', '#3c3c3a', '#4e4e4c']},
        "count": 2,
    },
    "mixed_2": {  # 2019年1月11日
        "text": _path.text_lic_small_date,
        "font_type": {0: [_path.font_lic_hei], 1: [_path.font_lic_hei, _path.font_lic_jian, _path.font_lic_song]},
        "font_size": {0: [20, 28, 14, 18], 1: [20, 28, 14, 18]},
        "font_color": {0: ['#292929', '#3b3b3b', '#474747', '#06060e', '#0b0300', '#090907', '#696b66', '#44443f',
                           '#84817a', '#3c3c3a', '#4e4e4c'],
                       1: ['#292929', '#3b3b3b', '#474747', '#06060e', '#0b0300', '#090907', '#696b66', '#44443f',
                           '#84817a', '#3c3c3a', '#4e4e4c']},
        "count": 2
    },
}
train_ticket = {
    "bank_ground": _path.template_train_image,
    "value_1": {  # 纯汉字         **车票信息**
        "text": _path.text_train_data1,
        "font_type": [_path.font_train_simhei, _path.font_train_song2],
        "font_size": [14],
        "font_color": ['#000000'],
        "count": 2
    },
    "value_2": {  # 纯字母         **火车站名称拼音**
        "text": _path.text_train_station_spell,
        "font_type": [_path.font_train_arial, _path.font_train_simsunf, _path.font_train_song1],
        "font_size": [14],
        "font_color": ['#000000'],
        "count": 2
    },
    "mixed_1": {  # 数字与字母混合     **左上角的红色编号**
        "text": _path.text_train_red_num_let,
        "font_type": {
            1: [_path.font_train_arial, _path.font_train_calibri, _path.font_train_simsunf],
            2: [_path.font_train_arial, _path.font_train_narrow, _path.font_train_simsunf]},
        "font_size": {1: [14], 2: [14]},
        "font_color": {1: ['#FF0000'], 2: ['#FF0000']},
        "fluctuate": False,
        "count": 1
    },
    "mixed_2": {  # 数字和字母混合     **车次**
        "text": _path.text_train_num_let,
        "font_type": {
            1: [_path.font_train_times, _path.font_train_simsunf],
            2: [_path.font_train_times, _path.font_train_simsunf]},
        "font_size": {1: [18], 2: [17]},
        "font_color": {1: ['#000000'], 2: ['#000000']},
        "fluctuate": False,
        "count": 1
    },
    "mixed_3": {  # 数字与字母混合     **火车票最下方编号**
        "text": _path.text_train_id_num_let,
        "font_type": {1: [_path.font_train_simsunf, _path.font_train_song1],
                      2: [_path.font_train_times, _path.font_train_song1]},
        "font_size": {1: [12], 2: [12]},
        "font_color": {1: ['#000000'], 2: ['#000000']},
        "fluctuate": False,
        "count": 1
    },
    "mixed_4": {  # 汉字和数字混合            **车座位号**
        "text": _path.text_train_seat_num,
        "font_type": {
            0: [_path.font_train_simhei, _path.font_train_song2, _path.font_train_song3],
            1: [_path.font_train_arial, _path.font_train_times],
            2: [_path.font_train_arial, _path.font_train_times]},
        "font_size": {0: [14], 1: [18], 2: [14]},
        "font_color": {0: ['#000000'], 1: ['#000000'], 2: ['#000000']},
        "fluctuate": False,
        "count": 3
    },
    "mixed_5": {  # 汉字和数字混合            **身份证号姓名**
        "text": _path.text_train_id_name,
        "font_type": {
            0: [_path.font_train_simhei, _path.font_train_song2],
            1: [_path.font_train_times, _path.font_train_calibri],
            2: [_path.font_train_simsunf, _path.font_train_times]},
        "font_size": {0: [15], 1: [15], 2: [14]},
        "font_color": {0: ['#000000'], 1: ['#000000'], 2: ['#000000']},
        "fluctuate": False,
        "count": 1
    },
    "train_1": {  # 汉字和汉字混合         **火车站名称**  比较 特殊
        "text": _path.text_train_station_name,
        "font_type": {0: [_path.font_train_simhei, _path.font_train_stxinwei, _path.font_train_stzhongs],
                      3: [_path.font_train_simhei, _path.font_train_stxinwei, _path.font_train_stzhongs]},
        "font_size": {0: [22], 3: [16]},
        "font_color": {0: ['#000000'], 3: ['#000000']},
        "fluctuate": False,
        "count": 2
    },
}
id_card_positive = {
    "bank_ground": _path.template_id_image,
    "key_1": {  # 每个列名称,例如：姓名/性别/出生/住址/公民身份证号码----黑体 6号 蓝色
        "text": _path.text_id_col_name,
        "font_type": [_path.font_id_hei],
        "font_size": [48],
        "font_color": ['#00BFFF'],
        "count": 8
    },
    "value_1": {  # 纯数字:身份证号码内容---OCR-B10BT 5号 黑色
        "text": _path.text_id_random_num,
        "font_type": [_path.font_id_ocrb10bt],
        "font_size": [72],
        "font_color": ['#000000'],
        "count": 4
    },
    "value_2": {  # 纯汉字:(除姓名外的)性别/民族/住址---黑体 小5号 黑色
        "text": _path.text_id_message,
        "font_type": [_path.font_id_hei],
        "font_size": [60],
        "font_color": ['#000000'],
        "count": 4
    },
    "value_3": {  # 纯汉字:姓名内容---黑体 5号 黑色
        "text": _path.text_id_name,
        "font_type": [_path.font_id_hei],
        "font_size": [72],
        "font_color": ['#000000'],
        "count": 4
    },
    "mixed_1": {  # 数字和汉字混合  汉字：0  数字：1:出生年月日---数字汉字混合:  数字为 方正黑体 小5号 黑色/汉字为 黑体 6号 蓝色
        "text": _path.text_id_date1,
        "font_type": {0: [_path.font_id_hei], 1: [_path.font_id_fzhei]},
        "font_size": {0: [48], 1: [60]},
        "font_color": {0: ['#00BFFF'], 1: ['#000000']},
        "count": 4
    },
}
id_card_negative = {
    "bank_ground": _path.template_id_image,
    "key_1": {  # 标题,例如：中华人民共和国----宋体 4号 黑色
        "text": _path.text_id_col_name,
        "font_type": [_path.font_simsun],
        "font_size": [14],
        "font_color": ['#000000'],
        "count": 1
    },
    "key_2": {  # 标题,例如:居民身份证---宋体 2号 黑色
        "text": _path.text_id_col_name,
        "font_type": [_path.font_simsun],
        "font_size": [22],
        "font_color": ['#000000'],
        "count": 1
    },
    "key_3": {  # 每个列名称:签发机关/有效期限---黑体 6号 黑色
        "text": _path.text_id_col_name,
        "font_type": [_path.font_id_hei],
        "font_size": [7.5],
        "font_color": ['#000000'],
        "count": 2
    },
    "value_1": {  # 纯汉字:机关名称---黑体 5号 黑色 **公安局
        "text": _path.text_id_company,
        "font_type": [_path.font_id_hei],
        "font_size": [72],
        "font_color": ['#000000'],
        "count": 1
    },
    "value_2": {  # 有效期 xxxx.xx-xxxx.xx.xx:---黑体 5号 黑色
        "text": _path.text_id_date2,
        "font_type": [_path.font_id_hei],
        "font_size": [72],
        "font_color": ['#000000'],
        "count": 1
    },
}
