import random

class Doctor():
    
    REPLACEMENTS = {"I":"you", "me":"you", "my":"your",
                    "we":"you", "us":"you", "mine":"yours"}
    
    QUALIFIERS = ['why do you say that','you seem to think that',
                  'did I just hear you say that', 'Why do you believe that']
    
    HEDGES = ['Go on.', 'I would like to hear more about that.',
              'And what do you think about this?', 'Please continue.']

    def __init__(self):
        self.history = []
    
    def greeting(self):
        return 'Good moring, how can I help you today?'
    
    def farewell(self):
        return 'Have a nice day!'
    
    def reply(self, sentence):
        choice = random.randint(1,10)
        if choice == 1:
            if len(self.history)> 3:
                answer = 'Earlier you said that' + \
                self.change_person(random.choice(self.history))
            
            else:
                answer = random.choice(Doctor.HEDGES)
                
        elif choice in (2,3,4,5):
            answer = random.choice(Doctor.QUALIFIERS)+ \
                self.change_person(sentence)
        
        else:
            answer = random.choice(Doctor.HEDGES)
        self.history.appen(sentence)
        return answer
    def change_person(self, sentence):
        oldlist = sentence.split()
        newlist = []
        for word in oldlist:
            if word in Doctor.REPLACEMENTS:
                newlist.append(Doctor.REPLACEMENTS[word])
            else:
                newlist.append(word)
        return ' '.join(newlist)
    
            
      