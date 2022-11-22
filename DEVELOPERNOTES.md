# Developer notes:
## Thoughts while writing code
1. Generating alphanumeric unique id with the length 7 (Upper case alphabets + Digits (0 to 9))

    Approach : 
   1. Used **uuid** library and did some work out. It gives the 128 bit long value but still tried to limiting it to alphanumeric and to the required length using hashing algorithm (Felt i am complicating this and time consuming but i believe it is not impossible)
   2. First used **random.choice** method and the used **secrets** library
   3. **secrets** module is used for generating cryptographically strong random numbers
   4. Tested manually the risk of getting duplicates using 'measure_the_risk_in_getting_duplicate' for 100 million ids 
   5. Added class template for generation module
   6. Used while loop and recursion to restart the method if it crashes (Here there is some room for improvement - Using while loop and recursive methods is dangerous)


2. Verified and added the unit tests
    1. Fixed constant modul bug (ID_CHARACTERS missing alphabets)
    2. Added unit test to validate the constant module variable values 
       (Failt tolerant - The unique id generator fails if the contant module variables gets changed. so i created unit test to make sure the values are not changed)
    3. Used fixture for the reusable (setUp) statements
    4. Added unit test to test bulk generation of unique ids
    5. Added unit test to check the multi processing 
    6. Added unit test to check the performance of the methods
   

   
