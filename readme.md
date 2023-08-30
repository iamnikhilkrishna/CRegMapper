
# C Reg Mapper

  

This is a python tool to create masks and corresponding shift values as C #defines.

This python tool parses the **regs.json** file to create a **regs_def.h** include file with all the necessary bit mappings.C reg mapper also creates a structure mapping of all the register represented as appropriate unsigned data type.

This mapper tool can be used for generating required #defines to deal with bit banked data which are most common in embedded system applications.

  
  

## Configuration Json file
 

A JSON configuration file is used to pass the information such as module/device name, register bit size, register name and number of bits used to represent various data.

The refernce configuration file can be used as a starting point.

A brief description of the configurable items in the configuration file.

- DEV_NAME -> Name of the module

- REG_SIZE -> Size in bytes of each memory fields in the module.Available options are 8 bits/16 bits/32 bits and 64 bits.

- REGS --> An array of JSON objects having REG_NAME field and individual data field name as key followed by number of bits used representing the data field as value.The order of defining the data fields must be from LSB first.