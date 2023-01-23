import cv2
import numpy as np

# from https://docs.duckietown.org/daffy/duckietown-robotics-development/out/creating_docker_containers.html
def gst_pipeline_string():
    # Parameters from the camera_node
    # Refer here : https://github.com/duckietown/dt-duckiebot-interface/blob/daffy/packages/camera_driver/config/jetson_nano_camera_node/duckiebot.yaml
    res_w, res_h, fps = 640, 480, 30
    fov = 'full'
    # find best mode
    camera_mode = 3  # 
    # compile gst pipeline
    gst_pipeline = """ \
            nvarguscamerasrc \
            sensor-mode= exposuretimerange="100000 80000000" ! \
            video/x-raw(memory:NVMM), width=, height=, format=NV12, 
                framerate=/1 ! \
            nvjpegenc ! \
            appsink \
        """.format(
        camera_mode,
        res_w,
        res_h,
        fps
    )

    # ---
    print("Using GST pipeline: ``".format(gst_pipeline))
    return gst_pipeline


def main():
    cap = cv2.VideoCapture()
    cap.open(gst_pipeline_string(), cv2.CAP_GSTREAMER)
    if not cap.isOpened():
        print("cannot open camera!")
        return
    while True:
        ret, frame = cap.read()
        if not ret:
            print("failed to get image, stopping...")
            break
        
        # color detector code here
        # unable to complete due to dt-duckiebot-interface issues
        
        cv2.imshow(frame)
    print("program exiting...")


if __name__ == "__main__":
    main()