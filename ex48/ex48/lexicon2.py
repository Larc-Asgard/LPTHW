#alternative from Jothan

class Lexicon(object):
    def scan(self, userinput):
        words = userinput.split()
        output = []

        for item in words:
            result = self.label(item)
            output.append(result)
            return output
    def label(self, item):
        if item in ['north','south','east']:
            return ('direction', item)
        elif item in ['go', 'kill', 'eat']:
            return ('verb', item)
        elif item in ['bear', 'princess']:
            return ('noun',item)
        elif item in ['the', 'in','of']:
            return ('stop',item)
        else:
            try:
                number = int(item)
                return ('number', item)
            except ValueError:
                    return ('error', item)

lexicon = Lexicon()
