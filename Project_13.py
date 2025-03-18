"""Question: This program uses a multiline string as a bitmap, 
a 2D image with only two possible colors for each pixel, 
to determine how it should display a message from the user. 
In this bitmap, space characters represent an empty space,
and all other characters are replaced by characters in the user’s message. 
The provided bitmap resembles a world map, but you can change this to any image you’d like. 
The binary simplicity of the space-or-message-characters system makes it good for beginners.
Try experimenting with different messages to see what the results look like!"""

def publish(bitmap):
    print("."*100)
    for eachline in bitmap.splitlines():
        for i,each in enumerate(eachline):
            if each ==" ":
                print(" ",end= "")
            else:
                print(msg[i%len(msg)],end="")
                
        print()
    print("."*100)


print("Bitmap Message, by Al Sweigart al@inventwithpython.com")
msg=input("Enter the message to display with the bitmap.\n > ")
if msg == "":
    exit()

bitmap1 = """ 
    **************   *  *** **  *      ******************************
   ********************* ** ** *  * ****************************** *
  **      *****************       ******************************
           *************          **  * **** ** ************** *
            *********            *******   **************** * *
             ********           ***************************  *
    *        * **** ***         *************** ******  ** *
                ****  *         ***************   *** ***  *
                  ******         *************    **   **  *
                  ********        *************    *  ** ***
                    ********         ********          * *** ****
                    *********         ******  *        **** ** * **
                    *********         ****** * *           *** *   *
                      ******          ***** **             *****   *
                      *****            **** *            ********
                     *****             ****              *********
                     ****              **                 *******   *
                     ***                                       *    *
                     **     *                    *
"""
bitmap2 ="""
                   **             **
                   ***            *** 
                   ****          ****
                   ****   **     *****
                   *******************
                  ****  ********  *****
                 ***      ***      *****
                 ****    ******   ******
                 *********   ***********
                 ****** *** ** ********
                 *******   *   *******
                 *********   *********
                 ********************

"""
bitmap3="""

"""

choose=input('which bitmap would you like to try? \noptions: \na) world map\nb) cat(hopefully) \n > ')

if choose.lower()=="a":
    publish(bitmap1)
elif choose.lower()=="b":
    publish(bitmap2)
elif choose.lower()=="c":
    publish(bitmap3)