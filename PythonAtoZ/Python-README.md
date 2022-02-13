# Taking User Input ()
. Though you ll be requried to explicitly cast it to your desired datatype thereafter.

#Taking input from User.
input()


#String Interpolation
uses 'f' unlike Scala which uses 's'. 

eg:
f"hello {name}"
s"hello ${name}"

# Using Lambda
Lambda methods are basically function which dont have any names. General syntax of such functions goes as follow
lambda {function params} : {Operation}
Though u can assign this function to variable and use that variable to call the method
but why to do so much locha.

Ideally Lambdas are useful when we have maps envolved.
Map is basically similar to map what we had in scala apart from its syntax:
Syntax:
Map(function here , collection on which the function needs to be applied.)

Similar kind of approach can be executed with below syntax as well which is briefly known as 
#list Comprehensions
x*2 for x in collection on which this process needs to be applied.

#Magic Methods
* __init__  ----> Constructor
*__str__   ------> Get String representation of your object 
* __repr__  ------> Statement to create object of that class in which you are present at that time.

#args and kwargs
* args are basically a placehf older which can expect n no. of arguments without we giving them explicit names or something like that.
for eg:
mul(*args) -> for i in args print(i*2)

* *agrs will always pass-on touple 
* **kwargs will always pass-on dictionary

#OOP

* Instance Method (Need No decorators) Takes self as a parameter
* Class Method (@classmethod Decorator required) Takes CLS as a parameter -->
  Does not needs any instance of class thats why its named as class method.
  Used when we want to do something with some properties of class which are not specific to a Instance specifically. kind of we can say when we want to bound
  child class to be created under some specific categrories only then we can use such methods with such categories envolved and create a object wiith specified category of which method is called.
  * eg:
    when we have books class and we want to restrict the books to be made of only 2 categories -> 1. HardCover and 2. SoftCover
    then we can create 2 class methods deriving the same and we can just call that specific class method of hardcover or softcover accordingly and get this done.
    this way we dont need to handle 2 diff cases of if the category is not present in allowed category then gently trying to exit the program with a given exception.
    
    
  
* static Method (@staticmethod Decorator required) Takes No parameters.
  Does not needs any instance of class and it doesnot takes any parameter.
* Magic Methods


# Type Hinting:
When ever we have a requirement where we want to send a warning when lets say a function is expecting a integer datatype param but at the runtime if we dont use type hinting and if user
passes strign in place of int he wont be presented with any warning but your program will fail.
To handle such issues what we can do is we can import typing package and we can import what ever the type of data we will be expecting in function definition and then run program accordingly.


#Decorators
where we want to some set of actions to be executed before our original function executes.
Syntax: original function -> 
def display():
  println("I am original")
def decorated_display():
  def wrapper(*args,**kwargs):
    Do your stuff of validations here.
    return originalfunction(*args,**kwargs) // Running original function here.

For eg :
Auth Level verification everytime when i API is triggered. Whether the current user is allowed to do so or not or some other checks on the request.
Db session creation wrapper before everytime committing a transaction in DB


#Try-Except-Else-Finally
Try -> Sensitive code snippet
Except -> If met an exception then execute this.
Else -> If didnt meet any exception then execute this.
Finally -> Irrespective of exception execute this at the end.
