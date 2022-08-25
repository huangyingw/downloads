class Solution(object):
    def simplifyPath(self, path):
        path_list = path.split('/')
        result = []
        for item in path_list:
            if item == '..' and result:
                result.pop()
            elif item and item != '.':
                result.append(item)
        return '/' + '/'.join(result)

