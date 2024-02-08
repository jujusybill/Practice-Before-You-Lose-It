
#Program to practice Python skills - making a random 10-char password generator


def main():
    import random
    

    #Lists of full set of data to integrate into password couplets
    full = ['a','b','c','d','e','f','g','h',
            'i','j','k','l','m','n','o','p','q',
            'r','s','t','u','v','w','x','y','z',
            'A','B','C','D','E','F','G','H','I','J',
            'K','L','M','N','O','P','Q','R','S','T',
            'U','V','W','X','Y','Z','!','@','#','$',
            '%','&','1','2','3','4','5','6','7','8','9','0']
 
    
    #This will be a program to generate passwords
    selected_item = []
    for i in range(10):
        item = random.choice(full)
        selected_item.append(item)

    #Converts list to string
    def list_to_string(s):
        str1 = ''
        for i in s:
            str1 += i
        return str1

    print("Here is your new password:", list_to_string(selected_item))
    
    
if __name__=='__main__':
    main()
    
