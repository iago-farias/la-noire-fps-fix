from ReadWriteMemory import ReadWriteMemory

# Valor padrão: 59.93999863

fpsFinalValue = 119.8

rmv = ReadWriteMemory()
process = rmv.get_process_by_name("LANoire.exe") 
process.open()

fps_pointer = process.get_pointer(0x151AC40, offsets=[0xE8]) # Recupera o ponteiro que guarda o valor que trava o jogo a 30fps. Usando o endereço estático somado ao offset E8
fpsActualValue = process.readFloat(fps_pointer)

print("Valor inicial:" + str(fpsActualValue))

process.writeFloat(fps_pointer, fpsFinalValue) # Com o ponteiro recuperado escreve na memória o valor 119.8 para que o jogo rode a 60fps

fpsActualValue = process.readFloat(fps_pointer)
print("Valor após as escrita:" + str(fpsActualValue))

process.close()