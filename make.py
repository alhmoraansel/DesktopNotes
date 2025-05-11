import tkinter as tk
from tkinter import ttk,font,colorchooser,filedialog
import os,configparser
LAST_FILE_PATH_FILE="last_rainmeter_note_file.txt"
def save_last_file_path(file_path):
 try:open(LAST_FILE_PATH_FILE,"w",encoding="utf-8").write(file_path)
 except:pass
def load_last_file_path():
 if os.path.exists(LAST_FILE_PATH_FILE):
  try:
   file_path=open(LAST_FILE_PATH_FILE,"r",encoding="utf-8").read().strip()
   return file_path if os.path.exists(file_path) else(os.remove(LAST_FILE_PATH_FILE),None)[0]
  except:return None
 return None
def create_rainmeter_note_gui():
 def export_ini():
  raw_note_text=note_text_entry.get("1.0",tk.END).strip();note_text=raw_note_text.replace('\n',' ')
  note_title=title_entry.get().strip();font_face=font_combobox.get()
  try:font_size=int(size_entry.get())
  except:return
  font_color=color_button.cget("background");aa_value=aa_var.get()
  r,g,b=root.winfo_rgb(font_color);a=255;font_color_str=f"{r//256},{g//256},{b//256},{a}"
  title_font_size_calculated=int(font_size*1.5);approx_title_height=title_font_size_calculated
  line_height=2;title_padding=5;line_text_padding=3;initial_offset=5
  line_y=initial_offset+approx_title_height*1.5+title_padding;text_y=line_y+line_height+line_text_padding
  ini_content=f"""[Rainmeter]
Update=1000000
AccurateText=1
DynamicWindowSize=1

[Variables]
FontFace={font_face}
FontSize={font_size}
FontColor={font_color_str}
AntiAlias={aa_value}
TitleText="{note_title}"
NoteText="{note_text}"
LineWidth={line_height}
LineLength=300
TitlePadding={title_padding}
LineTextPadding={line_text_padding}
InitialOffset={initial_offset}

[NoteTitle]
Meter=String
FontFace=#FontFace#
FontSize={title_font_size_calculated}
FontColor=#FontColor#
AntiAlias=#AntiAlias#
Text=#TitleText#
Y=#InitialOffset#
X=0

[LineSeparator]
Meter=Image
Y={line_y}
X=0
W=#LineLength#
H=#LineWidth#
SolidColor=#FontColor#

[NoteText]
Meter=String
FontFace=#FontFace#
FontSize=#FontSize#
FontColor=#FontColor#
AntiAlias=#AntiAlias#
Y={line_y+20}
X=20
W=245
H=180
Clipstring=1
Text=#NoteText#
"""
  file_path=filedialog.asksaveasfilename(defaultextension=".ini",initialfile=f"{note_title}.ini",title="Save Rainmeter INI File",filetypes=[("Rainmeter INI Files","*.ini"),("All Files","*.*")])
  if file_path:
   try:open(file_path,"w",encoding="utf-8").write(ini_content);save_last_file_path(file_path)
   except:pass
 def choose_color():
  color_code=colorchooser.askcolor(title="Choose Font Color")[0]
  if color_code:color_button.config(background='#%02x%02x%02x'%(int(color_code[0]),int(color_code[1]),int(color_code[2])))
 def load_ini(file_path=None):
  if file_path is None:file_path=filedialog.askopenfilename(title="Load Rainmeter INI File",filetypes=[("Rainmeter INI Files","*.ini"),("All Files","*.*")])
  if not file_path:return
  config=configparser.ConfigParser()
  try:
   config.read(file_path,encoding='utf-8')
   if'Variables'not in config:return
   variables=config['Variables']
   note_title=variables.get('TitleText','');note_text=variables.get('NoteText','');font_face=variables.get('FontFace','Consolas')
   font_size_str=variables.get('FontSize','12');font_color_str=variables.get('FontColor','255,255,255,255');aa_value_str=variables.get('AntiAlias','1')
   title_entry.delete(0,tk.END);title_entry.insert(0,note_title)
   note_text_entry.delete("1.0",tk.END);note_text_entry.insert("1.0",note_text)
   if font_face in available_fonts:font_combobox.set(font_face)
   size_entry.delete(0,tk.END)
   try:size_entry.insert(0,str(int(font_size_str)))
   except:size_entry.insert(0,'14')
   try:r,g,b,a=map(int,font_color_str.split(','));color_button.config(background='#%02x%02x%02x'%(r,g,b))
   except:pass
   try:aa_var.set(int(aa_value_str))
   except:pass
  except:pass
 root=tk.Tk();root.title("Rainmeter Note Generator");root.geometry("500x650")
 style=ttk.Style()
 congenial_font=font.Font(family="Segoe UI",size=10)
 style.configure("TLabel",font=congenial_font);style.configure("TEntry",font=congenial_font)
 style.configure("TCombobox",font=congenial_font);style.configure("TCheckbutton",font=congenial_font)
 style.configure("TButton",font=congenial_font,padding=10)
 tk_button_font=font.Font(family="Segoe UI",size=10)
 title_label=ttk.Label(root,text="Note Title:");title_label.pack(pady=(10,0),padx=10,anchor=tk.W)
 title_entry=ttk.Entry(root,width=60);title_entry.pack(pady=(0,10),padx=10,anchor=tk.W,fill=tk.X)
 note_text_label=ttk.Label(root,text="Note Text:");note_text_label.pack(pady=(10,0),padx=10,anchor=tk.W)
 note_text_entry=tk.Text(root,width=60,height=10,font=tk_button_font);note_text_entry.pack(pady=(0,10),padx=10,anchor=tk.W,fill=tk.BOTH,expand=True)
 font_label=ttk.Label(root,text="Font:");font_label.pack(pady=(10,0),padx=10,anchor=tk.W)
 available_fonts=sorted(font.families());font_combobox=ttk.Combobox(root,values=available_fonts,width=60);font_combobox.set("Consolas");font_combobox.pack(pady=(0,10),padx=10,anchor=tk.W,fill=tk.X)
 size_label=ttk.Label(root,text="Font Size:");size_label.pack(pady=(10,0),padx=10,anchor=tk.W)
 size_entry=ttk.Entry(root,width=60);size_entry.insert(0,'14');size_entry.pack(pady=(0,10),padx=10,anchor=tk.W,fill=tk.X)
 color_label=ttk.Label(root,text="Font Color:");color_label.pack(pady=(10,0),padx=10,anchor=tk.W)
 color_button=tk.Button(root,text="Choose Color",command=choose_color,bg="white",width=20,font=tk_button_font);color_button.pack(pady=(0,10),padx=10,anchor=tk.W)
 aa_label=ttk.Label(root,text="Anti-Aliasing:");aa_label.pack(pady=(10,0),padx=10,anchor=tk.W)
 aa_var=tk.IntVar();aa_check=ttk.Checkbutton(root,text="Enable Anti-Aliasing",variable=aa_var);aa_var.set(1);aa_check.pack(pady=(0,10),padx=10,anchor=tk.W)
 button_frame=ttk.Frame(root);button_frame.pack(pady=20,padx=10,fill=tk.X)
 load_button=ttk.Button(button_frame,text="Load from INI",command=load_ini);load_button.pack(side=tk.LEFT,padx=(0,5),fill=tk.X,expand=True)
 export_button=ttk.Button(button_frame,text="Export to INI",command=export_ini);export_button.pack(side=tk.LEFT,padx=(5,0),fill=tk.X,expand=True)
 last_file=load_last_file_path();last_file and load_ini(last_file)
 root.mainloop()
if __name__=="__main__":create_rainmeter_note_gui()
