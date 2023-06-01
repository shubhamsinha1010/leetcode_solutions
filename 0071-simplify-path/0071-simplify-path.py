class Solution:
    def simplifyPath(self, path: str) -> str:
            # Split the path by '/'
        components = path.split('/')

        # Initialize a stack to track directories
        stack = []

        # Process each component of the path
        for component in components:
            if component == '' or component == '.':
                # Ignore empty components or current directory references
                continue
            elif component == '..':
                # If encountering '..', go up one level by popping the last directory from the stack
                if stack:
                    stack.pop()
            else:
                # Add the directory to the stack
                stack.append(component)

        # Join the directories in the stack to form the canonical path
        canonical_path = '/' + '/'.join(stack)

        return canonical_path
