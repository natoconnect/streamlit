#!/usr/bin/env python
# coding: utf-8

# ### Mortgage Calculator  
# Calculate the monthly payments of a fixed term mortgage over given Nth terms at a given interest rate. Also figure out how long it will take the user to pay back the loan. For added complexity, add an option for users to select the compounding interval (Monthly, Weekly, Daily, Continually).

# ## Functions  
# ___  
# >**- npv  (rate, values)**  *Returns the NPV (Net Present Value) of a cash flow series.*  
# **- pmt  (rate, nper, pv[, fv, when])**  *Compute the payment against loan principal plus interest.*  
# **- ppmt (rate, per, nper, pv[, fv, when])** *Compute the payment against loan principal.*  
# **- pv   (rate, nper, pmt[, fv, when])** *Compute the present value.*  
# **- rate (nper, pmt, pv, fv[, when, guess, tol, …])**  *Compute the rate of interest per period
# 
# https://numpy.org/numpy-financial/latest/

# In[ ]:


from IPython.display import clear_output
from IPython.display import display
import numpy as np
import numpy_financial as npf
import ipywidgets as widgets
import time as time
from jupyter_ui_poll import ui_events


# In[ ]:


def apr_float():
    
    while True:
        try:
            apr = float(input("Enter an interest rate (numbers ony): "))
            if apr == type(float):
                raise ValueError
#                 print(apr)
            return apr
            break
        except ValueError:
            print("Numbers only, please.")  


# In[ ]:


def years_int():
    while True:
        try:
            years = int(input("Enter length of loan (in years <= 50): "))
            if years == type(int) or years > 50:
                raise ValueError
            return years
            break
        except ValueError:
            print("Whole numbers only and less than",years, "please.")  


# In[ ]:


def loan_int():
    while True:
        try:
            ask = int(input("Enter loan amount (whole numbers ony): "))
            if ask == type(int):
                raise ValueError
            return ask
            break
        except ValueError:
            print("Whole numbers only, please.")  


# In[ ]:


# ROUGH DRAFT
# select_terms(apr,ask,1,years)
def select_terms(rate, loan_amt, interval, years):    
#     import numpy as np
#     import numpy_financial as npf
    
    periods = 0
    apr_percent = rate/100    

 # Derive the equivalent periodic mortgage rate from the annual rate
    apr = rate/100    
    if interval == 1:        
        periods = 12*years
        period = 'Monthly'
        ppr = 12
        
    elif interval == 2:
        periods = 52*years
        period = 'Weekly'
        ppr = 52

    elif interval == 3:
        periods = 365*years
        period = 'Daily'
        ppr = 365

    else:
        interval == 4
        periods = 365*24*years
        period = 'Constant'
        ppr = 365*24

    ppr = rate/100/ppr
    clear_output()
    print('Loan Amount: $',f"{loan_amt:.2f}",' APR:',f"{rate}%")
    print(period,'Percentage Rate of',f"{ppr:.4%}")

    periodic_mortgage_payment = -1*npf.pmt(ppr,periods,loan_amt)
    periodic_mortgage_payment = periodic_mortgage_payment

    print(f"{period} Mortgage Payment: $" + str(round(periodic_mortgage_payment, 2)))


# In[ ]:


# from IPython.display import display
# import ipywidgets as widgets
# from jupyter_ui_poll import ui_events
# import time as time

ask = loan_int()
apr = apr_float()
years = years_int()
# print(ask,apr,years)

# Create the widget
widget = widgets.Dropdown(
    options=[('Monthly', 1), ('Weekly', 2), ('Daily', 3),('Constant', 4)],
    description='Period:',disabled=False)

# Create a function to continue the execution
button_clicked = False
def on_click(b):
    global button_clicked
    button_clicked = True

# Create a button widget
button = widgets.Button(description="Calculate")
button.on_click(on_click)

# Display the widget and button
display(widget, button)

# Wait for user to press the button
with ui_events() as poll:
    while button_clicked is False:
        poll(10)          # React to UI events (upto 10 at a time)
        time.sleep(0.1)


global prd 
prd = 1
# Get the selected value from the widget
prd = widget.value
# print("Selected value:", prd)
select_terms(apr,ask,prd,years)

