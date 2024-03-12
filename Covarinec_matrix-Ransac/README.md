
### To run this code following libraries are required
* OpenCV, 
* random, 
* matplotlib, 
* NumPy, 
* time,
* glob,
* pandas.

### Installation (For ubuntu 18.04) ###
* OpenCV
	````
	sudo apt install python3-opencv
	````
* matplotlib
	````
	python -m pip install -U matplotlib
	````
* NumPy
	````
	pip install numpy
	````
	
### Running code in ubuntu
After changing the path of the video source file and installing dependencies
Make sure that current working derectory is same as the directory of program
You can change the working derectory by using **cd** command

* Run the following command to get Covarience Matrix and to plot the eiganvectors
````
Covarience matrix.py
````
* Run the following command to plot the LS, TLS, RANSAC on the dataset 
````
LS,TLS,RANSAC.py
````

### Troubleshooting ###
	Most of the cases the issue will be incorrect file path.
	Double check the path by opening the properies of the video and while writing the frames
	Also check the path using glob libarary while calling the images.
	Make sure the CSV file path is correct to get the dataset
	and copying path directly from there.

	For issues that you may encounter create an issue on GitHub.
### Maintainers ###
	Nisarg Upadhyay(nisargupadhyay2@gmail.com)
