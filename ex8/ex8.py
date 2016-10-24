# -*- coding: utf-8 -*-

formatter = '%r %r %r %r'

print formatter % (1,2,3,4)
print formatter % ('ein', 'zwei', 'drei', 'vier')
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
"Hey, I've just met you.",
"And this is crazy.",
"So here's my number.",
"Call me 'Maybe'."

)
