print('\n***** BİLGİ YARIŞMASINA HOŞGELDİNİZ *****\n\n')
print('* Yarışmamız Toplam 10 sorudan Oluşmaktadır.\n* Her soru 10 Puandır.\n')
print('***** BAŞARILAR ***** \n\n'.center( 24 ,'*'))    


# QUESTION

class Question:
    def __init__(self, text, choices, answer):
        self.text = text
        self.choices = choices
        self.answer = answer
        
    def checkAnswer  (self, answer):
        return self.answer == answer

#QUIZ

class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0
        self.questionsIndex = 0
        
    def getQuestion(self):
        return self.questions[self.questionsIndex]
    
    def displayQuestion(self):
        question = self.getQuestion()
        
        
        print(f'SORU {self.questionsIndex + 1} : \n{question.text}\n')
        
        for q in question.choices:
            print('-' + q)
            
        answer = input('CEVAP : ')
        self.guess(answer)
        self.loadQuestion()
        
        
    def guess(self, answer):
        question = self.getQuestion()
        
        if question.checkAnswer(answer):
            self.score += 10
        self.questionsIndex += 1
        
        
    def loadQuestion(self):
         
         if len(self.questions) == self.questionsIndex:
             self.showScore()
         else:
             self.displayProgress()
             self.displayQuestion()
             
    def showScore(self):
         print('\nSCORE : ', self.score)
         
     
    def displayProgress(self):   
        totalQuestion = len(self.questions)
        questionNumber = self.questionsIndex + 1
        
        
        if (questionNumber > totalQuestion):
            print('Yarışma bitti. ')
            
        else:
            print('\n')
            print(f'Question {questionNumber} of {totalQuestion}'.center( 40 ,'*'))
            print('\n')
            
q1 = Question("Python'da 'Hello World' çıktısını hangisi verir ?", ['A)- echo("Hello World");', 'B)- p("Hello World")', 'C)- print("Hello World")', 'D)- printf("Hello World");'], 'C') 
q2 = Question("Python'da hangisi yorum satırı ekler ?", ['A)- //This is a comment', 'B)- /*This is a comment*/', 'C)- #This is a comment', 'D)- This is a comment'], 'C')
q3 = Question("Python'da hangisi dosya uzantısıdır ?", ['A)- .py', 'B)- .pyth', 'C)- .pt', 'D)- .ph'], 'A') 
q4 = Question("Hangisi Fonksiyon oluşturur ?", ['A)- create myFunction():', 'B)- class myFunction():', 'C)- function myfunction():', 'D)- def myfunction():'], 'D')
q5 = Question("Ekrana yazı yazdırılmasını sağlayan komut hangisidir ?", ['A)- .pyth', 'B)- .py', 'C)- .pt', 'D)- .ph'], 'B')
q6 = Question("len('Programlama')\nAşağıdakilerden hangisi yukarıda verilen Python komut satırı çalıştırıldığında programın vereceği çıktıdır ?", ['A)- Prg', 'B)- 11', 'C)- len', 'D)- Programlama '], 'B')
q7 = Question("liste.append() komutunun görevi aşağıdakilerden hangisidir ?", ['A)- Listeye yeni eleman eklemeyi sağlar', 'B)- Listede kaç elaman olduğunu, karakter sayısını verir', 'C)- Liste oluşturmayı sağlar', 'D)- Listeden eleman silmeyi sağlar'], 'A')
q8 = Question("Aşağıdaki karşılaştırma operatörlerinden hangisi eşitse ifadesinin karşılığıdır ?", ['A)- ==', 'B)- =!', 'C)- =<', 'D)- <>'], 'A')
q9 = Question("Sayısal bir ifadeyi Metinsel bir ifadeye çevirmek için hangi komutu kullanırız ?", ['A)- Numeric()', 'B)- Str()', 'C)- Float()', 'D)- İnt()'], 'B')
q10 = Question("Hangisi doğru while döngüsüdür ?", ['A)- while x > y {', 'B)- x > y while {', 'C)- while x > y:', 'D)- while (x > y)'], 'C')
      
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]

quiz = Quiz(questions)

quiz.loadQuestion()

        


