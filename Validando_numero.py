import re

def validate_numero_telefone(phone_number):
   
   pattern = r"\(\d{2}\)\s[9]\d{4}\-\d{4}"

   if re.match(pattern, phone_number):
         return "Número de telefone válido."
   
   return "Número de telefone inválido."
    
phone_number = input()  

result = (validate_numero_telefone(phone_number))

print(result)