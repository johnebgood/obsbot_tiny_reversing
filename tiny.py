#!/usr/bin/python3
# Generated by usbrply
# cmd: /usr/local/bin/usbrply --device-hi --vid 0x6130 --pid 0xfef0 --sleep --wrapper --comment --setup --halt -p data/sunday5.pcapng
import pygame
import binascii
import struct
import time
import usb1

def open_dev(usbcontext=None):
    if usbcontext is None:
        usbcontext = usb1.USBContext()
    
    print('Scanning for devices...')
    for udev in usbcontext.getDeviceList(skip_on_error=True):
        vid = udev.getVendorID()
        pid = udev.getProductID()
        print("%04x:%04x"%(vid, pid))
        if (vid, pid) == (0x6e30, 0xfef0):
            print("")
            print("")
            print('Found device')
            print('Bus %03i Device %03i: ID %04x:%04x' % (
                udev.getBusNumber(),
                udev.getDeviceAddress(),
                vid,
                pid))
            print("aa")
            return udev.open()
    raise Exception("Failed to find a device")

if __name__ == "__main__":
    import argparse 
    
    parser = argparse.ArgumentParser(description='Replay captured USB packets')
    args = parser.parse_args()

    usbcontext = usb1.USBContext()
    usbdev = open_dev(usbcontext)
    for i in range(1):
        print(i)
        if usbdev.kernelDriverActive(i):
            print("detaching", i)
            usbdev.detachKernelDriver(i)
    
    usbdev.claimInterface(0)
    usbdev.resetDevice()
    


    background_colour = (255,255,255)
    (width, height) = (300, 200)
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('obsbot_tiny_reversing')
    screen.fill(background_colour)
    pygame.display.flip()
    running = True
    while running:
        
        pygame.mouse.set_pos = (400, 300)
        mouse_move = (0,0)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                    running = False

                if event.key == pygame.K_LEFT:
                    usbdev.controlWrite(0x21, 0x01, 0x0200, 0x0A00, b"\xAA\x00\x19\x10\x00\x0E\x82\x44\x00\xE3\x30\x23\x03\x00\x00\x48\x43\x23\xC5\xC5\xC0\x19\xDA\xEA\x41\x00\x75\x00\x72\x00\x00\x00\xC0\xA9\x3C\xEA\xA9\x02\x00\x00\x23\x1F\x6B\x46\x00\xBB\x03\x80\xC0\xAC\x3C\xEA\xA9\x02\x00\x00\x40\xAB\x3C\xEA", 1000)
                if event.key == pygame.K_RIGHT:
                    usbdev.controlWrite(0x21, 0x01, 0x0200, 0x0A00, b"\xAA\x00\x19\x10\x00\x1D\x90\x7D\x00\xE3\x30\x23\x03\x00\x00\x48\x43\xF3\x24\x32\xC0\xFB\x41\xD7\xC1\x00\x00\x00\x00\x00\x00\x00\xE0\xAD\x3C\xEA\xA9\x02\x00\x00\x45\x1F\x09\x46\x00\xB1\x03\x90\x01\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00", 1000)
                if event.key == pygame.K_UP:
                    usbdev.controlWrite(0x21, 0x01, 0x0200, 0x0A00, b"\xAA\x00\x19\x10\x00\x1B\x4F\x84\x00\xE3\x30\x23\x03\x00\x00\x48\x43\x96\x27\xE1\xC1\x62\xBB\x59\xC0\x00\x00\x00\x00\x00\x00\x00\x70\xA5\x3C\xEA\xA9\x02\x00\x00\x4F\x1E\x07\x47\x00\x5F\x03\x80\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00", 1000)
                if event.key == pygame.K_DOWN:
                    usbdev.controlWrite(0x21, 0x01, 0x0200, 0x0A00, b"\xAA\x00\x19\x10\x00\x2B\x20\x2B\x00\xE3\x30\x23\x03\x00\x00\x48\x43\x5C\xFD\xC0\x41\x84\x8E\x0A\x40\x00\x70\x00\x65\x00\x67\x00\x00\x00\x3C\xEA\xA9\x02\x00\x00\x0B\x1E\x43\x47\x00\x73\x03\x80\x00\x00\x00\x00\x02\x00\x00\x00\x00\x00\x00\x00", 1000)
                if event.key == pygame.K_r:
                    usbdev.controlWrite(0x21, 0x01, 0x0600, 0x0A00, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00", 1000)
                
                if event.key == pygame.K_a:
                    print("ai on")
                    usbdev.controlWrite(0x21, 0x01, 0x0300, 0x0A00, b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
                if event.key == pygame.K_b:
                    print("ai off")
                    usbdev.controlWrite(0x21, 0x01, 0x0300, 0x0A00, b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")
                



            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:                        
                    usbdev.controlWrite(0x21, 0x01, 0x0200, 0x0A00, b"\xAA\x00\x19\x10\x00\x31\x3A\x3A\x00\xE3\x30\x23\x03\x00\x00\x48\x43\x00\x00\x00\x00\x00\x00\x00\x00\x6E\x67\x00\x6E\x00\x73\x00\x00\x00\x3C\xEA\xA9\x02\x00\x00\xE3\x1E\xAB\x47\x00\x7B\x03\x80\xE8\xC6\x6A\x7E\xFF\x7F\x00\x00\xB0\x31\x37\xE7", 1000)
                    #print("up")
            
            if event.type == pygame.MOUSEMOTION:
                mouse_move = event.rel 
            if mouse_move != (0,0):
                print(mouse_move)
        
        #presumably some accelerometer
        #mybytes = usbdev.controlRead(0xA1, 0x81 , 0x0D00, 0x0100, 8)                
        #mybytes = usbdev.controlRead(0xA1, 0x81 , 0x0E00, 0x0100, 8)
        
        #print(mybytes)
        #a = struct.unpack('<HHHH', p)
        print(''.join(format(byte, '08b') for byte in usbdev.controlRead(0xA1, 0x81 , 0x0D00, 0x0100, 8)))
        #print(''.join(format(byte, '08b') for byte in usbdev.controlRead(0xA1, 0x81 , 0x0E00, 0x0100, 8)))
        