def string_splosion(s):
   '''
   Creates a string splosion of s
   '''
   result = ""
   for i in range(0, len(s) + 1):
      result += s[:i]
   return result
    
