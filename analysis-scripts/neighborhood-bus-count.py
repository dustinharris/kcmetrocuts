import re
import collections
words = re.findall('\w+', open('service-reduction-summary.txt').read().lower())
print collections.Counter(words).most_common(50)