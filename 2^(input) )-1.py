'''****** ห้ามใช้ For , While  ( ให้ฝึกเอาไว้ เนื่องจากถ้าเจอตอนสอบจะได้ 0 )
เขียน Recursive เพื่อหาว่าเลขตั้งแต่ 0 จนถึง ( 2^(input) ) - 1 นั้นมีตัวอะไรบ้าง  หากเป็นเลขติดลบให้แสดงผลเป็น Only Positive & Zero Number ! ! ! 
*** ตัวอย่างเช่น ถ้าหาก input = 2 ก็ต้องแสดงผลลัพธ์เป็น 00 , 01 , 10 , 11'''
def binNum(i,num,n):
    if i==n+1:
        return
    else:
        print(f'{i:0{num}b}')
        return binNum(i+1,num,n)

num = int(input('Enter number:'))
if num < 0:
    print("Only Positive & Zero Number ! ! !")
else:
    n = 2**num-1
    binNum(0,num,n)