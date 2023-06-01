class Solution:
    def simplifyPath(self, path: str) -> str:
        components = path.split('/')
        stack = []

        for component in components:
            if component in ('', '.'):
                continue
            elif component == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(component)

        canonical_path = '/' + '/'.join(stack)
        return canonical_path
