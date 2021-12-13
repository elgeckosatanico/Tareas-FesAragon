
def MultArr(lista):
    mult=1
    for i in lista:
        mult=mult*i
    return mult

def main():
    print(MultArr([1,2,3,4]))#24
    print(MultArr([1,2,3]))#6
    print(MultArr([1]))#1
    
    
if __name__=='__main__':
    main()
        


