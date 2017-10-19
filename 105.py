#coding: utf-8

# Created by: Anthony Freeman
# Created on: September 2017
# Created for: ICS3U

import ui

def calculate_button_touch_up_inside(sender):

    PI = 3.14
    LABOUR_COST = 0.75
    RENT_COST = 1.00
    MATERIAL_COST = 0.50
    HST = 0.13
    
    diameter = float(view['diameter_textbox'].text)
    
    sub_total = LABOUR_COST + RENT_COST + (MATERIAL_COST * diameter) 
    cost = sub_total + (sub_total * HST)
    
    view['answer_label'].text = 'The cost is: ' + '${:,.2f}'.format(cost)

view = ui.load_view()
view.present('full_screen')
