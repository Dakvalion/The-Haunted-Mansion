init python:
    numbl = 0
    numbc = 0
    numbr = 0
    
screen safe_code:
    modal True
    add "images/bg code start.png"
    add "images/cl_panel.png" align .5, .5 zoom 1.4
    
    imagebutton auto "images/up_%s.png" focus_mask True xalign .397 yalign .375 action If(numbl < 9, SetVariable("numbl", numbl + 1), SetVariable("numbl", 0))
    add "images/cl_%s.png"%(numbl) xalign .39 yalign .47 zoom 0.9
    imagebutton auto "images/dwn_%s.png" focus_mask True xalign .397 yalign .58 action If(numbl > 0, SetVariable("numbl", numbl - 1), SetVariable("numbl", 9))
    
    imagebutton auto "images/up_%s.png" focus_mask True xalign .454 yalign .375 action If(numbc < 9, SetVariable("numbc", numbc + 1), SetVariable("numbc", 0))
    add "images/cl_%s.png"%(numbc) xalign .45 yalign .47 zoom 0.9
    imagebutton auto "images/dwn_%s.png" focus_mask True xalign .454 yalign .58 action If(numbc > 0, SetVariable("numbc", numbc - 1), SetVariable("numbc", 9))
    
    imagebutton auto "images/up_%s.png" focus_mask True xalign .510 yalign .375 action If(numbr < 9, SetVariable("numbr", numbr + 1), SetVariable("numbr", 0))
    add "images/cl_%s.png"%(numbr) xalign .51 yalign .47 zoom 0.9
    imagebutton auto "images/dwn_%s.png" focus_mask True xalign .510 yalign .58 action If(numbr > 0, SetVariable("numbr", numbr - 1), SetVariable("numbr", 9))
    
    textbutton "ENTER" xalign .590 yalign .59 action If(numbl == 9, If(numbc == 6, If(numbr == 5, Hide("safe_code"), Show("access_denied")), Show("access_denied")), Show("access_denied"))

screen access_denied:
    modal True
    text "Wrong Password!!!" size 50 xalign 0.5 yalign 0.1
    textbutton "Try Again" xalign 0.5 yalign 0.2 action Hide("access_denied")

