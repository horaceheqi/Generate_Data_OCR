import io
import os
import random
from tqdm import tqdm
import code_setting as file_path


def gen_tel(_count):
    tel_num, tel_num1 = [], ''
    for i in range(_count):
        temp = random.randrange(0, 3)
        if temp == 0:
            tel_num1 = ''.join(random.choice("0123456789") for _ in range(8))
        elif temp == 1:
            tel_num1 = ''.join(random.choice("0123456789") for _ in range(3)) + "-" + ''.join(
                random.choice("0123456789") for _ in range(8))
        elif temp == 2:
            tel_num1 = ''.join(random.choice("0123456789") for _ in range(random.randrange(8, 11)))
        tel_num.append(tel_num1)
    return tel_num


# 加载常用汉字字典
def load_dict(_path):
    with open(_path, "r", encoding="utf-8") as f:
        data = f.read().splitlines()
        return data


# 随机生成汉字(行)
def gen_random_chinese(_path, row_count, col_count):  # 生成row_count行,每行最长col_count
    if os.path.exists(_path):
        os.remove(_path)
    _set = load_dict(file_path.ge_3500)
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            line = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(1, col_count)))
            print(line)
            f.write(u"{}\n".format(line))


# 随机生成汉字(行)
def gen_chinese_name(_path, row_count, col_count):  # 生成row_count行,每行最长col_count
    if os.path.exists(_path):
        os.remove(_path)
    _set = load_dict(file_path.ge_3500)
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            line = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(2, col_count)))
            print(line)
            f.write(u"{}\n".format(line))


# 随机生成数字(行)
def gen_random_digital(_path, row_count, col_count):  # 生成row_count行,每行最长col_count
    if os.path.exists(_path):
        os.remove(_path)
    _set = list("0123456789")
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            line = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(15, col_count)))
            print(line)
            f.write(u"{}\n".format(line))


# 生成大写金额
def gen_large_amount(_path, row_count, col_count):  # 生成row_count行,每行最长col_count
    if os.path.exists(_path):
        os.remove(_path)
    _set = list("壹贰叁肆伍陆柒捌玖零拾佰仟万亿圆角分整")
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            temp = random.randrange(0, 2)
            line = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(1, col_count)))
            if temp == 0:
                amount = line + ''.join(random.choice("圆角分")) + '整'
                print(amount)
                f.write(u"{}\n".format(amount))
            else:
                amount = 'ⓧ' + line + ''.join(random.choice("圆角分")) + '整'
                print(amount)
                f.write(u"{}\n".format(amount))


# 生成小写金额
def gen_small_amount(_path, row_count, col_count):  # 生成row_count行,每行最长col_count
    if os.path.exists(_path):
        os.remove(_path)
    _set = list("0123456789")
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            # 随机确定小数点前的位数
            line = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(1, col_count - 2)))
            # 随机确定小数点后的位数
            line = line + '.'
            for _ in range(2):
                line = line + random.sample(_set, 1)[0]
            print(line)
            f.write(u"{}\n".format(line))


# 生成求和金额(带￥)
def gen_sum_amount(_path, row_count, col_count):
    if os.path.exists(_path):
        os.remove(_path)
    _set = list("0123456789")
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            line = "￥"
            # 随机确定小数点前内容
            nums = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(1, col_count - 2)))
            # 随机确定小数点后的内容
            line = line + nums + '.'
            for _ in range(2):
                line = line + random.sample(_set, 1)[0]
            print(line)
            f.write(u"{}\n".format(line))


# 生成公司名称
def gen_company_name(_path, row_count, col_count):
    if os.path.exists(_path):
        os.remove(_path)
    _set = load_dict(file_path.ge_company)
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            name = ''.join(random.choice(_set) for _ in range(random.randrange(3, col_count)))
            cons = random.randrange(0, 3)
            company = ''
            if cons == 0:
                company = name + '有限公司'
            elif cons == 1:
                company = name + '股份有限公司'
            elif cons == 2:
                company = name + '集团有限公司'
            f.write("{}\n".format(company))


