def read_text():
       qouotes = open("/Users/admin/Desktop/movie_quotes.txt")
       contents_of_file=qouotes.read()
       print(contents_of_file)
       qouotes.close()

list=['banana','apple','apolo']

def check_profanity(list,word):
    for x in list:
        if x.lower()==word.lower() :
            return ("this word is a curse word")
        elif list.index(x)==len(list)-1:
            return("Concrats this word is not a course word")

read_text()
word=input('write a word')
if_course=check_profanity(list,word)
print(if_course)
