#!/usr/bin/python3
Message = 'NAANAAANNNAANAAAANANANANAAAAAAAANNAANAAANAAANANNAAAAAAAANNNAANAAAAANAANAAAA'
encMessage = Message.replace('N', 'B')
chars = [(encMessage[i:i+5]) for i in range(0, len(encMessage), 5)]
alphabet = {'AAAAA':'A',
            'AAAAB':'B',
            'AAABA':'C',
            'AAABB':'D',
            'AABAA':'E',
            'AABAB':'F',
      	    'AABBA':'G',
            'AABBB':'H',
            'ABAAA':'I',
            'ABAAB':'K',
	    'ABABA':'L',
	    'ABABB':'M',
	    'ABBAA':'N',
	    'ABBAB':'O',
	    'ABBBA':'P',
	    'ABBBB':'Q',
	    'BAAAA':'R',
	    'BAAAB':'S',
	    'BAABA':'T',
	    'BAABB':'U/V',
	    'BABAA':'W',
	    'BABAB':'X',
	    'BABBA':'Y',
	    'BABBB':'Z'}

decMessage = ''
for char in chars:
	if char in alphabet:
		decMessage += alphabet[char]
print('HTB{'+decMessage[9:]+'}')
