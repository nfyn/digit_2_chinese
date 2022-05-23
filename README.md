# digit_2_chinese
> 将阿拉伯数字转换为中文的脚本，便于NLP使用
> 
## 环境要求
 - python环境，不需要其他第三方库依赖

## 使用方法
```python
from digit_2_chinese import to_chinese

# 整数
test_num = '123456789'
print(to_chinese(test_num))
# '一亿二千三百四十五万六千七百八十九'

test_num = '103400567809'
print(to_chinese(test_num))
# '一千零三十四亿零五十六万七千八百零九'

test_num = '127809'
print(to_chinese(test_num))
# '十二万七千八百零九'

# 小数
test_num = '32456576.87'
print(to_chinese(test_num))
# '三千二百四十五万六千五百七十六点八七'
```

