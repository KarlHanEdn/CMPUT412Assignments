FROM 9e26d37f8a2a

WORKDIR /color_detector_dir

COPY ./color_detector_dir/requirements.txt .

RUN pip install -r requirements.txt

COPY ./color_detector_dir/color_detector.py .

CMD python3 ./color_detector.py

