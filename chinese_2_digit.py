def four_chinese_to_digit(c: str) -> str:
    res = ''
    thousand = re.match(r'.*?(\w)千', c)
    if thousand:
        res += thousand.group(1)
    else:
        res += '零'
    hundred = re.match(r'.*?(\w)百', c)
    if hundred:
        res += hundred.group(1)
    else:
        res += '零'
    ten = re.match(r'.*?十', c)
    if ten:
        ten1 = re.match(r'.*?(\w)十', c)
        if ten1:
            if ten1.group(1) == '零':
                res += '一'
            else:
                res += ten1.group(1)
    else:
        res += '零'
    single = c[-1]
    if single == '十':
        res += '零'
    else:
        res += single

    return ''.join([str(HAN_STR.index(i)) for i in res])


def chinese_2_digit(c: str) -> str:
    c_lst = re.split(r'点', c)
    integer_part = c_lst[0]
    decimal_part = c_lst[1] if len(c_lst) == 2 else None
    decimal_str = ''
    if decimal_part:
        decimal_str = '.'
        for d in decimal_part:
            decimal_str += str(HAN_STR.index(d))

    integer_lst = re.split(r'[万亿]', integer_part)

    integer_str = ''.join([four_chinese_to_digit(i) for i in integer_lst])
    return integer_str + decimal_str or ''
  
  if __name__ == '__main__':
    a = '一千零三十四亿零五十六万七千八百零九'
    print(chinese_2_digit(a))
    # '103400567809'
