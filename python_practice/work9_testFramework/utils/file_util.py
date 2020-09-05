#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/5 9:18
# @Author  : Yuki
import yaml


class FileUtil:
    @classmethod
    def from_file(cls, path):
        with open(path, encoding="utf-8") as f:
            yaml_datas = yaml.safe_load(f)
            params = yaml_datas["params"]
            # set()是集合，相对于dict存储的是key，且key是唯一的
            keys = set()
            values = []
            if isinstance(params, list):
                for row in params:
                    if isinstance(row, dict):
                        for key in row.keys():
                            keys.add(key)
                            values.append(list(row.values())[0])
            var_names = ','.join(keys)

            res = {"keys": var_names, "values": values}
            print(res)

            return res


