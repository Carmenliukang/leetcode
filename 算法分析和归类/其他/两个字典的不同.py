"""
对比两个字典的所有不同
"""


def pprint(dictA: dict, dictB: dict) -> None:
    for k, v in dictA.items():
        if dictB.get(k) != v:
            print(f"dictA {k}:{v}")

    for k, v in dictB.items():
        if dictA.get(k) != v:
            print(f"dictB {k}:{v}")
    return None


def pprintMethodA(dictA: dict, dictB: dict) -> None:
    keys = list(dictA.keys())
    keys.extend(list(dictB.keys()))
    keys = set(keys)
    for key in keys:
        while dictA.get(key) and dictA.get(key):
            if dictA.get(key) != dictB.get(key):
                print(f" {key} dictA={dictA.get(key)} dictB={dictB.get(key)}")

    return None


