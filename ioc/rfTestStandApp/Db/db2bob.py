#!/usr/bin/env python3

import sys

# Path to your .db file
file_path = sys.argv[1]

f = open(file_path, "r")

inside_record = False
record_name = ""
record_type = ""
desc = ""
egu = ""
record_count = 0
INP = "bbb"
OUT = "aaa"

bob_title = file_path.split("/")[len(file_path.split("/")) - 1].replace(".db", "")

bob_header = f"""<?xml version="1.0" encoding="UTF-8"?>
<display version="2.0.0">
  <name>{bob_title}</name>
  <class>DEFAULT1</class>
  <x>55</x>
  <width>920</width>
  <height>1000</height>
  <background_color>
    <color red="204" green="204" blue="204">
    </color>
  </background_color>
  <grid_visible>false</grid_visible>
  <grid_color>
    <color name="Header_Background" red="77" green="77" blue="77">
    </color>
  </grid_color>
  <grid_step_x>15</grid_step_x>
  <grid_step_y>15</grid_step_y>
"""

bob_tail = """
</display>
"""

def parse_line(line):
    global inside_record, record_name, record_type, desc, egu, field_name, INP, OUT
    line = line.strip()
    if line.startswith("#"):
        pass
    elif line.startswith("record"):
        inside_record = True
        record_type = line.split(",")[0].replace("record", "").replace(")", "").replace("(","").strip()
        start = line.split(",")[1].find('"') + 1
        end = line.split(",")[1].rfind('"')
        if start > 0 and end > start:
            record_name = line.split(",")[1][start:end]
        else:
            # todo: throw
            pass
    elif line.startswith("field"):
        field_name = line.split("field")[1].split(",")[0].replace("(", "")
        start = line.split(",", 1)[1].find('"') + 1
        end = line.split(",", 1)[1].rfind('"')
        if start > 0 and end > start:
            field_value = line.split(",")[1][start:end]
        else:
            # todo: throw
            pass

        if field_name == "DESC":
            desc = field_value
        elif field_name == "EGU":
            egu = field_value
        elif field_name == "INP":
            INP = field_value
        elif field_name == "OUT":
            OUT = field_value
    else:
        pass

def generate_widget_row(index):
    global inside_record, record_name, record_type, desc, egu, field_name, record_count, INP, OUT
    widget_row_left = 10
    widget_row_top = 25 * record_count
    return f"""
  <widget type="label" version="2.0.0">
    <name>Label_2</name>
    <text>{index}</text>
    <x>{widget_row_left}</x>
    <y>{widget_row_top}</y>
    <width>60</width>
    <height>20</height>
    <vertical_alignment>1</vertical_alignment>
  </widget>
  <widget type="label" version="2.0.0">
    <name>Label_2</name>
    <text>{record_type}</text>
    <x>{widget_row_left + 40}</x>
    <y>{widget_row_top}</y>
    <width>60</width>
    <height>20</height>
    <vertical_alignment>1</vertical_alignment>
  </widget>
  <widget type="label" version="2.0.0">
    <name>Label</name>
    <text>{record_name}</text>
    <x>{widget_row_left + 85}</x>
    <y>{widget_row_top}</y>
    <width>300</width>
    <height>20</height>
    <vertical_alignment>1</vertical_alignment>
    <wrap_words>false</wrap_words>
  </widget>
  <widget type="textupdate" version="2.0.0">
    <name>Text Update</name>
    <pv_name>{record_name + ".RVAL" if record_type == "bi" else record_name}</pv_name>
    <x>{widget_row_left + 400}</x>
    <y>{widget_row_top}</y>
    <width>120</width>
    <height>20</height>
    <vertical_alignment>1</vertical_alignment>
  </widget>
  {generate_widget_input(record_type, record_name, widget_row_left, widget_row_top)}
  <widget type="label" version="2.0.0">
    <name>Label_2</name>
    <text>{desc}</text>
    <x>{widget_row_left + 670}</x>
    <y>{widget_row_top}</y>
    <width>290</width>
    <height>20</height>
    <wrap_words>false</wrap_words>
    <vertical_alignment>1</vertical_alignment>
  </widget>
  {generate_widget_INP_OUT(record_type, INP, OUT, widget_row_left, widget_row_top):}
"""



def generate_widget_input(record_type, record_name, widget_row_left, widget_row_top):
    if record_type == "aao" or record_type == "ao" or record_type == "longout" or record_type == "lso" or record_type == "stringout":
        return f"""
  <widget type="textentry" version="3.0.0">
    <name>Text Entry</name>
    <pv_name>{record_name}</pv_name>
    <x>{widget_row_left + 530}</x>
    <y>{widget_row_top}</y>
    <height>20</height>
  </widget>
"""
    elif record_type == "bo" or record_type == "mbbo" or record_type == "mbboDirect":
        return f"""
  <widget type="combo" version="2.0.0">
    <name>Combo Box</name>
    <pv_name>{record_name}</pv_name>
    <x>{widget_row_left + 530}</x>
    <y>{widget_row_top}</y>
    <height>20</height>
  </widget>
"""
    else:
        return ""


def generate_widget_INP_OUT(record_type, INP, OUT, widget_row_left, widget_row_top):
    if record_type == "bo" or record_type == "mbbo" or record_type == "mbboDirect" or record_type == "aao" or record_type == "ao" or record_type == "longout" or record_type == "lso" or record_type == "stringout":
        return f"""
  <widget type="label" version="2.0.0">
    <name>Label_2</name>
    <text>{OUT}</text>
    <x>{widget_row_left + 1000}</x>
    <y>{widget_row_top}</y>
    <width>290</width>
    <height>20</height>
    <wrap_words>false</wrap_words>
    <vertical_alignment>1</vertical_alignment>
  </widget>
"""
    else :
        return f"""
  <widget type="label" version="2.0.0">
    <name>Label_2</name>
    <text>{INP}</text>
    <x>{widget_row_left + 1000}</x>
    <y>{widget_row_top}</y>
    <width>290</width>
    <height>20</height>
    <wrap_words>false</wrap_words>
    <vertical_alignment>1</vertical_alignment>
  </widget>
"""

line = f.readline()
result = bob_header


while line:
    # print(line)
    
    # a new record starts
    if line.strip().startswith("record"):
        # dump the previous info
        if (inside_record == True):
            result = result + generate_widget_row(record_count)

        inside_record = False
        record_name = ""
        record_type = ""
        desc = ""
        egu = "" 
        record_count = record_count + 1
    parse_line(line)    
    line = f.readline()

result = result + generate_widget_row(record_count)        

f.close()

result = result + bob_tail

file_name = file_path.replace(".db", ".bob")
with open(file_name, "w") as f:
    f.write(result + "\n")
    print("Success:\n  ", file_path, "-->", file_name)
