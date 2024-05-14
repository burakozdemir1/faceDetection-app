import sensor, time, image, lcd

sensor.reset() # Resetting the camera driver's registers

sensor.set_pixformat(sensor.RGB565) # Selecting the pixel format to be used

sensor.set_framesize(sensor.QQVGA) # Using a resolution of 160x120 pixels

sensor.skip_frames(time = 2000) # Waiting for 2 seconds

face_cascade = image.HaarCascade("frontalface", stage=25) # Loading the Haar Cascade algorithm to detect faces. "frontalface" file is used to detect frontal faces.

lcd.init(type=2) # Initializing the LCD screen

clock = time.clock() # Creating a clock object to measure frame rate

while True:
    clock.tick()
    
    img = sensor.snapshot() # Capturing a single frame image from the camera sensor
    
    objects = img.find_features(face_cascade, threshold=0.5, scale_factor=1.5) # Detecting faces in the captured image and returning the objects found
    # This line detects faces in the 'img' image and assigns them to a list named 'objects'. 
    # The 'threshold' parameter specifies how reliable the detected faces should be. The 'scale_factor' parameter specifies how large the cascade should detect faces in the image.
    
    count = 0
    for r in objects:  # Looping through detected faces to draw a rectangle around them and count how many faces were detected
        img.draw_rectangle(r) # Drawing a rectangle on the image
        print("%s %s" % (count,r)) # Printing the count of detected faces and their location (x,y)
        count = count + 1 # Incrementing the count of detected objects
        
    lcd.display(img) # Displaying the captured image with rectangles drawn around detected faces on the LCD screen
    
    print(clock.fps()) # Printing the frames per second (FPS) value
