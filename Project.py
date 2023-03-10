import sys
import re
import spacy
import neuralcoref 
import utils

# Function that returns true if the word is found 

def isWordPresent(sentence, word): 
      
    # To break the sentence in words 
    s = sentence.split(" ")
  
    for i in s: 
  
        # Comparing the current word 
        # with the word to be searched 
        if (i == word): 
            return True
    return False



def problem_category_classification(question,input_question):
    
    predicted_class=""
    processed_question=""
    
    for tokens in doc:
        if(tokens.pos_!="PUNCT"):
            processed_question = processed_question + tokens.text + " "
    
    for i in range(0,sentence_length):
        
        if(doc[i].tag_=="JJR" or doc[i].tag_=="RBR" or (isWordPresent(processed_question,"another")) or (isWordPresent(processed_question,"than"))):
            predicted_class="compare"
            return predicted_class
        
    for i in range(0,sentence_length):
        #if(isWordPresent(processed_question,"each") or isWordPresent(processed_question,"sold") or isWordPresent(processed_question,"whole") or doc[i].lemma_=="time" or doc[i].lemma_=="row" or doc[i].lemma_=="mile" or doc[i].lemma_=="kilometer" or doc[i].lemma_=="minute" or doc[i].lemma_=="day" or doc[i].lemma_=="hour" or (isWordPresent(processed_question,"do") and (not isWordPresent(processed_question,"all") or not isWordPresent(processed_question,"altogether"))) or isWordPresent(processed_question,"every") or isWordPresent(processed_question,"per") or (doc[i].lemma_=="share" and isWordPresent(processed_question,"among")) or doc[i].lemma_=="split" or doc[i].lemma_=="divide" or doc[i].lemma_=="cost" or doc[i].lemma_=="square" or doc[i].lemma_=="cover"):
         if(isWordPresent(processed_question,"each") or isWordPresent(processed_question,"feet") or (doc[i].lemma_=="sell" and isWordPresent(processed_question,"does")) or isWordPresent(processed_question,"whole") or doc[i].lemma_=="time" or doc[i].lemma_=="row" or doc[i].lemma_=="mile" or doc[i].lemma_=="kilometer" or doc[i].lemma_=="minute" or doc[i].lemma_=="day" or doc[i].lemma_=="hour" or isWordPresent(processed_question,"do") or isWordPresent(processed_question,"every") or isWordPresent(processed_question,"per") or (doc[i].lemma_=="share" and isWordPresent(processed_question,"among")) or doc[i].lemma_=="split" or doc[i].lemma_=="divide" or doc[i].lemma_=="cost" or doc[i].lemma_=="square" or doc[i].lemma_=="cover"):
            
            if(isWordPresent(processed_question,"do") and (isWordPresent(processed_question,"all") or isWordPresent(processed_question,"altogether"))):
                predicted_class="combine"
                return predicted_class
            
            elif(isWordPresent(processed_question,"added")):
                predicted_class="change"
                return predicted_class
            
            elif(isWordPresent(processed_question,"miles")):
                 
                if(isWordPresent(processed_question,"left")):
                    predicted_class="change"
                    return predicted_class
                else:
                    print("1")
                    predicted_class="div_mul"
                    return predicted_class
                

                
            else:
                print("2")
                predicted_class="div_mul"
                return predicted_class
        
    for i in range(0,sentence_length):    
        if(isWordPresent(processed_question,"all") or isWordPresent(processed_question,"total") or isWordPresent(processed_question,"altogether") or isWordPresent(processed_question,"together") or isWordPresent(processed_question,"overall")):
            predicted_class="combine"
            return predicted_class
        
    for i in range(0,sentence_length):     
        if(isWordPresent(processed_question,"now") or isWordPresent(processed_question,"eaten") or isWordPresent(processed_question,"sum") or doc[i].lemma_=="add" or doc[i].lemma_=="join" or doc[i].lemma_=="combine" or isWordPresent(processed_question,"left") or isWordPresent(processed_question,"change") or isWordPresent(processed_question,"rest") or isWordPresent(processed_question,"remain") or isWordPresent(processed_question,"empty") or isWordPresent(processed_question,"out") or isWordPresent(processed_question,"off") or isWordPresent(processed_question,"leftover") or doc[i].lemma_=="take" or isWordPresent(processed_question,"gives") or isWordPresent(processed_question,"lost") or isWordPresent(processed_question,"loses") or isWordPresent(processed_question,"shares") or isWordPresent(processed_question,"away")):
            predicted_class="change"
            return predicted_class
    

def operation_prediction(question_body,query_sentence,question,input_question,predicted_problem_category):
    
    question_body1 = ""
    query_sentence1 = ""
    
    operation=""
    item_name=""
    processed_question=""
    query_sentence_noun_chunks=[]
    persons=[]
    
    
    question_body_doc=nlp(question_body)
    query_sentence_doc=nlp(query_sentence)

    question_body_length=len(question_body_doc)
    query_sentence_length=len(query_sentence_doc)
    
    #Removing punctuation from the original question
    
    for tokens in doc:
        if(tokens.pos_!="PUNCT"):
            processed_question = processed_question + tokens.text + " "
            
    #Checking for "compare" type.       
    
    if(predicted_problem_category=="compare"):
        
        if(isWordPresent(processed_question,"some")):
            #Tommy had some balloons. His mom gave him 34 more balloons for his birthday. Then, Tommy had 60 balloons. How many balloons did  Tommy have to start with?
            #Ethan has some presents. Alissa has 22 more than Ethan. If Alisha has 32 presents, how many presents does Ethan have?
            print("Presence of keyword 'some' in the question body indicates that, one quantity is unknown. To identify the unknown quantity, always subtraction operation is performed.")
            print("s2")
            operation="subtraction"
            return operation
                
        if(isWordPresent(processed_question,"another")):
            #Jennifer starts with 7 apples. She finds another 74. How many apples does Jennifer end with?
            print("Keyword 'another' is normally associated with (finds another/gets another etc.) Therefore, its presence in question body indicates positive transfer if no comparative adjective is present along with.Therefore, the operation must be addition.")        
            print("a4")
            operation="addition"
            return operation
        
        for i in range(0,query_sentence_length):
            if(query_sentence_doc[i].tag_=="JJR" or query_sentence_doc[i].tag_=="RBR"):
                #Anne weighs 67 pounds. Douglas weighs 52 pounds. How much heavier is Anne than Douglas?
                #John needs $2.50. He has $0.75. How much more money does he need?
                print("Presence of comparative adjective in the query sentence always indicate subtraction operation.")
                print("s1")
                operation="subtraction"
                return operation
        
        for i in range(0,question_body_length):
            if(question_body_doc[i].tag_=="JJR" or question_body_doc[i].tag_=="RBR"):

