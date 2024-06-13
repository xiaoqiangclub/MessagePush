# _*_ coding : UTF-8 _*_
# 开发人员： XiaoqiangClub
# 微信公众号: XiaoqiangClub
# 开发时间：2024年06月13日
# 文件名称： config_loader.py
# 项目描述： 加载YAML和JSON配置文件的模块

import yaml
import json


class ConfigLoader:
    @staticmethod
    def load_config(config_path: str) -> dict:
        """
        加载YAML或JSON配置文件

        :param config_path: 配置文件路径
        :return: 配置字典
        """
        with open(config_path, 'r', encoding='utf-8') as file:
            if config_path.endswith('.yaml') or config_path.endswith('.yml'):
                config = yaml.safe_load(file)
            elif config_path.endswith('.json'):
                config = json.load(file)
            else:
                raise ValueError("Unsupported file format. Please use a YAML or JSON file.")
        return config
