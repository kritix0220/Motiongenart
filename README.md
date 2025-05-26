# Motiongenart
A Python script that generates generative art using motion detection from webcam input
A real-time computer vision application that generates beautiful mathematical art based on motion detected through your webcam. The more you move, the more dynamic the art becomes!
✨ Features

Real-time motion detection using OpenCV
Dynamic art generation with mathematical functions that respond to movement
Customizable parameters for motion sensitivity and art generation
Cooldown system to prevent spam generation
Live webcam feed with motion level display

🔧 How it Works

Motion Detection: Captures frames from your webcam and calculates motion levels using frame differencing
Art Generation: When significant motion is detected, it generates unique mathematical art using the Samila library
Dynamic Visualization: The art's characteristics change based on the intensity of detected motion

📦 Dependencies

opencv-python: Computer vision and webcam handling
numpy: Mathematical operations
Samila: Generative art creation
matplotlib: Visualization and plotting

📖 Usage

Start the application: Run python main.py
Position yourself: Make sure you're visible in the webcam feed
Move around: Wave your hands, dance, or move around to trigger art generation
Enjoy the art: Watch as your movements create unique mathematical visualizations
Exit: Press 'q' to quit the application

⚙️ Configuration
You can customize the application by modifying these parameters in main.py:
you can play with these parameters as you see fit:

motion_threshold: Minimum motion level to trigger art generation (default: 5000)
cooldown: Time in seconds between art generations (default: 5)
normalized_motion: Motion scaling factor (default: 10000000.0)