#                

                if(isWordPresent(processed_question,"than")):
                    print("Presence of 'than' keyword in the question body indicates that, one quantity is being compared with another quantity.")
                    if(len(question_body_doc._.coref_clusters)!=0):
                        question_body_after_resolved_coref=question_body_doc._.coref_resolved
                       
                        question_body_after_resolved_coref=question_body_after_resolved_coref
                    else:
                        question_body_after_resolved_coref=question_body

                    question_body_coref_doc=nlp(question_body_after_resolved_coref)
                    for tokens in question_body_coref_doc:
                        if((tokens.tag_=="NNP") and (tokens.text not in persons)):
                            persons.append(tokens.text)
                    print("Proper nouns:",persons)       

                    question_body_coref_doc_length=len(question_body_coref_doc)
                    

                    try:
                        for i in range(0,question_body_coref_doc_length):
                            if(str(question_body_coref_doc[i].text)=="than" and str(question_body_coref_doc[i+1].text)==persons[0]):
                                #Ethan has 31 presents. Alissa has 22 more than Ethan. How many presents does Alissa have?
                                print("One quantity in known. Comparing (more) the unknown quantity with the known quantity.Therefore, to identify the unknown quantity,we have to perform the addition operation.")
                                print("a1")
                                operation="addition"
                                return operation

                            if(str(question_body_coref_doc[i].text)=="than" and str(question_body_coref_doc[i+1].text)==persons[1]):
                                if(isWordPresent(query_sentence,"altogether") or isWordPresent(query_sentence,"together")):
                                    print("a2")
                                    operation="addition"
                                    return operation
                                else:
                                    #Marcus has 210 baseball cards. He has 58 more than Carter. How many baseball cards does Carter have?
                                    #Sean has 223 whistles. He has 95 more whistles than Charles. How many whistles does Charles have?
                                    print("One quantity in known. Comparing (more) the known quantity with the unknown quantity.Therefore, to identify the unknown quantity,we have to perform the subtraction operation.")
                                    print("s3")
                                    operation="subtraction"
                                    return operation
                    except LookupError:  
                        print ("Index Error Exception Raised, list index out of range.")

                else:
        
                    #If there are 7 bottle caps in a box and Linda puts 7 more bottle caps inside, how many bottle caps are in the box?
                    print("Presence of comparative adjective 'more' in the problem body, indicates the operation addition.")
                    print("a3")
                    operation="addition"
                    return operation

    

        
    
    
    #Checking for "div-mul" type. 
    
    if(predicted_problem_category=="div_mul"):
        
        if(isWordPresent(query_sentence,"each")):
        
            if(question_body==""):
                #How many cookies would you have if you had 37 bags of cookies with 19 cookies in each bag?
                print('m2')
                operation="multiplication"
                return operation
                
            else:
                #Betty has 24 oranges stored in boxes. If there are 3 boxes, how many oranges must go in each box?
                print('d1')
                operation="division"
                return operation
                
        
            
        if(isWordPresent(processed_question,"per")):
            if(isWordPresent(processed_question,"miles") or isWordPresent(processed_question,"kilometers") or isWordPresent(processed_question,"meters") or isWordPresent(processed_question,"hour") or isWordPresent(processed_question,"day") or isWordPresent(processed_question,"minute") or isWordPresent(processed_question,"second")):
                #print("Div-Mul new type6 question.")
                if(isWordPresent(query_sentence,"far") or isWordPresent(query_sentence,"miles") or isWordPresent(query_sentence,"kilometers") or isWordPresent(query_sentence,"meters")):
                    #If Anne wandered for 3 hours at 2 miles per hour. How far did Anne go?
                    #My car gets 20 miles per gallon. How many miles can I drive on 5 gallons of gas?
                    print('m3')
                    operation="multiplication"
                    return operation
                if(isWordPresent(query_sentence,"long") or isWordPresent(query_sentence,"gallons") or isWordPresent(query_sentence,"minutes") or isWordPresent(query_sentence,"hours") or isWordPresent(query_sentence,"seconds") or isWordPresent(query_sentence,"days")):
                    #If Charles strolled 6 miles at 3 miles per hour, how long was Charles travelling?
                    #My car gets 20 miles per gallon of gas. If Grandma’s house is 100 miles away, how many gallons of gas would it take to get to her house?
                    #Johnny practiced for the track team and ran 3 laps per minute. How many minutes did it take Johnny to run 10 laps?
                    print('d2')
                    operation="division"
                    return operation
            else:
                for j in range(0,query_sentence_length):
                    if(query_sentence_doc[j].tag_=="CD"):
                        #print("Div-Mul new type7 question.")
                        #Lukas averages 12 points per game in basketball. How many points would he score in 5 games?
                        print('m4')
                        operation="multiplication"
                        return operation
                    
        
        for i in range(0,sentence_length):
            if(doc[i].lemma_=="cost"):
               
                for k in range(0,query_sentence_length):
                    
                    if((query_sentence_doc[k].text=="how" and query_sentence_doc[k+1].text=="much")):       
                            #Each bottle cap costs $2.00. How much do 6 bottle caps cost?
                            print("Since keyword 'cost' is present in the question, the query sentence starts with 'how much' means asking about the amount of money.Therefore the operation must be multiplication.")
                            print('m6')
                            operation="multiplication"
                            return operation
                    if(query_sentence_doc[k].text=="how" and query_sentence_doc[k+1].text=="many"):
                            #I have 80 cents to buy candy. If each gumdrop costs 4 cents, how many gumdrops can I buy?
                            print("Since keyword 'cost' is present in the question, the query sentence starts with 'how many' means asking about the no. of items.Therefore the operation must be division.")
                            print('d5')
                            operation="division"
                            return operation
                        
        
        if(isWordPresent(processed_question,"times")):
            #print("Div-Mul type04 question.")
            if(isWordPresent(question_body,"times")):
                #Stephanie went to the store 8 times last month. She buys 2 oranges each time she goes to the store. How many oranges did Stephanie buy last month?
                print('m7')
                operation="multiplication"
                return operation
            
            if(isWordPresent(query_sentence,"times")):
                if(isWordPresent(processed_question,"will")):
                    #Mrs. Hilt measured the distance from her desk to the water fountain. It was 30 feet. How many feet will Mrs. Hilt walk on her trips to the  fountain if she goes to the water fountain 4 times today?
                    print('m8')
                    operation="multiplication"
                    return operation
                else:
                    #Sarah picked 45 apples. Her brother picked 9 apples. How many times as many apples did Sarah pick?
                    print('d6')
                    operation="division"
                    return operation
                
