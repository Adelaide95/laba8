#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    bts = {
        1: 'taehyung',
        2: 'jungkook',
        3: 'jimin',
        4: 'namjoon',
        5: 'hoseok',
        6: 'jin',
        7: 'yoongi'
    }
    print(bts)
    dict_items = bts.items()
    new_bts = dict(zip(bts.values(), bts.keys()))
    print(new_bts)
