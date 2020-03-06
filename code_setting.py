import os

# 根目录
root_path = 'D:/UMPAY/Project/Coding/General_Detect_Image'

# 加载生成图片的背景
template_invoice_paper = os.path.join(root_path, 'background_image/detect/invoice_paper.jpg')
template_invoice_elc = os.path.join(root_path, 'background_image/detect/invoice_elc2.jpg')
template_id_image = os.path.join(root_path, 'background_image/detect/id_card_negative.jpg')
template_license_image = os.path.join(root_path, 'background_image/detect/license_ticket.jpg')
template_train_image = os.path.join(root_path, 'background_image/detect/train_ticket2.jpg')

# 加载文字库
ge_3500 = os.path.join(root_path, 'dicts/ge_3500.txt')
ge_bank = os.path.join(root_path, 'dicts/ge_bank.txt')
ge_city = os.path.join(root_path, 'dicts/ge_city.txt')
ge_company = os.path.join(root_path, 'dicts/ge_company.txt')
ge_streets = os.path.join(root_path, 'dicts/ge_street.txt')
ge_rate = os.path.join(root_path, 'dicts/ge_rate.txt')

# 加载火车票语料库
text_train_amount = os.path.join('gen_text/train_ticket/text_amount.txt')
text_train_data1 = os.path.join('gen_text/train_ticket/text_data_1.txt')
text_train_data = os.path.join('gen_text/train_ticket/text_data.txt')
text_train_id_name = os.path.join('gen_text/train_ticket/text_id_name.txt')
text_train_id_num_let = os.path.join('gen_text/train_ticket/text_id_num_let.txt')
text_train_red_num_let = os.path.join('gen_text/train_ticket/text_red_num_let.txt')
text_train_seat_num = os.path.join('gen_text/train_ticket/text_seat_num.txt')
text_train_station_name = os.path.join('gen_text/train_ticket/text_station_name.txt')
text_train_station_spell = os.path.join('gen_text/train_ticket/text_station_spell.txt')
text_train_num_let = os.path.join('gen_text/train_ticket/text_train_num_let.txt')
# 加载火车票字体库
font_train_arial = os.path.join('fonts/train_ticket/arial.ttf')
font_train_narrow = os.path.join('fonts/train_ticket/arial narrow.ttf')
font_train_arialbd = os.path.join('fonts/train_ticket/arialbd.ttf')
font_train_arialn = os.path.join('fonts/train_ticket/ARIALN.TTF')
font_train_arialnb = os.path.join('fonts/train_ticket/ARIALNB.TTF')
font_train_ariblk = os.path.join('fonts/train_ticket/ariblk.ttf')
font_train_calibri = os.path.join('fonts/train_ticket/calibri.ttf')
font_train_calibrib = os.path.join('fonts/train_ticket/calibrib.ttf')
font_train_simhei = os.path.join('fonts/train_ticket/simhei.ttf')
font_train_simsunc = os.path.join('fonts/train_ticket/simsun.ttc')
font_train_simsunf = os.path.join('fonts/train_ticket/simsun.ttf')
font_train_stxinwei = os.path.join('fonts/train_ticket/STXINWEI.TTF')
font_train_stzhongs = os.path.join('fonts/train_ticket/STZHONGS.TTF')
font_train_song1 = os.path.join('fonts/train_ticket/仿宋_GB2312.ttf')
font_train_song2 = os.path.join('fonts/train_ticket/华文中宋.ttf')
font_train_song3 = os.path.join('fonts/train_ticket/标准仿宋体简.ttf')
font_train_times = os.path.join('fonts/train_ticket/车次.ttf')

# 加载身份证语料库
text_id_col_name = os.path.join('gen_text/id_card/column_name.txt')
text_id_random_num = os.path.join('gen_text/id_card/random_digital.txt')
text_id_message = os.path.join('gen_text/id_card/id_card_adr.txt')
text_id_name = os.path.join('gen_text/id_card/chinese_name.txt')
text_id_date1 = os.path.join('gen_text/id_card/id_date.txt')
text_id_date2 = os.path.join('gen_text/id_card/id_date2.txt')
text_id_company = os.path.join('gen_text/id_card/id_company_name.txt')
# 加载身份证字体库
font_id_fzhei = os.path.join('fonts/id_card/fzhei.ttf')
font_id_hei = os.path.join('fonts/id_card/hei.ttf')
font_id_ocrb10bt = os.path.join('fonts/id_card/ocrb10bt.ttf')

# 加载营业执照语料库
text_lic_annotation = os.path.join('gen_text/license_ticket/语料-二维码提示及脚注.txt')
text_lic_address = os.path.join('gen_text/license_ticket/语料-住所.txt')
text_lic_company_name = os.path.join('gen_text/license_ticket/语料-公司名.txt')
text_lic_company_type = os.path.join('gen_text/license_ticket/语料-公司类型.txt')
text_lic_large_title = os.path.join('gen_text/license_ticket/语料-大标题.txt')
text_lic_register_date = os.path.join('gen_text/license_ticket/语料-成立日期.txt')
text_lic_large_date = os.path.join('gen_text/license_ticket/语料-时间大写.txt')
text_lic_small_date = os.path.join('gen_text/license_ticket/语料-时间小写.txt')
text_lic_label = os.path.join('gen_text/license_ticket/语料-标签.txt')
text_lic_name = os.path.join('gen_text/license_ticket/语料-法定代表人.txt')
text_lic_amount = os.path.join('gen_text/license_ticket/语料-注册资本.txt')
text_lic_date_limit = os.path.join('gen_text/license_ticket/语料-营业期限.txt')
text_lic_foot_note = os.path.join('gen_text/license_ticket/语料-落款.txt')
text_lic_key_note = os.path.join('gen_text/license_ticket/语料-重要提示.txt')
text_lic_lang_num = os.path.join('gen_text/license_ticket/语料-长数字.txt')
#  加载营业执照字体库
font_lic_song = os.path.join('fonts/license_ticket/新宋体.ttc')
font_lic_jian = os.path.join('fonts/license_ticket/方正书宋简体.ttf')
font_lic_hei = os.path.join('fonts/license_ticket/黑体.ttf')