#             
            
        if(isWordPresent(query_sentence,"do")):
        
                print('m9')
                operation="multiplication"
                return operation

       
        if(isWordPresent(processed_question,"cover")):
            #Jesse’s room is 12 feet long and 8 feet wide. How much carpet does she need to cover the whole floor?
            print('m10')
            operation="multiplication"
            return operation

        if(isWordPresent(processed_question,"whole") and not(isWordPresent(processed_question,"cover"))):
            #A cereal box holds 18 cups of cereal. Each serving is 2 cups. How many servings are in the whole box?
            print('d7')
            operation="division"
            return operation
        
        
        if(isWordPresent(processed_question,"split")):
            #Jeffrey wants to split a collection of bottle caps into groups of 2. Jeffrey has 12 bottle caps. How many groups will be created?
            print('d8')
            operation="division"
            return operation

       
        if(isWordPresent(processed_question,"sold")):
            #If Karen sold 36 boxes of Tagalongs, how many cases of 12 boxes does Karen pickup from the cookie mom?
            print('d9')
            operation="division"
            return operation

          
        
        if(isWordPresent(processed_question,"fast")):
           
            #Emily sprinted to Timothy's house. It is 10 miles from Emily's house to Timothy's house. It took Emily 2 hours to get there. How fast did Emily go?
            print('d10')
            operation="division"
            return operation
        if(isWordPresent(processed_question,"far")):
            
            #Marie can bike at a speed of 12 miles an hour. How far can she bike in 31 hours?
            print('m11')
            operation="multiplication"
            return operation

        if(isWordPresent(question_body,"each") or isWordPresent(question_body,"every")):
            for j in range(0,query_sentence_length):
                if(query_sentence_doc[j].tag_=="CD"):
                    #print("Div-Mul new type2 question.")
                    #There are 6 marbles in each box. How many marbles are in 3 boxes?
                    print('m12')
                    operation="multiplication"
                    return operation
                
            
            if(isWordPresent(query_sentence,"total") or isWordPresent(query_sentence,"all") or isWordPresent(query_sentence,"altogether")):
            #if(isWordPresent(processed_question,"total") or isWordPresent(processed_question,"all") or isWordPresent(processed_question,"altogether")):
                #print("Div-Mul new type3 question.")
                #Mrs. Hilt saw 3 bugs eat 2 flowers each. How many flowers total did the bugs eat?
                #Mrs. Hilt bought 6 hot dogs. Each hot dog cost 50 cents. How much money did she pay for all of the hot dogs?
                print('m13')
                operation="multiplication"
                return operation
            
            for j in range(0,question_body_length):
                if(question_body_doc[j].text=="each" or question_body_doc[j].text=="every"):
                    each_index=j
                    break;

            for k in range(each_index+1,question_body_length):
                if(question_body_doc[k].pos_=="NOUN"):
                    item_name=item_name+" "+question_body_doc[k].text
                    #item_name=item_name+question_body_doc[k].text
                    if(question_body_doc[k+1].pos_!="NOUN"):
                        break;

            print("Item name:",item_name)
            item_name_doc=nlp(item_name)
            item_name_doc_length=len(item_name_doc)
            #print("item_name_doc_length",item_name_doc_length)

            for chunk in query_sentence_doc.noun_chunks:
                    query_sentence_noun_chunks.append(chunk.text)

            print("Noun chunks: ",query_sentence_noun_chunks)
            query_sentence_noun_chunks_doc=nlp(query_sentence_noun_chunks[0])
            wh_question=" ".join([token.lemma_ for token in query_sentence_noun_chunks_doc])
            print("wh_question: ",wh_question)

            wh_question_doc=nlp(wh_question)
            wh_question_last_noun_spacy=wh_question_doc[len(wh_question_doc)-1]
            wh_question_last_noun=str(wh_question_last_noun_spacy)
            print("last noun in wh question:",wh_question_last_noun)

            if(item_name_doc_length>0):

                item_name_last_noun_spacy=item_name_doc[len(item_name_doc)-1]
                item_name_last_noun=str(item_name_last_noun_spacy)
                print("last noun in item name:",item_name_last_noun)

                
                if(item_name_last_noun==wh_question_last_noun):
                   
                    #The school is planning a field trip. There are 14 students and 2 seats on each school bus. How many buses are needed to take the trip?
                    print('d11')
                    operation="division"
                    return operation
                else:
                    #michelle has 7 boxes of crayons. each box holds 5 crayons. how many crayons does michelle have?
                    print('m14')
                    operation="multiplication"
                    return operation

            else:

                if(question_body_doc[each_index-1].pos_=="NOUN"):
                   
                    item_name=question_body_doc[each_index-1].lemma_
                    item_name=str(item_name)
                    print("Item name:",item_name)
                    if(item_name==wh_question_last_noun):
                        #mrs. heine is buying valentine’s day treats for her 2 dogs. if she wants to buy them 3 heart biscuits each, how many biscuits does she need to  buy?
                        print('m15')
                        operation="multiplication"
                        return operation
                    else:
                        #There are 14240 books in a library. They are arranged on shelves that hold 8 books each. How many shelves are in the library?
                        print('d12')
                        operation="division"
                        return operation
                    
        for k in range(0,sentence_length):
            if((doc[k].lemma_=="row") or (isWordPresent(processed_question,"hours")) or (isWordPresent(processed_question,"miles")) or (isWordPresent(processed_question,"will"))):
                #A garden has 52 rows and 15 columns of bean plans. How many plants are there in all?
                print("Presence of rows/miles/hours/will in the question, mostly indicates multiplication operation.")
                print('m1 ')
                operation="multiplication"
                return operation
    
    
    
    #Checking for "combine" type. 
    
    if(predicted_problem_category=="combine"):
        
        if(isWordPresent(question_body,"all")):
            if(isWordPresent(processed_question,"will")):
                #Bridget has 4 Skittles. Henry has 4 Skittles. If Henry gives all of his Skittles to Bridget, how many Skittles will Bridget have?
                print("Since each/every is not present in the question, the presence of the keyword 'all' in the query sentence indicates the operation addition.")
                print("a5")
                operation="addition"
                return operation
            else:
                #Robin had 18 pieces of gum. Her brother gave her some more pieces. Now Robin has 44 pieces in all. How many pieces of gum did Robin's  brother give her?
                print("s4")
                operation="subtraction"
                return operation
            
        if(isWordPresent(query_sentence,"all")):
            #Mary’s mom is getting ready for Mary’s birthday party. She blew up 6 balloons this morning and 5 balloons this afternoon. How many balloons  did she blow up in all?
            print("Since each/every is not present in the question, the presence of the keyword 'all' in the query sentence indicates the operation addition.")
            print("a7")
            operation="addition"
            return operation
            
      
        if(isWordPresent(processed_question,"total")):
            #I read 21 pages of my English book yesterday. Today, I read 17 pages. What is the total number of pages did I read?
            print("Since each/every is not present in the question, the presence of the keyword 'total' in the query sentence indicates the operation addition.")
            print("a6")
            operation="addition"
            return operation
        
        if(isWordPresent(processed_question,"together")): 
            #I read 21 pages of my English book yesterday. Today, I read 17 pages. What is the total number of pages did I read?
            print("Since each/every is not present in the question, the presence of the keyword 'together' in the question indicates the operation addition.")
            print("a6.1")
            operation="addition"
            return operation
            
        if(isWordPresent(query_sentence,"altogether")):
            #Cindy’s mom baked 41 cookies. Paul’s dad baked 38 cookies. They both brought them to school for a party. How many cookies did they  have altogether?
            print("Since each/every is not present in the question, the presence of the keyword 'altogether' in the query sentence indicates the operation addition.")
            print("a8")
            operation="addition"
            return operation
            
        if(isWordPresent(question_body,"altogether")):
            #There are 40 boys and some girls on the playground. There are 117 children altogether. How many girls are on the playground?
            print("s5")
            operation="subtraction"
            return operation
        
        
    #Checking for "change" type. 
    
    if(predicted_problem_category=="change"):
        
        
        for k in range(0,query_sentence_length): 
            if(query_sentence_doc[k].lemma_=="add" or query_sentence_doc[k].lemma_=="join"):
                #Adolfo made a tower with 35 blocks. He added some more blocks and now he has 65 blocks. How many did he have to  add?
                print("In question body,one quantity is known and the another is unknown but their total is known.Presence of add/join keyword in the query sentence means it is asking about the unknown quantity. Therefore the operation must be subtraction.")
                print("s6")
                operation="subtraction"
                return operation
        
        for k in range(0,question_body_length): 
            if(question_body_doc[k].lemma_=="add" or question_body_doc[k].lemma_=="join"):
                #3 owls were sitting on the fence. 2 more owls joined them. How many owls are on the fence now?
                print("keyword 'add/join' is present in question body only indicates that one quantity is being added/joind to another quantity. This clearly indicate addition")
                print("a9")
                operation="addition"
                return operation

        if(isWordPresent(processed_question,"sum")):
            #Gino has 63 popsicle sticks. I have 50 popsicle sticks. What is the sum of our popsicle sticks?
            print("Since each/every is not present in the question, the presence of the keyword 'sum' in the query sentence indicates the operation addition.")
            print("a10")
            operation="addition"
            return operation
        
        for i in range(0,sentence_length):
            if(isWordPresent(processed_question,"away") or isWordPresent(processed_question,"stole") or isWordPresent(processed_question,"empty") or isWordPresent(processed_question,"rest") or isWordPresent(processed_question,"loses") or isWordPresent(processed_question,"lost") or isWordPresent(processed_question,"change") or (doc[i].lemma=="take") or isWordPresent(processed_question,"off") or isWordPresent(processed_question,"shares") or isWordPresent(processed_question,"eaten") or isWordPresent(processed_question,"gives")):
                #Virginia starts with 96 eggs. Amy takes 3 away. How many eggs does Virginia end with?
                #There are 47 eggs in a box. Harry takes 5 eggs. How many are left?
                #Josh had 16 marbles in his collection. He lost 7 marbles. How many marbles does he have now?
                #Marie starts with 95 erasers. She loses 42. How many erasers does Marie end with?
                #Adam has $5.00 to buy an airplane that costs $4.28. How much change will he get?
                #Isha’s pencil is 31 inches long. If she sharpens it, now her pencil is 14 inches long. How much did she sharpen off of her pencil?
                print("Presence of away/stole/empty/rest/loses/lost/change/takes/off/shares/eaten/gives keywords in the question directly indicate subtraction operation.")
                print("s7")
                operation="subtraction"
                return operation
    
    
        for i in range(0,query_sentence_length):
            if(str(query_sentence_doc[i].text)=="left" and query_sentence_doc[i].pos_=="VERB"):
