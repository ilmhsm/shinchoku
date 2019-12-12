#coding: utf-8
#!/usr/bin/env python
import random

isshinchoku = random.randint(1, 100)
if isshinchoku > 94:
    print('進捗出せた。頑張ったね！')
else:
    print('進捗ダメでした')