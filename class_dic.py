def get_dict_depth(d, current_depth=1):
    max_depth = current_depth
    try:
        for value in d.values():
            if isinstance(value, dict):
                depth = get_dict_depth(value, current_depth + 1)
                max_depth = max(max_depth, depth)
        return max_depth
    except:
        return -1


# 示例字典
def get_min_dict_depth(dictionary):
    """
    计算字典的最小嵌套层数。

    :param dictionary: 要检查的字典。
    :return: 字典的最小嵌套层数；如果没有嵌套，则返回0。
    """
    # if type(dictionary) == str or int:
    #     return -2
    # 标记是否找到嵌套字典
    found_nested = False

    # 遍历字典的值
    try:
        for value in dictionary.values():
            # 如果值是字典，说明找到了嵌套
            if isinstance(value, dict):
                found_nested = True
                break
    except:
        return -2

        # 如果没有找到嵌套字典，返回0
    if not found_nested:
        return 0

        # 初始化最小深度为1（因为顶层字典已经被计算）
    min_depth = 1

    # 再次遍历字典的值以找到最小嵌套深度
    for value in dictionary.values():
        # 如果值是字典，递归调用函数并获取嵌套深度
        if isinstance(value, dict):
            nested_depth = get_min_dict_depth(value) + 1  # +1表示当前层级
            # 更新最小深度
            min_depth = min(min_depth, nested_depth)

            # 返回最小深度
    return min_depth


def find_key_value(dictionary, key_to_find):
    for key, value in dictionary.items():
        if key == key_to_find:
            return value
        if isinstance(value, dict):
            nested_result = find_key_value(value, key_to_find)
            if nested_result is not None:
                return nested_result
    return None


example_dict = {
    "1. Introduction": "",
    "2. Historical Development of AI": {
        "2.1 Early Concepts of AI": "",
        "2.2 Emergence of Machine Learning": "",
        "2.3 Advancements in Deep Learning": ""
    },
    "3. Key Components of AI": {
        "3.1 Natural Language Processing": "",
        "3.2 Computer Vision": "",
        "3.3 Robotics": "",
        "3.4 Expert Systems": ""
    },
    "4. Applications of AI": {
        "4.1 Healthcare": "",
        "4.2 Finance": "",
        "4.3 Transportation": "",
        "4.4 Manufacturing": ""
    },
    "5. Ethical Considerations in AI": {
        "5.1 Bias and Fairness": "",
        "5.2 Privacy and Security": "",
        "5.3 Job Displacement": ""
    },
    "6. Future Directions of AI": {
        "6.1 Explainable AI": "",
        "6.2 AI in Space Exploration": "",
        "6.3 AI and Sustainability": ""
    },
    "7. Conclusion": ""
}


class dic_stru:
    name = {}
    all_keys = []  # 所有键：用于遍历和生成字典
    all_dic = {}  # 存储最终内容
    dic_keys = []  # 包含字典的键：用新prompt
    dic_list = []  # 包含字典的链表：用新的small_title
    str_keys = []  # 包含字典的键：用旧prompt

    def __init__(self, name):
        self.name = name  # get_structure返回的字典
        self.all_keys = self.get_all_keys()
        for key0 in self.all_keys:
            if get_dict_depth(self.find_key_value(key0)) == 1:
                self.dic_keys.append(key0)
                self.dic_list.append(self.find_key_value(key0))
        for key0 in self.all_keys:
            if get_min_dict_depth(self.find_key_value(key0)) == 1:
                print(key0)
                self.dic_keys.append(key0)
                small_dic = self.find_key_value(key0)
                for key1 in self.dic_keys:
                    small_dic = self.find_key_value(key0)
                    if key1 in small_dic:
                        small_dic.pop(key1)
                self.dic_list.append(small_dic)
        print("dic_keys:", self.dic_keys)
        print("dic_list:", self.dic_list)
        for key0 in self.all_keys:
            if (get_min_dict_depth(self.find_key_value(key0))) == -2 and key0 in self.name:
                self.str_keys.append(key0)
        print("str_keys:", self.str_keys)
        for key0 in self.all_keys:
            self.all_dic[key0] = ''
        print("all_dic:", self.all_dic)

    def get_all_keys(self):
        def get_all_keys(d):
            keys = []
            for key, value in d.items():
                keys.append(key)
                if isinstance(value, dict):
                    keys.extend(get_all_keys(value))
            return keys

        keys = []
        for key, value in self.name.items():
            keys.append(key)
            if isinstance(value, dict):
                keys.extend(get_all_keys(value))
        return keys

    def find_key_value(self, key_to_find):
        """
        在字典中搜索给定的键，包括嵌套字典，并返回找到的第一个匹配项的值。

        :param dictionary: 要搜索的字典
        :param key_to_find: 要查找的键
        :return: 找到的值或None（如果没有找到）
        """
        for key, value in self.name.items():
            if key == key_to_find:
                return value
            if isinstance(value, dict):
                nested_result = find_key_value(value, key_to_find)
                if nested_result is not None:
                    return nested_result
        return None

# dic = dic_stru(example_dict)
# print(dic.get_all_keys())
# print(dic.find_key_value("s"))
# print(get_dict_depth(dic.name["2. Fundamentals of Microfluidics"]))
# print(get_dict_depth(dic.name["3. Fabrication Techniques"]))
# print(get_min_dict_depth(dic.name))
# print(    result)  # ['1. Introduction', '2. Historical Development of Mathematics', '3. Branches of Mathematics', '4. Conclusion', '2.1 Ancient Mathematics', '3.1 Algebra', '3.2 Geometry', '3.3 Calculus', '3.4 Statistics', '3.5 Number Theory', '3.6 Mathematical Logic', '2.2 Mathematics in the 20th Century']