#                 
                    print("Presence of 'left' keyword in the query part, directly indicate subtraction operation.")
                    print("s8")
                    operation="subtraction"
                    return operation

        for i in range(0,question_body_length):
            
            if(str(question_body_doc[i].text)=="left" and question_body_doc[i].pos_=="VERB"):
                #Sarah had some trucks. She gave 13 to Jeff, and now she has 38 trucks left. How many trucks did Sarah have to start with?
                print("Presence of 'left' keyword in the question body, directly indicate addition operation.")
                print("a11")
                operation="addition"
                return operation
            
        for i in range(0,query_sentence_length):
            if(str(query_sentence_doc[i].text)=="begin" and str(query_sentence_doc[i+1].text)=="with"):
                print("a11.1")
                operation="addition"
                return operation



def finding_relevant_quantities(input_question,predicted_problem_category,predicted_operation):
    x=0
    
    question_body = ""
    query_sentence = ""
    quantity_count=0
    quantity_count_qb=0
    count=0
    tokens_left_child=[]
    
    query_sentence_noun_chunks=[]
    noun_chunk_with_wh=""
    query_sentence_location=""
    query_sentence_item=""
    query_sentence_entity_name=""
    query_sentence_persons=[]
    relevant_quantities=[]
    relevant_item=[]
    
    quantity=[]
    unit=[]
    
    nlp = spacy.load('en_core_web_sm') 
    neuralcoref.add_to_pipe(nlp)
    nlp.add_pipe(nlp.create_pipe('sentencizer'))
    input_question_doc=nlp(input_question)
    
    
    #finding number of quantities in the question
    
    for tokens in input_question_doc:
        if(tokens.tag_=='CD'):
            try:
                num=float(tokens.text)
                if(isinstance(num,float)):
                    quantity_count = quantity_count+1
                    print(num)
            except:
                continue
            
        
    #print("Number of quantities:",quantity_count)
    
    if(quantity_count==2): # having only relevant quantities in the question
        
        for tokens in input_question_doc:
            if(tokens.tag_=="CD"):
                try:
                    num=float(tokens.text)
                    if(isinstance(num,float)):
                        relevant_quantities.append(tokens.text)
                       
                except:
                    continue
                 
        print('\n')        
        print('\033[1m'+"Quantities: "+'\033[0m',relevant_quantities)
            
    if(quantity_count>2): # having irrelevant quantities also in the question
        
        #Splitting up the input question into question body and query sentence.

        sentence_length=len(input_question_doc)
        query_sentence_pos = sentence_length

        for i in range(0,sentence_length):
            if(input_question_doc[i].tag_=="WP" or input_question_doc[i].tag_=="WRB"):
                query_sentence_pos = i
                #print('query_sentence_pos: ',query_sentence_pos)
                count=count+1
                #print(count)
                if(count==1):
                    for j in range(i,sentence_length):
                        query_sentence=" ".join([query_sentence,input_question_doc[j].text])
                        query_sentence=" ".join(query_sentence.split())
                else:
                    question_body = ""
                    query_sentence = ""
                    for j in range(i,sentence_length):
                        query_sentence=" ".join([query_sentence,input_question_doc[j].text])
                        query_sentence=" ".join(query_sentence.split())

        #print('\033[1m'+"Problem question Q:"+'\033[0m',query_sentence)

        for k in range(0,query_sentence_pos):
            question_body = " ".join([question_body,input_question_doc[k].text])    
            question_body=" ".join(question_body.split())
        #print('\033[1m'+"Problem body Q:"+'\033[0m',question_body)
                    
        #Resolving the coreference of the question body.
        
        question_body_doc=nlp(question_body) 
        if(len(question_body_doc._.coref_clusters)!=0):
            question_body_after_resolved_coref=question_body_doc._.coref_resolved
            print('\033[1m'+"Question body after resolved coreference: "+'\033[0m',question_body_after_resolved_coref)

        else:
            question_body_after_resolved_coref=question_body
        
        #Rule based conjunction elemination and reconstruction of the sentence.
        
        after_resolved_doc = nlp(question_body_after_resolved_coref)
        sentences = [sent.string.strip() for sent in after_resolved_doc.sents]
       
        sent_numbers=len(sentences)
        
        
        for i in range(0,sent_numbers): # Iterating through each sentence
            
            each_sent_quant_count=0
            conj_flag=0  # to determine if, the sentence has any conjunction or not.
            sent_doc=nlp(sentences[i])
            
            for tokens in sent_doc:
                if(tokens.pos_=="NUM"):
                    each_sent_quant_count=each_sent_quant_count+1
                if(tokens.dep_=="cc"):
                    conj_flag=1
            
            
            if(each_sent_quant_count>=2 and conj_flag==1):
                for tokens in sent_doc:
                   

                    if(tokens.dep_=="nsubj" and tokens.head.dep_=="ROOT"):
                        
                        for x in tokens.lefts:
                            tokens_left_child.append(x.text)

                        if(len(tokens_left_child)==0):
                            for w in tokens.head.rights:
                                if(w.dep_=="dobj"):
                                    for y in w.lefts:
                                        if(y.dep_=="nummod"):
                                            first_part=tokens.text+" "+tokens.head.text+" "+y.text+" "+w.text
                                            sentences.remove(sentences[i])
                                            sentences.insert(i,first_part)
                                    for z in w.rights:
                                        
                                        if(z.dep_=="cc"):
                                            continue;
                                        if(z.dep_=="conj"):
                                            for a in z.lefts:
                                                if(a.dep_=="nummod"):
                                                    second_part=tokens.text+" "+tokens.head.text+" "+a.text+" "+z.text
                                                    sentences.insert(i+1,second_part)
                                                break;


                                if(w.dep_=="prep"):
                                    for y in w.rights:
                                        if(y.dep_=="pobj"):
                                            for z in y.lefts:
                                                if(z.dep_=="nummod"):
                                                    first_part_2=tokens.text+" "+tokens.head.text+" "+w.text+" "+z.text+" "+y.text
                                                    
                                                    sentences.remove(sentences[i])
                                                    sentences.insert(i,first_part_2)
                                            for a in y.rights:
                                                if(a.dep_=="cc"):
                                                    continue;
                                                if(a.dep_=="conj"):
                                                    for b in a.lefts:
                                                        if(b.dep_=="nummod"):
                                                            second_part_2=tokens.text+" "+tokens.head.text+" "+w.text+" "+b.text+" "+a.text
                                                            
                                                            sentences.insert(i+1,second_part_2)
                                                        break;
                                                        
                                                        
                                                        
        print('\033[1m'+"Sentences: "+'\033[0m',sentences)
        print('\n')
        
        #Identifying the relevant quantities based on the type of operation.
        
      
           
        query_sentence_doc=nlp(query_sentence)
        query_sentence_length=len(query_sentence_doc)
            


        for i in range(0,query_sentence_length):
            if(query_sentence_doc[i].tag_=="IN" and query_sentence_doc[i+1].tag_=="DT" and query_sentence_doc[i+2].tag_=="NN"):
                query_sentence_location=query_sentence_doc[i+2].text  #Extracting location name from query sentence
                print('\033[1m'+"Location name: "+'\033[0m',query_sentence_location)
                   
                    
      
            if(query_sentence_doc[i].tag_=="NNP"): #Extracting the persons name from the query sentence.
                query_sentence_persons.append(query_sentence_doc[i].text)
                print('\033[1m'+"Person(s): "+'\033[0m',query_sentence_persons)
                    
            
        for chunk in query_sentence_doc.noun_chunks:
            query_sentence_noun_chunks.append(chunk.text)
                
        for i in range(0,len(query_sentence_noun_chunks)):
            noun_chunk_doc=nlp(query_sentence_noun_chunks[i])
            per_noun_chunk_doc=nlp(str(noun_chunk_doc))
                
            for j in range(0,len(per_noun_chunk_doc)):
                if(per_noun_chunk_doc[j].tag_=="WP" or per_noun_chunk_doc[j].tag_=="WRB"):
                    noun_chunk_with_wh=str(per_noun_chunk_doc)
                        
                if(per_noun_chunk_doc[j].text=="each" and per_noun_chunk_doc[j+1].pos_=="NOUN"):
                    query_sentence_entity_name=per_noun_chunk_doc[j+1].text
                    print('\033[1m'+"Entity name: "+'\033[0m',query_sentence_entity_name)
                
              
        wh_noun_chunk_doc=nlp(noun_chunk_with_wh)
        for i in range(0,len(wh_noun_chunk_doc)):
            

            
            if(wh_noun_chunk_doc[i].pos_=="NOUN"):
                query_sentence_item=wh_noun_chunk_doc[i].text  #Extracting item name from query sentence
                
        print('\033[1m'+"Item name: "+'\033[0m',query_sentence_item)
                    
                   
                    
        if(predicted_operation=="addition" or predicted_operation=="subtraction"):
            
            for i in range(0,len(sentences)):  #Iterating through each sentence to identify the relevant one.
                
                person_present=""

                if(query_sentence_location!=""):  #if location information is given
                   

                    if(isWordPresent(sentences[i],query_sentence_location) and (query_sentence_item!="")):
                       

                        if(isWordPresent(sentences[i],query_sentence_item)):
                           
                            #There are 8 apples in a pile on the desk. Each apple comes in a package of 11. 5 apples are added to the pile. How many apples are there in the pile?
                            sent_doc=nlp(sentences[i])
                            for j in range(0,len(sent_doc)):
                                if(sent_doc[j].tag_=="CD"):
                                    relevant_quantities.append(sent_doc[j].text)
                                    relevant_item.append(query_sentence_item)

                        else: #if item name is not present in the sentance, but , need to map the item name from previous qualified sentence.
                           
                            #There are 8 apples in a pile on the desk. Each apple comes in a package of 11. 5 more are added to the pile. How many apples are there in the pile?
                            sent_doc=nlp(sentences[i])
                            for j in range(0,len(sent_doc)):
                                if(sent_doc[j].tag_=="CD"):
                                    if((sent_doc[j+1].tag_=="JJR" or sent_doc[j-1].tag_=="DT") and len(relevant_item)!=0): #5 more or another 5
                                        relevant_quantities.append(sent_doc[j].text)



                else:  # if no location information is given
                    

                    if(len(query_sentence_persons)!=0): #if persons present in the query sentence, but location not present
                       

                        for j in range(0,len(query_sentence_persons)):

                            if(isWordPresent(sentences[i],query_sentence_persons[j])):
                                
                                person_present="true"

                        if(person_present=="true" and query_sentence_item!=""): #if person and item name both present in the query sentence & person present in the sentence.
                            

                            if(isWordPresent(sentences[i],query_sentence_item)): # if person and item name both present in the sentence
                               
                                sent_doc=nlp(sentences[i])
                                for j in range(0,len(sent_doc)):
                                    if(sent_doc[j].tag_=="CD"):
                                        relevant_quantities.append(sent_doc[j].text)
                                        relevant_item.append(query_sentence_item)

                            else: #if item name is not present in the sentence
                                
                                sent_doc=nlp(sentences[i])
                                for j in range(0,len(sent_doc)):
                                    if(sent_doc[j].tag_=="CD"):
                                        
                                        if(not(sent_doc[j+1].pos_=="NOUN")):
                                            
                                            if((sent_doc[j+1].pos_=="ADJ" or sent_doc[j+1].pos_=="ADP" or sent_doc[j-1].tag_=="DT" or sent_doc[j-1].pos_=="VERB") and len(relevant_item)!=0): #5 more or another 5
                                                
                                                relevant_quantities.append(sent_doc[j].text)
                                                relevant_item.append(query_sentence_item)

                        if(person_present=="true" and query_sentence_item==""): # if both location and item are not present in the query sentence
                            

                            sent_doc=nlp(sentences[i])
                            for j in range(0,len(sent_doc)):
                                if(sent_doc[j].tag_=="CD" and sent_doc[j+1].pos_=="NOUN"):
                                    
                                    relevant_quantities.append(sent_doc[j].text)
                                    relevant_item.append(sent_doc[j+1].text)


                    else: # if both location and persons are not present in the query sentence
                        

                        if(query_sentence_item!=""):
                            
                            if(isWordPresent(sentences[i],query_sentence_item)):
                               
                                sent_doc=nlp(sentences[i])
                                for j in range(0,len(sent_doc)):
                                    if(sent_doc[j].tag_=="CD"):
                                        relevant_quantities.append(sent_doc[j].text)
                                        relevant_item.append(query_sentence_item)


            print('\033[1m'+"Relevant quantities: "+'\033[0m',relevant_quantities)
            
            
          
            
        if(predicted_operation=="division"):
            
            question_body_noun_phrase=[]
            noun_phrase_with_quantities=[]
            
            if(query_sentence_item!="" and query_sentence_entity_name!=""):
               
                for i in range(0,len(sentences)):
                    sent_doc=nlp(sentences[i])
                    for chunk in sent_doc.noun_chunks:
                        if chunk.text not in question_body_noun_phrase: # checking for duplicate noun phrase
                            question_body_noun_phrase.append(chunk.text)
               
                        
                for j in range(0,len(question_body_noun_phrase)):
                    per_qb_noun_phrase_doc=nlp(question_body_noun_phrase[j])
                    
                    for k in range(0,len(per_qb_noun_phrase_doc)):
                        
                        if(per_qb_noun_phrase_doc[k].tag_=="CD" and per_qb_noun_phrase_doc[k+1].pos_=="NOUN"):
                            if(per_qb_noun_phrase_doc[k+1].text==query_sentence_item or per_qb_noun_phrase_doc[k+1].lemma_==query_sentence_entity_name):
                                relevant_quantities.append(per_qb_noun_phrase_doc[k].text)
                            
                        
                        
            print('\033[1m'+"Relevant quantities: "+'\033[0m',relevant_quantities)
                   
                
        if(predicted_operation=="multiplication"):
            
            mul_quant=[]
            mul_unit=[]
            mul_singular_quant=[]
            mul_singular_unit=[]
            
            for i in range(0,len(input_question_doc)):
                
                if(input_question_doc[i].pos_=="NUM" and input_question_doc[i+1].pos_=="NOUN"):
                    
                    if(input_question_doc[i+1].tag_=="NN"):
                        mul_singular_quant.append(input_question_doc[i].text)
                        mul_singular_unit.append(input_question_doc[i+1].text)
                        
                    if(input_question_doc[i+1].tag_=="NNS"):
                        mul_quant.append(input_question_doc[i].text)
                        mul_unit.append(input_question_doc[i+1].text)
                        
            if(len(mul_singular_quant)!=0):
                relevant_quantities=mul_quant
                print('\033[1m'+"Relevant quantities: "+'\033[0m',relevant_quantities)    
            
            
            else:
                
                for i in range(0,len(sentences)): # conjunction elemination for multiplication type question.
                    sent_doc=nlp(sentences[i])
                    quant_count=0
                    conj_flag=0
                    for chunk in sent_doc:
                        if(chunk.pos_=="NUM"):
                            quant_count=quant_count+1 
                        if(chunk.dep_=="cc"):
                            conj_flag=1
                    if(quant_count>=2 and conj_flag==1):
                        sent=""
                        sent1=""
                        k=0
                        for j in range(0,len(sent_doc)):
                            if(sent_doc[j].dep_!="cc"):
                                sent=sent+" "+sent_doc[j].text
                            else:
                                k=j+1
                                break;
                                
                        sentences.remove(sentences[i])
                        sentences.insert(i,sent)
                                
                        for l in range(k,len(sent_doc)):
                            sent1=sent1+" "+sent_doc[l].text
                        sentences.insert(i+1,sent1)
                
                        
                    
                    
                for i in range(0,len(sentences)): 
                    sent_doc=nlp(sentences[i])
                    
                    
                            
                    
                    if(isWordPresent(sentences[i],query_sentence_item)):
                        for tokens in sent_doc:
                            if(tokens.pos_=="NUM"):
                                relevant_quantities.append(tokens.text)
                                
                    
            
                print('\033[1m'+"Relevant quantities: "+'\033[0m',relevant_quantities)
            
            
    # calling the function which will evaluate the final result
    
   
    return perform_operation(predicted_operation,relevant_quantities)       
                
            
                 
    