# 生成校验码
def gen_check_code(_path, row_count, col_count=5):
    if os.path.exists(_path):
        os.remove(_path)
    _set = list("0123456789")
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(1, row_count+1)):
            line = "校验码 "
            for _ in range(4):
                for _ in range(col_count):
                    line = line + random.sample(_set, 1)[0]
                line = line + " "
            print(line)
            f.write("{}\n".format(line))


# 生成票据密码
def gen_ticket_cipher(_path, row_count, col_count=27):
    if os.path.exists(_path):
        os.remove(_path)
    _set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    cipher_set = _set + ['+', '-', '*', '/', '<', '>']
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(1, row_count+1)):
            line = ''.join(random.sample(cipher_set, 1)[0] for _ in range(random.randrange(1, col_count)))
            print(line)
            f.write("{}\n".format(line))


# 生成标题Title
def gen_text_title(_path, row_count):  # flag如果为真采用模板,否则采用自定义汉字
    if os.path.exists(_path):
        os.remove(_path)
    _set = ["北京", "天津", "上海", "重庆", "河北", "山西", "辽宁", "吉林", "黑龙江", "江苏",
            "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北", "湖南", "广东", "海南",
            "四川", "贵州", "云南", "陕西", "甘肃", "青海", "内蒙古", "广西", "西藏", "宁夏", "新疆"]
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(1, row_count + 1)):
            line = ""
            line = line + random.sample(_set, 1)[0]
            line = line + "增值税"
            line = line + random.sample(["电子", ""], 1)[0]
            line = line + random.sample(["普通", "专用"], 1)[0]
            line = line + "发票"
            print(line)
            f.write("{}\n".format(line))


# 生成地址
def gen_adr_tel(_path, row_count):
    if os.path.exists(_path):
        os.remove(_path)
    tel_num = gen_tel(row_count)
    city, word = [], []
    with io.open(file_path.ge_city, mode='r', encoding='utf-8') as f:
        for l in f.readlines():
            city.append(l.strip())
    with io.open(file_path.ge_company, mode='r', encoding='utf-8') as f:
        for l in f.readlines():
            word.append(l.strip())
    with io.open(_path, 'w', encoding='utf-8') as f:
        for i in range(row_count):
            name = ''.join(random.choice(word) for _ in range(random.randrange(3, 7)))
            name1 = ''.join(random.choice(word) for _ in range(random.randrange(2, 5)))
            name2 = ''.join(random.choice(word) for _ in range(random.randrange(2, 5)))
            adr_tel = random.choice(city) + name1 + "街道" + name2 + "小区" \
                      + ''.join(' ' for _ in range(random.randrange(0, 3))) + random.choice(tel_num)
            print(adr_tel)
            f.write(u"{}\n".format(adr_tel))


# 生成银行地址和账号(汉字数据)
def gen_bank_account(_path, row_count, col_count):
    if os.path.exists(_path):
        os.remove(_path)
    _set = list("0123456789")
    id_count = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(12, col_count)))
    city, word = [], []
    with io.open(file_path.ge_city, mode='r', encoding='utf-8') as f:
        for l in f.readlines():
            city.append(l.strip())
    with io.open(file_path.ge_company, mode='r', encoding='utf-8') as f:
        for l in f.readlines():
            word.append(l.strip())
    with io.open(_path, 'w', encoding="utf-8") as f:
        for i in range(row_count):
            name = ''.join(random.choice(word) for _ in range(random.randrange(3, 7)))
            name1 = ''.join(random.choice(word) for _ in range(random.randrange(2, 5)))
            name2 = ''.join(random.choice(word) for _ in range(random.randrange(2, 5)))
            cons = random.randrange(0, 2)
            if cons == 0:
                bank_id = random.choice(city)[:3] + name1 + "银行" + name2 + "支行" + ''.join(
                    ' ' for _ in range(random.randrange(0, 3))) + id_count
            else:
                bank_id = random.choice(city)[:3] + name1 + "银行" + name2 + "支行" + name[:3] + "分理处" + ''.join(
                    ' ' for _ in range(random.randrange(0, 3))) + id_count
            print(bank_id)
            f.write(u"{}\n".format(bank_id))


