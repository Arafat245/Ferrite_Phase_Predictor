
import numpy as np
import pandas as pd
import ipywidgets as widgets
from IPython.display import display


def take_input():
    # Create widgets for each variable
    alloy_name = widgets.Text(description="Alloy Name:",placeholder="Enter Alloy Name here")
    ni_widget = widgets.FloatText(description="Ni", step=0.1)
    c_widget = widgets.FloatText(description="C", step=0.1)
    n_widget = widgets.FloatText(description="N:", step=0.1)
    mn_widget = widgets.FloatText(description="Mn:", step=0.1)
    cr_widget = widgets.FloatText(description="Cr:", step=0.1)
    si_widget = widgets.FloatText(description="Si:", step=0.1)
    mo_widget = widgets.FloatText(description="Mo:", step=0.1)
    cu_widget = widgets.FloatText(description="Cu:", step=0.1)
    nb_widget = widgets.FloatText(description="Nb:", step=0.1)

    # Submit button
    submit_button = widgets.Button(description="Submit")

    # Output widget
    output = widgets.Output()

    # Container to store the values
    stored_values = {}

    # Define the button click event
    def submit_values(b):
        with output:
            output.clear_output()
            try:
                stored_values.update({
                    "Ni": ni_widget.value,
                    "C": c_widget.value,
                    "N": n_widget.value,
                    "Mn": mn_widget.value,
                    "Cr": cr_widget.value,
                    "Si": si_widget.value,
                    "Mo": mo_widget.value,
                    "Cu": cu_widget.value,
                    "Nb": nb_widget.value
                })
                print(f"Values Entered:")
                for key, value in stored_values.items():
                    print(f"{key}: {value}")
            except ValueError:
                print("Please enter valid numeric values for all fields.")       

    # Attach the event to the button
    submit_button.on_click(submit_values)

    # Display the widgets and button
    display(alloy_name, ni_widget, c_widget, n_widget, mn_widget, cr_widget, si_widget, mo_widget, cu_widget, nb_widget, submit_button, output)

    return stored_values

def sc_calc(C, N, Mn, Ni, Cr, Mo, Si, Cu, Nb):
    
    
    Nieq = Ni + 30*C + 0.5*Mn
    Creq = Cr + Mo + 1.5*Si

    # print(f'According to Schaffler Nieq: {Nieq}')
    # print(f'According to Schaffler Creq: {Creq}')
    
    def ferrite_sc(Nieq, Creq, a, b):
        return a*((Nieq+2) / (Creq-5.4)) + b

    data_sc = {
    "a": [-55.6, -41.7, -64.5, -190.5, -296.3, -121.2],
    "b": [60.6, 46.7, 66.8, 158.1, 223.7, 138.8],
    "FE (vol%) min": [0, 5, 10, 20, 40, 80],
    "FE (vol%) max": [5, 10, 20, 40, 80, 100]
    }

    abdata_sc = pd.DataFrame(data_sc)
    
    for index, row in abdata_sc.iterrows():
        fe_sc = ferrite_sc(Nieq, Creq, row['a'], row['b'])
        fe_sc = int(fe_sc)

        if row['FE (vol%) min'] <= fe_sc and fe_sc <= row['FE (vol%) max']:
            return fe_sc
    return 0
    
    
    
