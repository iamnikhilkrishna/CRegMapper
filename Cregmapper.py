import sys
import json


def readConfig(absFilenamePath):
    try:
        with open(absFilenamePath) as configfile:
            regjson = configfile.read()
            return json.loads(regjson)
    except Exception:
        print("Reading configuration file error ")

def createOutFile(filename):
    print("Creating file:  " + filename+'_regDef.h \n')
    try:
        outfile = open(filename+'_regDef.h','w')
        outfile.writelines('#define '+ filename.upper() + '_REG_DEFS\n')
        outfile.writelines('#ifdef '+ filename.upper() + '_REG_DEFS\n')
        outfile.writelines('\n#include <stdint.h> \n\n')
    except FileNotFoundError:
        print("File not found , Unable to create file ")
    return outfile

def closeOutFile(Outfd,filename):
    try:
        Outfd.writelines('\n\n\n\n')
        Outfd.writelines('#endif //'+filename.upper() + '_REG_DEFS\n')
        Outfd.close()
        print("Completed register mapping \n")
    except Exception:
        print("File closing error ")

def getFormatstr(regSize):
    switcher={
        8:'#04X',
        16:'#06X',
        32:'#010X',
        64:'#020X'
    }
    return switcher.get(regSize, "#020X")

def getCType(regSize):
    switcher={
        8:'uint8_t',
        16:'uint16_t',
        32:'uint32_t',
        64:'uint64_t'
    }
    return switcher.get(regSize,'Type not found')

def getMaskValue(startPos,numbits):
    maskval = 0
    while(numbits > 0):
        if startPos == 0:
            maskval = 1
        else:
            maskval = maskval ^ (1 << (startPos))
        startPos = startPos + 1
        numbits = numbits - 1
    return maskval


def createMasks(devName,regDetails,outfd,regSize):
    bitposCount =0
    bitMaskVal = 1
    formatStr = getFormatstr(regSize)
    
    try:
        regName = regDetails['REG_NAME']
        regdesc = {key:value for key , value in regDetails.items() if key != 'REG_NAME'}
        for regKey,numBitsValue in regdesc.items():
            if "RESERVED" not in regKey:
                bitMaskVal = getMaskValue(bitposCount,numBitsValue)
                outfd.writelines('#define ' + devName.upper()  + '_' + regName.upper() + '_' + regKey.upper() + '_MASK '+' ' + format(bitMaskVal,formatStr) + '\n' )
                outfd.writelines('#define ' + devName.upper()  + '_' + regName.upper() + '_' + regKey.upper() +  '_SHIFT_VAL '+ ' ' + str(bitposCount) + '\n' )
                outfd.writelines('\n')
            bitposCount = bitposCount + numBitsValue
    except Exception:
        print("json configuration format error,the generated map file may be incomplete ")
        
def createStructHeader(outfd):
    try:
        outfd.writelines('typedef struct{ \n')
    except Exception:
        print("Output file write error ")

def createStructFooter(devName,outfd):
    try:
        outfd.writelines('} ' + devName.lower() + '_t; \n\n')
    except Exception:
        print("Output file write error ")

def addToStruct(regDetails,outfd,regSize):
    try:
        TypeStr = getCType(regSize)
        if 'Type not found' not in TypeStr:
            outfd.writelines(TypeStr + ' ' + regDetails["REG_NAME"].lower() + ';\n')
        else: print("Unknown type of regs in config ...\n aborting .... \n")
    except Exception: print("Adding to output file error")


def doMapping(configJson):
    try:
        outfd = createOutFile(configJson['DEV_NAME'])
        regSize=configJson["REG_SIZE"]
        createStructHeader(outfd)
        for regDetails in configJson['REGS']: addToStruct(regDetails,outfd,regSize)
        createStructFooter(configJson['DEV_NAME'],outfd)
        for regDetails in configJson['REGS']: createMasks(configJson['DEV_NAME'],regDetails,outfd,regSize)
        closeOutFile(outfd,configJson['DEV_NAME'])
    except Exception: print("Invalid json configuration, the generated map file may be incomplete")
    
        

def main():
    if len(sys.argv) > 1:
        print("C Reg Mapper in action \n")
        print("Openning Config file: "+ sys.argv[1])
        Configjson=readConfig(sys.argv[1])
        doMapping(Configjson)
    else: print('\nInsufficent arguments \n')


if __name__=="__main__":
    main()