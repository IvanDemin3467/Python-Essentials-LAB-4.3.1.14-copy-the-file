# This is the Python Essentials 2 LAB 4.3.1.14 copy the file

from os import strerror

srcname = input("Enter the source file name: ") # ask the user for the name of the file to copy
try:
    src = open(srcname, 'rb') # try to open it to read
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno)) # terminate the program
                                                              # execution if the open fails
    exit(e.errno) #the exit() function stops program execution
                  # and passes the completion code to the OS;
                  # any completion code other than 0 says that the program has encountered
                  # some problems; use the errno value to specify the nature of the issue	

dstname = input("Enter the destination file name: ") # repeat nearly the same action, 
try:                                                 # but this time for the output file
    dst = open(dstname, 'wb')
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

# prepare a piece of memory for transferring data from the source file to the target one;
buffer = bytearray(65536)
total  = 0 # count the bytes copied - this is the counter and its initial value
try:
    readin = src.readinto(buffer) # try to fill the buffer for the very first time
    while readin > 0: # as long as you get a non-zero number of bytes, repeat the same actions
        written = dst.write(buffer[:readin]) # write the buffer's contents to the output file 
        # a slice is used to limit the number of bytes being written,
        # as write() always prefer to write the whole buffer
        total += written                     # update the counter
        readin = src.readinto(buffer)        # read the next file chunk
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	

# some final cleaning - the job is done
print(total,'byte(s) succesfully written')
src.close()
dst.close()
