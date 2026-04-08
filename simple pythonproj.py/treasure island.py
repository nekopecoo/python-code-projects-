print('''
        ,~~;,~~.~~,
       (`'` ` `    `,
        ~~``` ` `   ;
        |@ , @ | , ';
        ' (    ' `  ;
        `._o__/^;' ';
        ;..'  ';.` ;        .
        '   * _ ;.;)_____  .  _-
        \____/ ) )_____  )� _-    __--
        \_____/ |-_  -_:-._-  __-- ___
         |______|  --_/:::\_--  _--
        /     , \---=|:::::|=----------
       |   ,     \ __-\:::/-__  -__
      /   ;       |  _- | -_sd--__ ---
     |         ,  |_- . | . -_    --__
    /         ;   |  �  |  �  -_
   |  ,      ;    | �   |   �   -
  /  ;            |
 |__'___^^_______^^
        ~~       ^^

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction=input("would like to go left or right").lower()
if direction=="right":
    print("wow! you have reached a lake")
    # level two
    swim_or_wait=input("would you like to swim or wait for the boat").lower()
    if swim_or_wait=="swim":
        print("you were pulled by mermaid to a mysterious underwater!")
        print("mermaid offers two pearls!but you can only choose one. choose wisely.")
        pearl=input("choose a pearl pink or blue").lower()
        if pearl=="blue":
           print("you got ability to breath underwater!")
           print("you reached a palace with three doors. choose wisely")
           door=input("which door would you like to choose red,black,white").lower()
           if door=="black":
              print("YOU FOUND THE TREASURE!!!")
              print("BUT, you need to carry it out of the sea .")
              hellp=input("would you like to ask mermaids for help.Y or N").lower()
              if hellp=="y":
                  print("you reached the land with treasure!!")
              else:
                  print("you failed ! GAME OVER")
           elif door=="red":
                 print("a beast ate you! GAME OVER")
           else:
                   print("you were dragged to the land!GAME OVER")
        else:
             print("you ran out of air!GAME OVER")
    else:
     print("your boat exploded!GAME OVER")
else:
    print("you  fell into a pit!GAME OVER")