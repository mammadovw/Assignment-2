#import libraries here

def main():
  x = input('Enter a letter of the alphabet: ' )
  if x=='y':
    print('Sometimes it is a vowel, and sometimes it is a consonant!')
  else :    
    for i in 'aeiou' :
        if x==i :
            print('Entered alphabet is a vowel!')
            break
    for i in 'qwrtpsdfghjklzxcvbnm':
            if x==i:
                print('Entered alphabet is a consonant!')
                break
  pass

if __name__ == "__main__":
  main()
