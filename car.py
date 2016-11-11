class Car(object):
 """
 Attributes:
 car_type:The type of the car as a string
 car_model:The model of the car as a string
 car_name: The name of the car as a string
 """
  def __init__(self, car_type = None , car_model = None, car_name =None ):
    self.car_type = car_type
    
    if car_model is None:
      self.car_model = "GM"
    else:  
      self.car_model = car_model
    if car_name is None :
      self.car_name = "General"
    else:
      self.car_name = car_name
    
  def set_car_type(self, car_type):
    self.car_type = car_type
    
  def set_car_model(self, car_model):
    self.car_model = car_model
    
  def set_car_name(self, car_name):
    self.car_name = car_name
    
  """ 
  this method returns the number of doors 
  for porsche and koenigsegg it will return 4
  else 
  """  

   def car_doors(self):
     if self.car_type != "porshe" or "Koenigsegg":
       return 4
     return 2
     
  """this method retuns the number of wheels of the given
  type 
  if the type is a trailler it will return 8 else it will return 4
 """   
   def num_of_wheels(self):
     if self.car_type != "trailer":
       return 4
     return 8
  """
  this method tests whether the object passed to it is of type car
  """   
  def drive_car(self, car_object):
    if isinstance(car_object, Car):
      return car_object
    return "The car drive function should return the instance of the Car class"  