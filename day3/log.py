import re
from collections import Counter

# '169.197.108.42 - - [26/Dec/2019:10:02:20 +0200] "GET / HTTP/1.1" 200 1814 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"
# '84.110.208.186 - - [26/Dec/2019:00:37:57 +0200] "-" 408 5165 "-" "-"'
line_pattern = re.compile(r'^(?P<ip>[^ ]+) - - \[[^]]+\] "([A-Z]+ (?P<url>[^ ]+) .*|-)" (?P<response>[0-9]+)')
entries = []
with open('log.txt') as file:
    for line in file:
        if match := line_pattern.search(line):
            entries.append(match.groupdict())

# ips_with_408 = [e['ip'] for e in entries if e['response'] == '408']
# count_ips = Counter(ips_with_408)
# print(count_ips)

print([e['url'] for e in entries if e['response'] == '404'])




