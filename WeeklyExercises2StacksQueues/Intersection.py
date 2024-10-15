def Intersection (Set_List_A, Set_List_B):

  Intersecting_Set_C = []
  
  for x in Set_List_A:
      
      for y in Set_List_B:
          
          if (x == y):
              
              Intersecting_Set_C.append(x)
  
  return Intersecting_Set_C