# 生成数字、字母混合
def gen_num_let(_path, row_count):
    if os.path.exists(_path):
        os.remove(_path)
    with open(_path, "w", encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            random_str = ""
            num_8 = ''.join(random.choice("0123456789") for _ in range(8))
            length = random.randrange(0, 3)
            if length == 0:
                for i in range(0, 7):
                    temp = random.randrange(0, 2)
                    if temp == 0:
                        ch = chr(random.randrange(ord('A'), ord('Z') + 1))
                        random_str += ch
                    else:
                        ch = str(random.randrange(0, 9))
                        random_str += ch
            elif length == 1:
                temp = random.randrange(0, 2)
                if temp == 0:
                    random_str = ''.join(random.choice("0123456789") for _ in range(10))
                else:
                    random_str = ''.join(random.choice("0123456789") for _ in range(7))
            elif length == 2:
                for j in range(0, 10):
                    temp = random.randrange(0, 2)
                    if temp == 0:
                        ch = chr(random.randrange(ord('A'), ord('Z') + 1))
                        random_str += ch
                    else:
                        ch = str(random.randrange(0, 9))
                        random_str += ch
            random_str = num_8 + random_str
            print(random_str)
            f.write(u"{}\n".format(random_str))


# 生成yyyy-mm-dd格式的日期
def gen_data(_path, row_count):  # yyyy-mm-dd
    if os.path.exists(_path):
        os.remove(_path)
    with open(_path, 'w', encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            temp = ''.join(random.choice("0123456789") for i in range(4)) + '年' \
            + ''.join(random.choice(['01','02','03','04','05','06','07','08','09','10','11','12'])) + '月' \
            + random.choice([str(i) for i in range(0, 31)]) + '日'
            f.write("{}\n".format(temp))


# 生成yyyy-mm-dd 至 yyyy-mm-dd格式的日期
def gen_data2(_path, row_count):  # yyyy-mm-dd 至 yyy-mm-dd
    if os.path.exists(_path):
        os.remove(_path)
    with open(_path, 'w', encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            temp1 = ''.join(random.choice("0123456789") for i in range(4)) + '年' \
            + ''.join(random.choice(['01','02','03','04','05','06','07','08','09','10','11','12'])) + '月' \
            + random.choice([str(i) for i in range(0, 31)]) + '日'
            temp2 = ''.join(random.choice("0123456789") for i in range(4)) + '年' \
            + ''.join(random.choice(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'])) + '月' \
            + random.choice([str(i) for i in range(0, 31)]) + '日'
            data = temp1 + '' + '' + '' + temp2
            f.write("{}\n".format(data))


# 随机生成纯字母
def gen_random_english(_path, row_count, col_count):
    if os.path.exists(_path):
        os.remove(_path)
    _set = list("abcdefghijklmnopqrstuvwxyz")
    # _set = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    with open(_path, 'w', encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            line = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(5, 10)))
            print(line)
            f.write(u"{}\n".format(line))


# 生成字母、数字和汉字混合(车次号)
def gen_train_times(_path, row_count, col_count):
    if os.path.exists(_path):
        os.remove(_path)
    _set = list("0123456789")
    with open(_path, 'w', encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            line1 = chr(random.randrange(ord('A'), ord('Z') + 1))
            line2 = ''.join(random.sample(_set, 1)[0] for _ in range(random.randrange(1, col_count)))
            line = line1 + line2 + '次'
            print(line)
            f.write(u"{}\n".format(line))


# 生成汉字和字母混合 (户AD)
def gen_chines_digital(_path, row_count, col_count):
    if os.path.exists(_path):
        os.remove(_path)
    _set1 = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    _set2 = load_dict(file_path.ge_3500)
    with open(_path, 'w', encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            line1 = ''.join(random.sample(_set2, 1)[0] for _ in range(random.randrange(1, col_count)))
            line2 = ''.join(random.sample(_set1, 1)[0] for _ in range(random.randrange(1, col_count)))
            line = line1 + line2
            print(line)
            f.write(u"{}\n".format(line))


# 生成汉字和字母混合 (户AD)
def gen_id_text(_path, row_count, col_count):
    if os.path.exists(_path):
        os.remove(_path)
    _set1 = ['男', '女']
    _set2 = ['蒙古族', '回族', '藏族', '维吾尔族', '苗族', '彝族', '壮族', '布依族', '朝鲜族', '满族', '侗族', '瑶族', '白族',
             '土家族', '哈尼族', '哈萨克族', '傣族', '黎族', '僳僳族', '佤族', '畲族', '高山族', '拉祜族', '水族', '东乡族',
             '纳西族', '景颇族', '柯尔克孜族', '土族', '达斡尔族', '仫佬族', '羌族', '布朗族', '撒拉族', '毛南族', '仡佬族',
             '锡伯族', '阿昌族', '普米族', '塔吉克族', '怒族', '乌孜别克族', '俄罗斯族', '鄂温克族', '德昂族', '保安族',
             '裕固族', '京族', '塔塔尔族', '独龙族', '鄂伦春族', '赫哲族', '门巴族', '珞巴族', '基诺族', '汉族']
    _set3 = load_dict('./gen_text/address_name.txt')
    with open(_path, 'w', encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            nums = random.randrange(0, col_count)
            if nums == 0:
                line = random.sample(_set1, 1)[0]
                f.write(u"{}\n".format(line))
            if nums == 1:
                line = random.sample(_set2, 1)[0]
                f.write(u"{}\n".format(line))
            if nums == 2:
                line = random.sample(_set3, 1)[0]
                f.write(u"{}\n".format(line))


# 生成营业执照数字 15/20位纯数字,18位字母数字混合
def gen_lic_num(_path, row_count, col_count):
    if os.path.exists(_path):
        os.remove(_path)
    _set1 = load_dict('./gen_text/random_digital.txt')
    _set2 = load_dict('./gen_text/num_let.txt')
    with open(_path, 'w', encoding="utf-8") as f:
        for _ in tqdm(range(row_count)):
            nums = random.randrange(0, col_count)
            if nums == 0:
                line = random.sample(_set1, 1)[0]
                f.write(u"{}\n".format(line))
            if nums == 1:
                line = random.sample(_set2, 1)[0]
                f.write(u"{}\n".format(line))


if __name__ == '__main__':
    # gen_random_chinese('./gen_text/random_chinese.txt', 5000, 10)  # 随机生成汉字
    # gen_random_digital('./gen_text/random_digital.txt', 5000, 20)  # 随机生成数字
    # gen_large_amount('./gen_text/large_amount.txt', 5000, 10)  # 生成大写金额
    # gen_small_amount('./gen_text/small_amount.txt', 5000, 10)  # 生成小写金额
    # gen_sum_amount('./gen_text/sum_amount.txt', 5000, 7)  # 生成求和金额(带￥)
    # gen_company_name('./gen_text/company_name.txt', 5000, 10)  # 生成公司名称
    # gen_ticket_cipher('./gen_text/ticket_cipher.txt', 5000, 27)  # 生成票据密码(数字和符号混合)
    # gen_check_code('./gen_text/check_code.txt', 5000, 5)  # 生成票据密码
    # gen_chinese_name('./gen_text/chinese_name.txt', 5000, 5)  # 生成人名
    # gen_text_title('./gen_text/text_title.txt', 5000)  # 生成票据标题
    # gen_adr_tel('./gen_text/adr_tel.txt', 5000)  # 生成地址(汉字和数字混合)
    # gen_bank_account('./gen_text/bank_account.txt', 5000, 15)  # 生成银行地址和账号(汉字和数字混合)
    # gen_num_let('./gen_text/num_let.txt', 5000)  # 生成数字、字母混合
    # gen_data('./gen_text/data_1.txt', 5000)  # yyyy-mm-dd
    # gen_data2('./gen_text/data_2.txt', 5000)  # yyyy-mm-dd 至 yyyy-mm-dd
    # gen_random_english('./gen_text/random_english.txt', 5000, 10)  # 随机生成纯字母
    # gen_train_times('./gen_text/trains_times.txt', 5000, 5)  # 随机生成车次
    # gen_chines_digital('./gen_text/chines_digital.txt', 5000, 3)  # 生成汉字和字母混合 (户AD)
    # gen_id_text('./gen_text/id_card_adr.txt', 5000, 3)  # 生成汉字和字母混合 (户AD)
    gen_lic_num('./gen_text/lic_num_let.txt', 5000, 2)  # 生成营业执照数字 15/20位纯数字,18位字母数字混合