# 加载增值税语料库
text_inc_name = os.path.join('gen_text/invoice_ticket/语料-人名.txt')
text_inc_company = os.path.join('gen_text/invoice_ticket/语料-公司名称.txt')
text_inc_price = os.path.join('gen_text/invoice_ticket/语料-单价.txt')
text_inc_code = os.path.join('gen_text/invoice_ticket/语料-发票代码.txt')
text_inc_number = os.path.join('gen_text/invoice_ticket/语料-发票号码.txt')
text_inc_address = os.path.join('gen_text/invoice_ticket/语料-地址电话.txt')
text_inc_large_amount = os.path.join('gen_text/invoice_ticket/语料-大写金额.txt')
text_inc_large_title = os.path.join('gen_text/invoice_ticket/语料-大标题.txt')
text_inc_pwd = os.path.join('gen_text/invoice_ticket/语料-密码区.txt')
text_inc_account = os.path.join('gen_text/invoice_ticket/语料-开户行及账号.txt')
text_inc_time = os.path.join('gen_text/invoice_ticket/语料-开票时间.txt')
text_inc_total = os.path.join('gen_text/invoice_ticket/语料-总价.txt')
text_inc_nums = os.path.join('gen_text/invoice_ticket/语料-数量.txt')
text_inc_machine = os.path.join('gen_text/invoice_ticket/语料-机器码.txt')
text_inc_label = os.path.join('gen_text/invoice_ticket/语料-标签.txt')
text_inc_rate = os.path.join('gen_text/invoice_ticket/语料-税率.txt')
text_inc_id = os.path.join('gen_text/invoice_ticket/语料-纳税人识别号.txt')
# 加载增值税字体库
font_elc_arial = os.path.join('fonts/invoice_ticket/Arial.ttf')
font_elc_song = os.path.join('fonts/invoice_ticket/新宋体.ttc')
font_elc_kai = os.path.join('fonts/invoice_ticket/楷体.ttf')
font_elc_hei = os.path.join('fonts/invoice_ticket/黑体.ttf')
font_pa_songjian = os.path.join('fonts/invoice_ticket/方正书宋简体.ttf')
font_pa_xinsong = os.path.join('fonts/invoice_ticket/新宋体.ttc')
font_pa_kai = os.path.join('fonts/invoice_ticket/楷体.ttf')

# 加载其它文字字体
font_simhei = os.path.join(root_path, 'fonts/simhei.ttf')
font_simli = os.path.join(root_path, 'fonts/SIMLI.TTF')
font_simsun = os.path.join(root_path, 'fonts/SimSun.ttf')
font_hansan  = os.path.join(root_path, 'fonts/SourceHanSans-Normal.ttf')
font_stix = os.path.join(root_path, 'fonts/STIX-Regular.otf')
font_stzhong = os.path.join(root_path, 'fonts/STZHONGS.TTF')

# 加载其它文本
text_adr_tel = os.path.join('gen_text/adr_tel.txt')  # 汉字 + 数字(地址/电话)
text_bank_account = os.path.join('gen_text/bank_account.txt')  # 汉字 + 数字(银行地址/银行号)
text_check_code = os.path.join('gen_text/check_code.txt')  # 汉字 + 数字(校验码/20数字)
text_chinese_name = os.path.join('gen_text/chinese_name.txt')  # 纯汉字(2-4个)
text_company_name = os.path.join('gen_text/company_name.txt')  # 公司名称(最长20)
text_data_1 = os.path.join('gen_text/data_1.txt')  # 数字 + 汉字(yyyy年mm月dd日)
text_data_2 = os.path.join('gen_text/data_2.txt')  # 数字 + 汉字(yyyy年mm月dd日 至 yyyy年mm月dd日)
text_large_amount = os.path.join('gen_text/large_amount.txt')  # 大写金额
text_num_let = os.path.join('gen_text/num_let.txt')  # 数字 + 字母
text_random_chinese = os.path.join(root_path, 'gen_text/random_chinese.txt')  # 纯汉字
text_random_digital = os.path.join('gen_text/random_digital.txt')  # 纯数字
text_random_english = os.path.join('gen_text/random_english.txt')  # 纯字母
text_small_amount = os.path.join('gen_text/small_amount.txt')  # 小写金额
text_sum_amount = os.path.join('gen_text/sum_amount.txt')  # 总金额(￥金额)
text_title = os.path.join(root_path, 'gen_text/text_title.txt')  # 纯汉字(增值税发票)
text_ticket_cipher = os.path.join('gen_text/ticket_cipher.txt')  # 增值税发票验证码
text_trains_times = os.path.join('gen_text/trains_times.txt')  # 字母 + 数字 + 汉字(车次)
text_chinese_english = os.path.join('gen_text/chines_english.txt')  # 汉字 + 字母(户AD)
