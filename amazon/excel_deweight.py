# -- coding: utf-8 --
# @Author: 胡H
# @File: excel_deweight.py
# @Created: 2025/4/12 16:02
# @LastModified: 
# Copyright (c) 2025 by 胡H, All Rights Reserved.
# @desc: excel去重
import pandas as pd


def deduplicate_excel(input_file, output_file, subset='href', keep='first'):
    """
    Excel文件href去重功能

    :param input_file: 输入文件路径
    :param output_file: 输出文件路径
    :param subset: 去重依据列，默认为href
    :param keep: 保留策略：first-保留第一个（默认） last-保留最后
    """
    try:
        # 读取数据
        df = pd.read_excel(input_file)

        # 检查是否存在目标列
        if subset not in df.columns:
            raise ValueError(f"数据中不存在 '{subset}' 列")

        # 执行去重
        cleaned_df = df.drop_duplicates(subset=[subset], keep=keep)

        # 保存结果
        cleaned_df.to_excel(output_file, index=False)

        print(f"去重完成！原始记录：{len(df)}条 → 去重后：{len(cleaned_df)}条")
        print(f"结果已保存至：{output_file}")

    except Exception as e:
        print(f"处理失败：{str(e)}")


# 使用示例
deduplicate_excel(
    input_file="compilations/hdisneyList-1744446396.xlsx",
    output_file="compilations/amazon_动漫电视.xlsx",
    subset="href",  # 去重依据列
    keep="last"  # 保留策略：first/last
)
