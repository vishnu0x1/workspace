import re

pattern = input()
text = input()

pattern = '(?=' + pattern + ')'
match_start_indices = [match.start() for match in re.finditer(pattern, text)]

answer = ' '.join(str(x) for x in match_start_indices)
print(answer)