def perform_operation(predicted_operation,relevant_quantities):
    final_count=0
    if(len(relevant_quantities)==2):
        
        # converting the relevant quantities into floating point numbers
        for i in range(0,len(relevant_quantities)):
            
            relevant_quantities[i]=float(relevant_quantities[i])
        

        if(predicted_operation in('subtraction','division')): # in case of division or subtraction, order of quantities matters

            larger_number=max(relevant_quantities)
            smaller_number=min(relevant_quantities)

            if(predicted_operation=="subtraction"):
                solution=larger_number-smaller_number
                solution=round(solution,2)
                print(ans)
                if(ans==solution):
                    final_count+=1
                print('\033[1m'+"Solution: "+'\033[0m',"("+str(larger_number)+" - "+str(smaller_number)+")"+" = "+str(solution))

            else:
                solution=larger_number/smaller_number
                solution=round(solution,2)
                if(ans==solution):
                    final_count+=1
                print('\033[1m'+"Solution: "+'\033[0m',"("+str(larger_number)+" / "+str(smaller_number)+")"+" = "+str(solution))



        if(predicted_operation=="addition"):

            solution=0    
            for i in range(0,len(relevant_quantities)):
                solution=solution+relevant_quantities[i]
                solution=round(solution,2)
                if(ans==solution):
                    final_count+=1
            print('\033[1m'+"Solution: "+'\033[0m',"("+str(relevant_quantities[0])+" + "+str(relevant_quantities[len(relevant_quantities)-1])+")"+" = "+str(solution))


        if(predicted_operation=="multiplication"):

            solution=1
            for i in range(0,len(relevant_quantities)):
                solution=solution*relevant_quantities[i]
                solution=round(solution,2)
                if(ans==solution):
                    final_count+=1
            print('\033[1m'+"Solution: "+'\033[0m',"("+str(relevant_quantities[0])+" * "+str(relevant_quantities[len(relevant_quantities)-1])+")"+" = "+str(solution)) 
    return final_count


