# Ocean One Mp4 Server

This repo creates an http server on localhost:5000, which serves an mp4 video at http://localhost:5000/o1k.mp4. To start the server, simply run python server.py. 

Also included is an mp4 writer that converts jpgs in a folder to a video. This video will be served for the server. The workflow is:
1.)  Start the server with the default mp4
2.)  Run the stereo visualizer script to write jpg to specified file continuously
3.)  Run the mp4 writer script to continuously create mp4 videos upon trigger of a number of jpg files. This also triggers the deletion of all the current files up to this point.

After confirmation of the above processes, then run the Android application sample-play-sbs-video on the tablet. 

