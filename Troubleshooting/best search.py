def linear_search(list, key):
   #Returns the number of steps to determine if key is in the list


   #Initialize the counter of steps
   steps=0
   for i, item in enumerate(list):
       steps += 1
       if item == key:
           return steps
   return steps


def binary_search(list, key):
   #Returns the number of steps to determine if key is in the list


   #List must be sorted:
   list.sort()


   #The Sort was 1 step, so initialize the counter of steps to 1
   steps=1


   left = 0
   right = len(list) - 1
   while left <= right:
       steps += 1
       middle = (left + right) // 2
      
       if list[middle] == key:
           return steps
       if list[middle] > key:
           right = middle - 1
       if list[middle] < key:
           left = middle + 1
   return steps


def best_search(list, key):
   steps_linear = linear_search(list.copy(), key)
   steps_binary = binary_search(list.copy(), key)
   results = "Linear: " + str(steps_linear) + " steps, "
   results += "Binary: " + str(steps_binary) + " steps. "
   if steps_linear < steps_binary:
       results += "Best Search is Linear."
   elif steps_binary < steps_linear:
       results += "Best Search is Binary."
   else:
       results += "Result is a Tie."


   return results


print(best_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1))
#Should be: Linear: 1 steps, Binary: 4 steps. Best Search is Linear.


print(best_search([10, 2, 9, 1, 7, 5, 3, 4, 6, 8], 1))
#Should be: Linear: 4 steps, Binary: 4 steps. Result is a Tie.


print(best_search([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 7))
#Should be: Linear: 4 steps, Binary: 5 steps. Best Search is Linear.


print(best_search([1, 3, 5, 7, 9, 10, 2, 4, 6, 8], 10))
#Should be: Linear: 6 steps, Binary: 5 steps. Best Search is Binary.


print(best_search([5, 1, 8, 2, 4, 10, 7, 6, 3, 9], 11))
#Should be: Linear: 10 steps, Binary: 5 steps. Best Search is Binary.