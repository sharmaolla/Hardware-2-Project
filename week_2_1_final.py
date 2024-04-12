from filefifo import Filefifo

data = Filefifo(10, name = 'capture_250Hz_01.txt')
peaks = []
prev = 0
curr = 0
going_up = True

for i in range(1000):
    curr = data.get()
    
    if prev > curr and going_up:
        peaks.append(i-1)
        going_up = False
        
    if prev < curr and  not going_up:
        going_up = True     
       
    prev = curr
print(peaks)
sub = peaks[-1] - peaks[-2] 
print("The number of samples is", sub)
ppi = sub * 0.004
ppi_ms = sub * 4
print("The PPI", round(ppi, 2), "sec  OR", ppi_ms, "ms.")
frequency = 1/ ppi
print("The frequency is", round(frequency, 2), "Hz")
