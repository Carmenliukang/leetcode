#!/usr/bin/env python
# encoding: utf-8


class Solution:
    def simplifyPath(self, path: str) -> str:
        r = []
        for s in path.split('/'):
            r = {'': r, '.': r, '..': r[:-1]}.get(s, r + [s])
        return '/' + '/'.join(r)


if __name__ == '__main__':
    path = "/a/../../b/../c//.//"
    print(Solution().simplifyPath(path))
