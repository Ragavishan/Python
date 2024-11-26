def calculator(operation,num1,num2):
  switcher={
          'add':num1+num2,
          'subtract':num1*num2,
          'multiply':num1*num2,
          'devide':num1/num2
          if num2!=0
          else
          'Error:Devision by Zero'
          }
  return switcher.get(operation,'invalid operation')
print(calculator('add',10,5))
print(calculator('subtract',10,5))
print(calculator('multiply',10,5))
print(calculator('devide',10,5))
print(calculator('devide',10,0))
print(calculator('mod',10,5))                                                                              
  

