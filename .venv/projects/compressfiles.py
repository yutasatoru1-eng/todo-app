import FreeSimpleGUI as fsg

label1= fsg.Text("Select File to compress:")
input1= fsg.Input()

label2= fsg.Text("Select destination folder:")
input2= fsg.Input()


compress_buton=fsg.Button("Compress")

window=fsg.Window("File compressor",layout=[[label1,input1,choose_buton1],[label2,input2,choose_buton2],[compress_buton]])

window.read()
window.close()
