"""
打印嵌套字典的不同，规格为：.a.b 不同
{"a": {"b": 1}}
{"a": {"b": 2}}

"""


def dfs(dictA: dict, dictB: dict, key="") -> None:
    # 这个题目本质上还是一个 N叉树 的一种方式
    for k, v in dictA.items():
        key += f".{k}"
        if isinstance(v, dict):
            dfs(dictA=v, dictB=dictB.get(k, {}),key=key)
        else:
            if v != dictB.get(k):
                print(key)
                return None
    return None


if __name__ == '__main__':
    dictA: dict = {1: {2: {3: {4: ""}}}}
    dictB: dict = {1: {2: {3: {4: "1"}}}}

    dfs(dictA, dictB)