import json
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy
from sklearn import metrics
from mlxtend.evaluate import confusion_matrix

df=pd.read_json('questions.json',orient="records")
df.head(len(df))
print(len(df))
Total_count=len(df)
actual_ans=[]
predicted_ans=[]
countaa=0
countas=0
countam=0
countad=0
countsa=0
countss=0
countsm=0
countsd=0
countma=0
countms=0
countmm=0
countmd=0
countda=0
countds=0
countdm=0
countdd=0
final_count=0
for i in range(0,len(df)):
    print('\033[1m'+"Index:"+'\033[0m',df.iIndex.iloc[i])
    print('\033[1m'+"Question:"+'\033[0m',df.sQuestion.iloc[i])
    #print('\033[1m'+"Alignment:"+'\033[0m',df.lAlignments.iloc[i])
    print('\033[1m'+"Equation:"+'\033[0m',df.lEquations.iloc[i])
    ans=df.lSolutions.iloc[i]
    question_body = ""
    query_sentence = ""
    count=0
    ca=0
    cs=0
    cm=0
    cd=0
    input_question=df.sQuestion.iloc[i]
    actual_operation=-1
    act_operation=""
    for j in range(len(df.lEquations.iloc[i])):
        print(type(df.lEquations.iloc[i][j]))
        for k in range(len(df.lEquations.iloc[i][j])):
            if(df.lEquations.iloc[i][j][k]=='+'):
                actual_operation=1
                act_operation='addition'
                ca+=1
            if(df.lEquations.iloc[i][j][k]=='-'):
                actual_operation=2
                act_operation='subtraction'
                cs+=1
            if(df.lEquations.iloc[i][j][k]=='*'):
                actual_operation=3
                act_operation='multiplication'
                cm+=1
            if(df.lEquations.iloc[i][j][k]=='/'):
                actual_operation=4
                act_operation='division'
                cd+=1
            

    # Converting the input question in lower form
    actual_ans.append(actual_operation)
    question = input_question.lower()

    nlp = spacy.load('en_core_web_sm') 
    neuralcoref.add_to_pipe(nlp)

    doc = nlp(question) 

    print('\033[1m'+"Input Question: "+'\033[0m',doc.text)

    #doc1 = nlp(preprocessed_question)

    sentence_length=len(doc)
    query_sentence_pos=sentence_length

    for i in range(0,sentence_length):
        if(doc[i].tag_=="WP" or doc[i].tag_=="WRB"):
            query_sentence_pos = i
            count=count+1
            if(count==1):
                for j in range(i,sentence_length):
                    query_sentence=" ".join([query_sentence,doc[j].text])
                    query_sentence=" ".join(query_sentence.split()) 
            else:
                question_body = ""
                query_sentence = ""
                for j in range(i,sentence_length):
                    query_sentence=" ".join([query_sentence,doc[j].text])
                    query_sentence=" ".join(query_sentence.split()) 
            
    print('\033[1m'+"Problem question:"+'\033[0m',query_sentence)

    for k in range(0,query_sentence_pos):
        question_body = " ".join([question_body,doc[k].text])    
        question_body=" ".join(question_body.split())
    print('\033[1m'+"Problem body:"+'\033[0m',question_body)

    
    predicted_problem_category=problem_category_classification(question,input_question)
    print('\033[1m'+"Predicted Problem Category: "+'\033[0m',predicted_problem_category)
    
    predicted_operation=operation_prediction(question_body,query_sentence,question,input_question,predicted_problem_category)
    if(predicted_operation=='addition' and actual_operation==1 ):
        countaa+=1
    if(predicted_operation=='addition' and actual_operation==2 ):
        countas+=1
    if(predicted_operation=='addition' and actual_operation==3 ):
        countam+=1
    if(predicted_operation=='addition' and actual_operation==4 ):
        countad+=1
    if(predicted_operation=='subtraction' and actual_operation==1 ):
        countsa+=1
    if(predicted_operation=='subtraction' and actual_operation==2 ):
        countss+=1
    if(predicted_operation=='subtraction' and actual_operation==3 ):
        countsm+=1
    if(predicted_operation=='subtraction' and actual_operation==4 ):
        countsd+=1
    if(predicted_operation=="multiplication" and actual_operation==1 ):
        countma+=1
    if(predicted_operation=="multiplication" and actual_operation==2 ):
        countms+=1
    if(predicted_operation=="multiplication" and actual_operation==3 ):
        countmm+=1
    if(predicted_operation=="multiplication" and actual_operation==4 ):
        countmd+=1
    if(predicted_operation=='division' and actual_operation==1 ):
        countda+=1
    if(predicted_operation=='division' and actual_operation==2 ):
        countds+=1
    if(predicted_operation=='division' and actual_operation==3 ):
        countdm+=1
    if(predicted_operation=='division' and actual_operation==4 ):
        countdd+=1
    print('\033[1m'+"Predicted operation: "+'\033[0m',predicted_operation)
    if(predicted_operation=='division'):
        k=4
    if(predicted_operation=="multiplication"):
        k=3
    if(predicted_operation=='subtraction'):
        k=2
    if(predicted_operation=='addition' ):
        k=1
    predicted_ans.append(k)

    
    final_count+=finding_relevant_quantities(input_question,predicted_problem_category,predicted_operation)
    print('\n')
print(actual_ans)
print(Total_count)
print("Accuracy: "+str((final_count/Total_count)*100))  
cm = confusion_matrix(y_target=actual_ans, 
                      y_predicted=predicted_ans, 
                      binary=False)
cm
confusion_matrix = metrics.confusion_matrix(actual_ans, predicted_ans)
#cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix = confusion_matrix, display_labels =[1,2,3,4,5])

#cm_display.plot()
#plt.show()      
print(ca,cs,cm,cd)
print("sajdce")

print(countaa,
countas,
countam,
countad,
countsa,
countss,
countsm,
countsd,
countma,
countms,
countmm,
countmd,
countda,
countds,
countdm,
countdd,)
