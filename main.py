import tkinter

def getWordList():
  f= open('Words','r')

  array = []

  i = 0

  for line in f:
    if(line != '\n'):
      array.append(line[:-1])
    else:
      continue

  groupedArray = []

  for word in array:
    if(i%2 == 0):
      groupedArray.append([word])
    elif(i%2 == 1):
      groupedArray[-1].append(word)

    i = i +1

  return groupedArray



        


class LDMAppGUI:

    def __init__(self):
        # Keep track of what word has been displayed. Set to 1 because the first word
        # (index zero is already set below
        self.word_index = 1
        self.word_list = getWordList()

        # Construct the gui
        self.window = tkinter.Tk()
        self.window.title("Lexical Decision Making")
        self.window.bind('<Key>',self.nextWord)

        self.word_1_label = tkinter.Label(self.window, text = self.word_list[0][0])
        self.word_2_label = tkinter.Label(self.window, text = self.word_list[0][1])

        self.word_1_label.pack()
        self.word_2_label.pack()


    # Events
    def nextWord(self,event):
        key_pressed = str(event.char)
        
        if(self.word_index < len(self.word_list)):

            if key_pressed == 't':
                pass # do something
            elif key_pressed == 'f':
                pass # do something else
            else:
                # unrekognized key, don't do anything
                return
            
            
            # if we haven't returned yet means that the key was recognized, so
            # we can update the
            word_pair = self.word_list[self.word_index]
            self.word_index += 1

            self.word_1_label["text"] = word_pair[0]
            self.word_2_label["text"] = word_pair[1]
            


    def mainloop(self):
        self.window.mainloop()




# actually run the app
myApp = LDMAppGUI()
myApp.mainloop()



