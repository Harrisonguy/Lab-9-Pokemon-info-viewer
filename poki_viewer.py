from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_poke

# Create the window
root = Tk()
root.title("Pokemon Info Viewer")
root.resizable(False, False)

# Add frames to window
frm_top = ttk.Frame(root)
frm_top.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

frm_btm_left = ttk.LabelFrame(root, text='Info')
frm_btm_left.grid(row=1, column=0, sticky=N, padx=(10,0)) 

frm_btm_right = ttk.LabelFrame(root, text='Stats')
frm_btm_right.grid(row=1, column=1, sticky=N, padx=10, pady=(0, 10)) 

# Add widget to window
lbl_name = ttk.Label(frm_top, text='Pokemon Name:')
lbl_name.grid(row=0, column=0)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0, column=1, padx=10)

def handle_get_info_btn_click():
    # Get the name of the Pokemon
    poke_name = ent_name.get().strip()
    if poke_name == '':
        return
    
    # Get pokemone in from the api
    poke_info = get_poke(poke_name)
    if poke_info is None:
        err_msg = f'Inable to get information from pokeAPI for {poke_name}.'
        messagebox.showinfo(title='Error', message=err_msg, icon='error')
        return
    
    if len(poke_info['types']) == 2:
        types = poke_info['types'][0]['type']['name'] + ', ' + poke_info['types'][1]['type']['name']
    else:
        types = poke_info['types'][0]['type']['name']
    types = types.title()
    height = poke_info['height'] / 10
    weight = poke_info['weight'] / 10
    
    # Populate the info values
    lbl_height_value['text'] = f"{height} m"
    lbl_weight_value['text'] = f"{weight} kg"
    lbl_type_value['text'] = f"{types}" 


    # Populate the stat values
    prg_hp['value'] = poke_info['stats'][0]['base_stat']
    prg_att['value'] = poke_info['stats'][1]['base_stat']
    prg_def['value'] = poke_info['stats'][2]['base_stat']
    prg_satt['value'] = poke_info['stats'][3]['base_stat']
    prg_sdef['value'] = poke_info['stats'][4]['base_stat']
    prg_spd['value'] = poke_info['stats'][5]['base_stat']
    return

# Make button
btn_get_info = ttk.Button(frm_top, text='Get Info', command=handle_get_info_btn_click)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)

# Add widgets to bottom left frame
lbl_height = ttk.Label(frm_btm_left, text='Height:')
lbl_height.grid(row=0, column=0, padx=5, pady=(0,5))
lbl_height_value = ttk.Label(frm_btm_left)
lbl_height_value.grid(row=0, column=1, padx=5, pady=(0,5))

lbl_weight = ttk.Label(frm_btm_left, text='Weight:')
lbl_weight.grid(row=1, column=0, padx=5, pady=(0,5))
lbl_weight_value = ttk.Label(frm_btm_left)
lbl_weight_value.grid(row=1, column=1, padx=5, pady=(0,5))

lbl_type = ttk.Label(frm_btm_left, text='Type:')
lbl_type.grid(row=2, column=0, padx=5, pady=(0,5))
lbl_type_value = ttk.Label(frm_btm_left)
lbl_type_value.grid(row=2, column=1, padx=5, pady=(0,5))



#Add widgets to bottom right frame
lbl_hp = ttk.Label(frm_btm_right, text='HP:')
lbl_hp.grid(row=0, column=0, sticky=E, padx=7, pady=7)
prg_hp =ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_hp.grid(row=0, column=1, padx=(0,5))

lbl_att = ttk.Label(frm_btm_right, text='Attack:')
lbl_att.grid(row=1, column=0, sticky=E)
prg_att =ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_att.grid(row=1, column=1, padx=(0,5), pady=5)

lbl_def = ttk.Label(frm_btm_right, text='Defence:')
lbl_def.grid(row=2, column=0, sticky=E)
prg_def =ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_def.grid(row=2, column=1, padx=(0,5), pady=5)

lbl_satt = ttk.Label(frm_btm_right, text='Special Attack:')
lbl_satt.grid(row=3, column=0, sticky=E)
prg_satt =ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_satt.grid(row=3, column=1, padx=(0,5), pady=5)

lbl_sdef = ttk.Label(frm_btm_right, text='Special Defence:')
lbl_sdef.grid(row=4, column=0, sticky=E)
prg_sdef =ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_sdef.grid(row=4, column=1, padx=(0,5), pady=5)

lbl_spd = ttk.Label(frm_btm_right, text='Speed:')
lbl_spd.grid(row=5, column=0, sticky=E)
prg_spd =ttk.Progressbar(frm_btm_right, orient=HORIZONTAL, length=200, maximum=255)
prg_spd.grid(row=5, column=1, padx=(0,5), pady=5)






# Loop until window is closed

root.mainloop()